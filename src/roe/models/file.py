"""File upload helper model."""

import mimetypes
import os
from typing import BinaryIO

from pydantic import BaseModel, Field, model_validator

from roe.exceptions import BadRequestError

# Maximum file size: 2GB (aligned with main-roe backend)
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024


class FileUpload(BaseModel):
    """Helper class for explicit file uploads with metadata."""

    path: str | None = Field(default=None, description="File path to upload")
    file_obj: BinaryIO | None = Field(default=None, description="File object to upload")
    filename: str | None = Field(default=None, description="Override filename")
    mime_type: str | None = Field(
        default=None, description="MIME type (auto-detected if not provided)"
    )

    class Config:
        arbitrary_types_allowed = True

    @model_validator(mode="after")
    def validate_file_source(self):
        """Ensure exactly one of path or file_obj is provided, and validate file size."""
        if not self.path and not self.file_obj:
            raise ValueError("Either 'path' or 'file_obj' must be provided")

        if self.path and self.file_obj:
            raise ValueError("Only one of 'path' or 'file_obj' should be provided")

        # Validate file size if path is provided
        if self.path:
            try:
                file_size = os.path.getsize(self.path)
                if file_size > MAX_FILE_SIZE:
                    size_gb = file_size / (1024 * 1024 * 1024)
                    raise BadRequestError(
                        message=f"File exceeds maximum size of 2GB: {self.path} ({size_gb:.2f}GB)",
                        status_code=400,
                        response=None,
                    )
            except OSError as e:
                raise ValueError(f"Cannot access file: {self.path}") from e

        return self

    @property
    def effective_filename(self) -> str:
        """Get the effective filename for the upload."""
        if self.filename:
            return self.filename

        if self.path:
            return os.path.basename(self.path)

        # For file objects, try to get name attribute or use default
        if self.file_obj and hasattr(self.file_obj, "name"):
            return os.path.basename(self.file_obj.name)

        return "upload"

    @property
    def effective_mime_type(self) -> str:
        """Get the effective MIME type for the upload."""
        if self.mime_type:
            return self.mime_type

        # Try to guess from filename
        filename = self.effective_filename
        guessed_type, _ = mimetypes.guess_type(filename)

        return guessed_type or "application/octet-stream"

    def open(self) -> BinaryIO:
        """Open the file for reading."""
        if self.file_obj:
            return self.file_obj

        if self.path:
            return open(self.path, "rb")

        raise ValueError("No file source available")

    def to_multipart_tuple(self) -> tuple[str, BinaryIO, str]:
        """Convert to tuple format for multipart form data."""
        file_obj = self.open()
        return (self.effective_filename, file_obj, self.effective_mime_type)
