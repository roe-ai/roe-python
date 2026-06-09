"""Multipart-bypass helper for the dynamic-input agent run endpoints.

`openapi-python-client`'s generated `AgentExecutionRequestRequest.to_multipart()`
encodes every dynamic input as `(None, str(prop).encode(), "text/plain")` —
which silently sends a file's `repr` instead of its bytes. To send real
multipart with the right MIME types we bypass the model and call the generated
endpoint's `_get_kwargs(...)` directly, then mutate the kwargs to inject our
own `data=` and `files=` before handing them to httpx.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

import httpx

from roe._generated.client import AuthenticatedClient
from roe.exceptions import translate_response
from roe.utils.inputs import build_execution_multipart_payload


def call_dynamic(
    raw: AuthenticatedClient,
    ep_module: Any,
    *,
    inputs: dict[str, Any],
    metadata: dict[str, Any] | None,
    organization_id: UUID,
    extra_headers: dict[str, str] | None = None,
    **path_params: Any,
) -> httpx.Response:
    """Send a multipart request through the generated endpoint's URL/auth machinery.

    Calls `ep_module._get_kwargs(...)` to build the URL, query string and auth,
    then strips the generated body and replaces it with our own multipart
    payload built from `build_execution_multipart_payload`. Raises a typed
    `RoeAPIException` on non-2xx via `translate_response`.
    """
    multipart = build_execution_multipart_payload(inputs, metadata)
    kwargs = ep_module._get_kwargs(organization_id=organization_id, **path_params)
    kwargs.pop("json", None)
    kwargs.pop("data", None)
    kwargs.pop("files", None)
    kwargs["data"] = multipart.data
    kwargs["files"] = multipart.files
    request_headers = kwargs.setdefault("headers", {})
    request_headers["x-roe-skip-retry"] = (
        "1"  # multipart POST — do not replay (aligns with TS)
    )
    if extra_headers is not None:
        request_headers.update(extra_headers)
    request_headers.pop("Content-Type", None)  # let httpx pick the boundary
    try:
        response = raw.get_httpx_client().request(**kwargs)
        translate_response(response)
        return response
    finally:
        multipart.close()
