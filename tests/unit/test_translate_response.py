"""Verify translate_response maps status codes to typed exceptions."""

from __future__ import annotations

import os
import sys
from http import HTTPStatus

import httpx
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from roe.exceptions import (  # noqa: E402
    AuthenticationError,
    BadRequestError,
    ForbiddenError,
    InsufficientCreditsError,
    NotFoundError,
    RoeAPIException,
    ServerError,
    translate_response,
)


def _resp(status: int, content: bytes = b"") -> httpx.Response:
    return httpx.Response(status, content=content)


def test_2xx_is_noop():
    translate_response(_resp(200, b'{"ok": true}'))
    translate_response(_resp(204))


@pytest.mark.parametrize(
    "status,exc_type",
    [
        (400, BadRequestError),
        (401, AuthenticationError),
        (402, InsufficientCreditsError),
        (403, ForbiddenError),
        (404, NotFoundError),
        (429, RoeAPIException),
        (500, ServerError),
        (502, ServerError),
    ],
)
def test_status_codes_map_to_typed_exceptions(status, exc_type):
    with pytest.raises(exc_type) as exc_info:
        translate_response(_resp(status, b'{"detail": "boom"}'))
    assert exc_info.value.status_code == status
    assert exc_info.value.message == "boom"


def test_dict_body_extracts_detail():
    with pytest.raises(BadRequestError) as exc_info:
        translate_response(_resp(400, b'{"detail": "bad"}'))
    assert exc_info.value.message == "bad"
    assert exc_info.value.response == {"detail": "bad"}


def test_list_body_joined_as_message():
    with pytest.raises(BadRequestError) as exc_info:
        translate_response(_resp(400, b'["a", "b"]'))
    assert exc_info.value.message == "a; b"
    assert exc_info.value.response is None


def test_non_json_body_falls_back_to_status_snippet():
    with pytest.raises(NotFoundError) as exc_info:
        translate_response(_resp(404, b"<html>not found</html>"))
    assert "404" in exc_info.value.message


def test_empty_body():
    with pytest.raises(NotFoundError) as exc_info:
        translate_response(_resp(404))
    assert exc_info.value.message == "HTTP 404"


def test_accepts_generated_response_shape():
    """Response from openapi-python-client uses HTTPStatus + bytes content."""

    class FakeResp:
        status_code = HTTPStatus(403)
        content = b'{"error": "forbidden"}'

    with pytest.raises(ForbiddenError) as exc_info:
        translate_response(FakeResp())
    assert exc_info.value.message == "forbidden"


def test_dict_body_uses_error_key_when_no_detail():
    with pytest.raises(BadRequestError) as exc_info:
        translate_response(_resp(400, b'{"error": "bad input"}'))
    assert exc_info.value.message == "bad input"


def test_dict_body_uses_message_key_as_fallback():
    with pytest.raises(BadRequestError) as exc_info:
        translate_response(_resp(400, b'{"message": "broken"}'))
    assert exc_info.value.message == "broken"


def _resp_with_headers(
    status: int, headers: dict[str, str], content: bytes = b'{"detail":"x"}'
) -> httpx.Response:
    return httpx.Response(status, headers=headers, content=content)


def test_429_retry_after_seconds_preserved_in_headers():
    with pytest.raises(RoeAPIException) as exc_info:
        translate_response(_resp_with_headers(429, {"Retry-After": "7"}))
    assert exc_info.value.headers is not None
    assert exc_info.value.headers.get("retry-after") == "7"


def test_429_retry_after_http_date_preserved_in_headers():
    date = "Wed, 21 Oct 2025 07:28:00 GMT"
    with pytest.raises(RoeAPIException) as exc_info:
        translate_response(_resp_with_headers(429, {"Retry-After": date}))
    assert exc_info.value.headers.get("retry-after") == date


def test_429_no_retry_after_header_when_absent():
    """httpx still synthesises content-length etc., so the headers dict isn't
    empty — but `retry-after` must not be present when the server didn't send it."""
    with pytest.raises(RoeAPIException) as exc_info:
        translate_response(_resp(429, b'{"detail":"throttled"}'))
    assert exc_info.value.headers is not None
    assert "retry-after" not in exc_info.value.headers


def test_404_headers_preserved_general_feature():
    with pytest.raises(NotFoundError) as exc_info:
        translate_response(_resp_with_headers(404, {"x-request-id": "abc-123"}))
    assert exc_info.value.headers.get("x-request-id") == "abc-123"


def test_500_headers_preserved_general_feature():
    with pytest.raises(ServerError) as exc_info:
        translate_response(_resp_with_headers(500, {"x-trace": "t1"}))
    assert exc_info.value.headers.get("x-trace") == "t1"


def test_generated_response_with_uppercased_headers_normalised_to_lowercase():
    """The generated client's MutableMapping[str, str] preserves original HTTP
    casing (e.g. "Retry-After"). Callers must still be able to look up by
    lowercase, so __init__ normalises at store time."""

    class GeneratedRespStub:
        status_code = HTTPStatus(429)
        content = b'{"detail": "throttled"}'
        headers = {"Retry-After": "9", "X-Trace-Id": "abc"}

    with pytest.raises(RoeAPIException) as exc_info:
        translate_response(GeneratedRespStub())
    assert exc_info.value.headers is not None
    assert exc_info.value.headers.get("retry-after") == "9"
    assert exc_info.value.headers.get("x-trace-id") == "abc"


def test_response_without_headers_attribute_yields_none_headers():
    """A stub response that omits .headers should not crash; exc.headers becomes None."""

    class Stub:
        status_code = 500
        content = b'{"detail": "x"}'

    with pytest.raises(ServerError) as exc_info:
        translate_response(Stub())
    assert exc_info.value.headers is None


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
