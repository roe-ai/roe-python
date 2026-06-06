"""Dynamic-input pre-processor for agent execution requests.

Splits a user-supplied ``inputs`` dict into ``(form_data, files)`` suitable
for ``httpx``'s ``data=`` and ``files=`` kwargs. Detects:

  * ``FileUpload`` instances → ``files``
  * file-like objects (``io.IOBase``, anything with ``.read()``) → ``files``
  * UUID strings → ``form_data`` (Roe file ID reference, never opened)
  * existing file paths → ``files`` (auto-opened in binary mode and streamed)
  * everything else → stringified into ``form_data``

Bypasses the generated request models' ``to_multipart()`` because
``openapi-python-client`` encodes every additional property as
``(None, str(prop).encode(), "text/plain")`` — which silently sends a file's
``repr`` instead of its bytes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import io
import json as _json
import mimetypes
from pathlib import Path
from typing import Any, BinaryIO

from roe.models.file import FileUpload
from roe.utils.file_detection import is_file_path, is_uuid_string


@dataclass
class ExecutionMultipart:
    data: dict[str, Any]
    files: list[tuple[str, Any]]
    closeables: list[BinaryIO] = field(default_factory=list)

    def close(self) -> None:
        for file_obj in self.closeables:
            file_obj.close()


def build_execution_multipart(
    inputs: dict[str, Any],
    metadata: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], list[tuple[str, Any]]]:
    """Split caller-owned inputs into ``(form_data, files)`` for multipart.

    Use ``build_execution_multipart_payload`` for local paths or ``FileUpload``
    path values because it returns a payload object that can close SDK-opened
    file handles after the request.
    """
    multipart = build_execution_multipart_payload(inputs, metadata)
    if multipart.closeables:
        multipart.close()
        raise ValueError(
            "build_execution_multipart cannot safely return SDK-opened file "
            "handles. Use build_execution_multipart_payload(...) and call "
            "payload.close() after the request."
        )
    return multipart.data, multipart.files


def build_execution_multipart_payload(
    inputs: dict[str, Any],
    metadata: dict[str, Any] | None = None,
) -> ExecutionMultipart:
    """Build a multipart payload and track SDK-opened file objects."""
    form_data: dict[str, Any] = {}
    files: list[tuple[str, Any]] = []
    closeables: list[BinaryIO] = []

    try:
        for key, value in inputs.items():
            if isinstance(value, FileUpload):
                _append_file(files, closeables, key, value)
            elif _is_file_sequence(value):
                for item in value:
                    _append_file(files, closeables, key, item)
            elif _is_ambiguous_file_sequence(value):
                raise ValueError(
                    f"Agent input {key!r} mixes local file uploads with scalar "
                    "values. Use FileUpload/local paths for files, and pass URLs "
                    "or Roe file IDs as scalar inputs."
                )
            elif _is_raw_bytes(value):
                raise ValueError(
                    f"Agent input {key!r} is raw bytes. Use "
                    "FileUpload.from_bytes(..., filename=...) so Roe receives a "
                    "filename and MIME type."
                )
            elif isinstance(value, (io.IOBase, io.BytesIO)) or hasattr(value, "read"):
                files.append((key, value))
            elif isinstance(value, str):
                if is_uuid_string(value):
                    form_data[key] = value
                elif is_file_path(value):
                    _append_path_file(files, closeables, key, value)
                else:
                    form_data[key] = value
            else:
                if value is not None:
                    form_data[key] = str(value)

        if metadata is not None:
            form_data["metadata"] = _json.dumps(metadata)
    except Exception:
        for file_obj in closeables:
            file_obj.close()
        raise

    return ExecutionMultipart(data=form_data, files=files, closeables=closeables)


def _is_file_sequence(value: Any) -> bool:
    if not isinstance(value, (list, tuple)):
        return False
    return bool(value) and all(
        _is_file_value(item) or _is_file_path_string(item) for item in value
    )


def _is_ambiguous_file_sequence(value: Any) -> bool:
    if not isinstance(value, (list, tuple)):
        return False
    if any(_is_raw_bytes(item) for item in value):
        return True
    has_file = any(_is_file_value(item) or _is_file_path_string(item) for item in value)
    return has_file and not all(
        _is_file_value(item) or _is_file_path_string(item) for item in value
    )


def _is_file_value(value: Any) -> bool:
    return (
        isinstance(value, FileUpload)
        or isinstance(value, (io.IOBase, io.BytesIO))
        or hasattr(value, "read")
    )


def _is_file_path_string(value: Any) -> bool:
    return isinstance(value, str) and is_file_path(value)


def _is_raw_bytes(value: Any) -> bool:
    return isinstance(value, (bytes, bytearray, memoryview))


def _append_file(
    files: list[tuple[str, Any]],
    closeables: list[BinaryIO],
    key: str,
    value: Any,
) -> None:
    if isinstance(value, FileUpload):
        filename, file_obj, mime_type = value.to_multipart_tuple()
        files.append((key, (filename, file_obj, mime_type)))
        if value.path is not None:
            closeables.append(file_obj)
        return
    if _is_file_path_string(value):
        _append_path_file(files, closeables, key, value)
        return
    files.append((key, value))


def _append_path_file(
    files: list[tuple[str, Any]],
    closeables: list[BinaryIO],
    key: str,
    path: str,
) -> None:
    p = Path(path)
    mime, _ = mimetypes.guess_type(p.name)
    file_obj = open(path, "rb")
    files.append((key, (p.name, file_obj, mime or "application/octet-stream")))
    closeables.append(file_obj)
