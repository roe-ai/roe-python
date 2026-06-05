"""Large table upload helpers for the generated tables facade."""

from __future__ import annotations

import mimetypes
import time
from pathlib import Path
from typing import Any
from uuid import UUID

import httpx

from roe.exceptions import RoeAPIException, translate_response

TERMINAL_UPLOAD_STATUSES = frozenset({"COMPLETED", "FAILED", "EXPIRED"})
PRESIGNED_UPLOAD_TIMEOUT_SECONDS = 300.0
PRESIGNED_UPLOAD_MAX_RETRIES = 2
PRESIGNED_UPLOAD_RETRY_STATUSES = frozenset({500, 502, 503, 504})
FORBIDDEN_PRESIGNED_HEADERS = {
    "authorization",
    "x-organization-id",
    "x-roe-organization-id",
}


class TableUploadHelpersMixin:
    """Presigned-upload helpers composed into ``TablesAPI`` by codegen."""

    def create_upload(
        self,
        *,
        table_name: str,
        filename: str,
        content_type: str = "text/csv",
        with_headers: bool = True,
        organization_id: str | UUID | None = None,
    ) -> dict[str, Any]:
        """Create a presigned CSV upload session and return the PUT URL."""
        resolved_org = organization_id or self.config.organization_id
        return self._request_json(
            "POST",
            "/v1/tables/upload/presigned-url/",
            json_body=_compact_dict(
                {
                    "table_name": table_name,
                    "filename": filename,
                    "content_type": content_type,
                    "with_headers": with_headers,
                    "organization_id": str(resolved_org) if resolved_org else None,
                }
            ),
            expected_status={200, 201},
        )

    def complete_upload(self, *, upload_id: str | UUID) -> dict[str, Any]:
        """Start importing a previously uploaded presigned CSV object."""
        upload_id = _coerce_upload_id(upload_id)
        return self._request_json(
            "POST",
            f"/v1/tables/upload/{upload_id}/complete/",
            expected_status={200, 201, 202},
        )

    def upload_status(self, *, upload_id: str | UUID) -> dict[str, Any]:
        """Return the current status for a table upload session."""
        upload_id = _coerce_upload_id(upload_id)
        return self._request_json(
            "GET",
            f"/v1/tables/upload/{upload_id}/status/",
            expected_status={200},
        )

    def upload_large(
        self,
        file: str | Path,
        *,
        table_name: str,
        with_headers: bool = True,
        wait: bool = False,
        poll_interval: float = 2.0,
        timeout: float | None = None,
        organization_id: str | UUID | None = None,
        filename: str | None = None,
        mime_type: str | None = None,
    ) -> dict[str, Any]:
        """Upload a local CSV through the presigned storage path."""
        path = Path(file)
        if not path.is_file():
            raise FileNotFoundError(f"CSV file not found: {path}")

        effective_filename = filename or path.name
        content_type = _mime_type(effective_filename, mime_type)
        created = self.create_upload(
            table_name=table_name,
            filename=effective_filename,
            content_type=content_type,
            with_headers=with_headers,
            organization_id=organization_id,
        )
        _put_presigned_upload(
            upload_url=created["upload_url"],
            headers=created.get("headers") or {},
            file_path=path,
        )
        completed = self.complete_upload(upload_id=created["upload_id"])
        if not wait or completed.get("status") in TERMINAL_UPLOAD_STATUSES:
            return completed
        return self.wait_for_upload(
            upload_id=created["upload_id"],
            poll_interval=poll_interval,
            timeout=timeout,
        )

    def wait_for_upload(
        self,
        *,
        upload_id: str | UUID,
        poll_interval: float = 2.0,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        """Poll a table upload session until it reaches a terminal status."""
        upload_id = _coerce_upload_id(upload_id)
        if poll_interval <= 0:
            raise ValueError("poll_interval must be greater than 0")
        deadline = time.monotonic() + timeout if timeout is not None else None
        while True:
            result = self.upload_status(upload_id=upload_id)
            if result.get("status") in TERMINAL_UPLOAD_STATUSES:
                return result
            if deadline is not None and time.monotonic() >= deadline:
                raise TimeoutError(f"Timed out waiting for table upload {upload_id}")
            sleep_for = poll_interval
            if deadline is not None:
                sleep_for = min(sleep_for, max(0.0, deadline - time.monotonic()))
            time.sleep(sleep_for)

    def _request_json(
        self,
        method: str,
        path: str,
        *,
        json_body: dict[str, Any] | None = None,
        expected_status: set[int],
    ) -> dict[str, Any]:
        kwargs: dict[str, Any] = {}
        if json_body is not None:
            kwargs["json"] = json_body
        response = self._raw.get_httpx_client().request(method, path, **kwargs)
        if response.status_code not in expected_status:
            translate_response(response)
            raise RoeAPIException(
                f"{method} {path} returned unexpected HTTP {response.status_code}",
                status_code=response.status_code,
                headers=response.headers,
            )
        if not response.content:
            return {}
        try:
            data = response.json()
        except ValueError as exc:
            raise RoeAPIException(
                f"{method} {path} returned non-JSON body: {response.text!r}",
                status_code=response.status_code,
                headers=response.headers,
            ) from exc
        if not isinstance(data, dict):
            raise RoeAPIException(
                f"{method} {path} returned unexpected response shape: {data!r}",
                status_code=response.status_code,
                headers=response.headers,
            )
        return data


def _mime_type(filename: str, override: str | None) -> str:
    if override:
        return override
    guessed, _ = mimetypes.guess_type(filename)
    return guessed or "text/csv"


def _compact_dict(data: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in data.items() if value is not None}


def _coerce_upload_id(upload_id: str | UUID) -> str:
    return str(UUID(str(upload_id)))


def _put_presigned_upload(
    *,
    upload_url: str,
    headers: dict[str, str],
    file_path: Path,
) -> None:
    clean_headers = {
        str(key): str(value)
        for key, value in headers.items()
        if str(key).lower() not in FORBIDDEN_PRESIGNED_HEADERS
    }
    clean_headers.setdefault("Content-Length", str(file_path.stat().st_size))
    timeout = httpx.Timeout(
        PRESIGNED_UPLOAD_TIMEOUT_SECONDS,
        connect=30.0,
        read=60.0,
        write=PRESIGNED_UPLOAD_TIMEOUT_SECONDS,
    )
    last_error: httpx.TransportError | None = None
    for attempt in range(PRESIGNED_UPLOAD_MAX_RETRIES + 1):
        try:
            with file_path.open("rb") as payload, httpx.Client(
                timeout=timeout,
                trust_env=False,
            ) as client:
                response = client.put(
                    upload_url,
                    headers=clean_headers,
                    content=payload,
                )
        except httpx.TransportError as exc:
            last_error = exc
            if attempt >= PRESIGNED_UPLOAD_MAX_RETRIES:
                raise RoeAPIException(f"presigned upload failed: {exc}") from exc
            time.sleep(2**attempt)
            continue
        if (
            response.status_code in PRESIGNED_UPLOAD_RETRY_STATUSES
            and attempt < PRESIGNED_UPLOAD_MAX_RETRIES
        ):
            time.sleep(2**attempt)
            continue
        translate_response(response)
        return
    if last_error is not None:
        raise RoeAPIException(f"presigned upload failed: {last_error}") from last_error
