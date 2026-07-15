from __future__ import annotations

from typing import Any

from roe._generated.client import AuthenticatedClient
from roe._generated.types import UNSET, Unset
from roe.exceptions import translate_response


class _DictBody:
    def __init__(self, value: dict[str, Any]):
        self.value = value

    def to_dict(self) -> dict[str, Any]:
        return self.value


def request_raw(
    raw: AuthenticatedClient,
    ep_module: Any,
    *path_args: Any,
    body: Any = UNSET,
    extra_headers: dict[str, str] | None = None,
    **kwargs: Any,
) -> Any:
    """Call a generated endpoint while forcing JSON body serialization."""
    if not isinstance(body, Unset):
        generated_body = _DictBody(body) if isinstance(body, dict) else body
        request_kwargs = ep_module._get_kwargs(
            *path_args, body=generated_body, **kwargs
        )
        request_kwargs.pop("data", None)
        request_kwargs.pop("files", None)
        request_kwargs["json"] = body.to_dict() if hasattr(body, "to_dict") else body
        headers = request_kwargs.setdefault("headers", {})
        headers["Content-Type"] = "application/json"
    else:
        request_kwargs = ep_module._get_kwargs(*path_args, **kwargs)

    if extra_headers:
        request_kwargs.setdefault("headers", {}).update(extra_headers)

    response = raw.get_httpx_client().request(**request_kwargs)
    translate_response(response)
    return response


def request_json(
    raw: AuthenticatedClient,
    ep_module: Any,
    *path_args: Any,
    body: Any = UNSET,
    **kwargs: Any,
) -> Any:
    """Call a generated endpoint and parse a successful JSON response.

    Some generated endpoints advertise the same request model under JSON,
    form, and multipart content types. openapi-python-client emits all three
    branches and the final multipart branch wins, which breaks nested
    dict/list fields such as policy content and agent engine_config. The SDK
    wrappers intend these requests to be JSON, so normalize before dispatch.
    """
    response = request_raw(
        raw,
        ep_module,
        *path_args,
        body=body,
        **kwargs,
    )
    return ep_module._build_response(client=raw, response=response)
