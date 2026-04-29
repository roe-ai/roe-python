"""Dynamic-input pre-processor for agent execution requests.

Splits a user-supplied ``inputs`` dict into ``(form_data, files)`` suitable
for ``httpx``'s ``data=`` and ``files=`` kwargs. Detects:

  * ``FileUpload`` instances → ``files``
  * file-like objects (``io.IOBase``, anything with ``.read()``) → ``files``
  * UUID strings → ``form_data`` (Roe file ID reference, never opened)
  * existing file paths → ``files`` (auto-opened in binary mode)
  * everything else → stringified into ``form_data``

Bypasses the generated request models' ``to_multipart()`` because
``openapi-python-client`` encodes every additional property as
``(None, str(prop).encode(), "text/plain")`` — which silently sends a file's
``repr`` instead of its bytes.
"""

from __future__ import annotations

import io
import json as _json
import mimetypes
from pathlib import Path
from typing import Any

from roe.models.file import FileUpload
from roe.utils.file_detection import is_file_path, is_uuid_string


def build_execution_multipart(
    inputs: dict[str, Any],
    metadata: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Split inputs into ``(form_data, files)`` for an httpx multipart request.

    Detects ``FileUpload``, file-like objects, file-path strings, UUID strings
    (treated as Roe file references — kept in form data, not opened), and
    plain scalars. ``metadata`` is JSON-encoded into the form when present.
    """
    form_data: dict[str, Any] = {}
    files: dict[str, Any] = {}

    for key, value in inputs.items():
        if isinstance(value, FileUpload):
            filename, file_obj, mime_type = value.to_multipart_tuple()
            files[key] = (filename, file_obj, mime_type)
        elif isinstance(value, (io.IOBase, io.BytesIO)) or hasattr(value, "read"):
            files[key] = value
        elif isinstance(value, str):
            if is_uuid_string(value):
                form_data[key] = value
            elif is_file_path(value):
                p = Path(value)
                mime, _ = mimetypes.guess_type(p.name)
                with open(value, "rb") as fh:
                    files[key] = (p.name, fh.read(), mime or "application/octet-stream")
            else:
                form_data[key] = value
        else:
            if value is not None:
                form_data[key] = str(value)

    if metadata is not None:
        form_data["metadata"] = _json.dumps(metadata)

    return form_data, files
