"""Tables API — helpers for uploading Roe tables."""

from __future__ import annotations

from io import BytesIO
import mimetypes
from pathlib import Path
from typing import BinaryIO
from uuid import UUID

from roe._generated.api.tables import upload_table
from roe._generated.client import AuthenticatedClient
from roe._generated.models.table_upload_request import TableUploadRequest
from roe._generated.models.table_upload_response import TableUploadResponse
from roe._generated.types import UNSET, File, Unset
from roe.config import RoeConfig
from roe.exceptions import translate_response
from roe.models import FileUpload


class TablesAPI:
    """API for uploading CSV files into Roe tables."""

    def __init__(self, config: RoeConfig, raw_client: AuthenticatedClient):
        self.config = config
        self._raw = raw_client

    def upload(
        self,
        *,
        table_name: str,
        file: str | Path | bytes | BinaryIO | FileUpload,
        with_headers: bool = True,
        organization_id: str | UUID | None = None,
        filename: str | None = None,
        mime_type: str | None = None,
    ) -> TableUploadResponse:
        """Upload a CSV file and create a Roe table.

        Args:
            table_name: Name of the table to create.
            file: CSV file path, bytes, binary file object, or ``FileUpload``.
            with_headers: Whether the first CSV row contains column headers.
            organization_id: Optional override; defaults to the client's configured org.
            filename: Filename to use for bytes/file objects.
            mime_type: MIME type override. Defaults to ``text/csv`` for ``.csv`` names.
        """

        # Coerce to UUID once; pass UNSET (not None) when no org id is
        # available so the generated multipart serializer omits the form
        # field cleanly. Sending a literal "None" would hit the backend
        # UUID validator and return 400.
        resolved_org: UUID | Unset
        candidate = organization_id or self.config.organization_id
        resolved_org = UUID(str(candidate)) if candidate else UNSET

        upload_file, close_after = self._as_generated_file(file, filename, mime_type)
        try:
            body = TableUploadRequest(
                table_name=table_name,
                file=upload_file,
                with_headers=with_headers,
                organization_id=resolved_org,
            )
            resp = upload_table.sync_detailed(client=self._raw, body=body)
            translate_response(resp)
            return resp.parsed  # type: ignore[return-value]
        finally:
            if close_after:
                upload_file.payload.close()

    @staticmethod
    def _as_generated_file(
        file: str | Path | bytes | BinaryIO | FileUpload,
        filename: str | None,
        mime_type: str | None,
    ) -> tuple[File, bool]:
        if isinstance(file, FileUpload):
            payload = file.open()
            effective_filename = filename or file.effective_filename
            effective_mime_type = mime_type or file.effective_mime_type
            return (
                File(
                    payload=payload,
                    file_name=effective_filename,
                    mime_type=effective_mime_type,
                ),
                file.path is not None,
            )

        if isinstance(file, (str, Path)):
            path = Path(file)
            payload = path.open("rb")
            effective_filename = filename or path.name
            return (
                File(
                    payload=payload,
                    file_name=effective_filename,
                    mime_type=_mime_type(effective_filename, mime_type),
                ),
                True,
            )

        if isinstance(file, bytes):
            effective_filename = filename or "upload.csv"
            return (
                File(
                    payload=BytesIO(file),
                    file_name=effective_filename,
                    mime_type=_mime_type(effective_filename, mime_type),
                ),
                True,
            )

        effective_filename = filename or Path(getattr(file, "name", "upload.csv")).name
        return (
            File(
                payload=file,
                file_name=effective_filename,
                mime_type=_mime_type(effective_filename, mime_type),
            ),
            False,
        )


def _mime_type(filename: str, override: str | None) -> str:
    if override:
        return override
    guessed, _ = mimetypes.guess_type(filename)
    return guessed or "text/csv"
