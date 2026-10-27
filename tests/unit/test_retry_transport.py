"""Verify RoeRetryTransport only replays requests that are safe to send twice."""

from __future__ import annotations

import os
import sys

import httpx
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from roe.utils import transport  # noqa: E402
from roe.utils.transport import RoeRetryTransport  # noqa: E402


@pytest.mark.parametrize(
    ("method", "error", "expected_attempts"),
    [
        # The request may already have reached the server: never resend a POST.
        ("POST", httpx.ReadTimeout, 1),
        ("PATCH", httpx.RemoteProtocolError, 1),
        # The request never left the client, so resending is safe.
        ("POST", httpx.ConnectError, 4),
        ("POST", httpx.ConnectTimeout, 4),
        # Idempotent methods keep retrying every transport error.
        ("GET", httpx.ReadTimeout, 4),
        ("DELETE", httpx.ReadTimeout, 4),
    ],
)
def test_transport_error_retries(monkeypatch, method, error, expected_attempts):
    attempts = []

    def fail(self, request):
        attempts.append(request.method)
        raise error("boom", request=request)

    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", fail)
    monkeypatch.setattr(transport.time, "sleep", lambda _: None)

    request = httpx.Request(method, "https://api.roe-ai.com/v1/workflows/w/runs/")
    with pytest.raises(error):
        RoeRetryTransport(max_retries=3).handle_request(request)
    assert len(attempts) == expected_attempts
