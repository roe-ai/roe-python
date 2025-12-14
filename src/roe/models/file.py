"""File upload helper model."""

import mimetypes
import os
from typing import BinaryIO

from pydantic import BaseModel, Field, model_validator

from roe.exceptions import BadRequestError

# Maximum file size: 2GB (aligned with main-roe backend)
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024


class FileUpload(BaseModel):
    """Helper class for explicit file uploads with metadata.

    Supports context manager protocol for automatic file cleanup:

        with FileUpload(path="file.pdf") as upload:
            filename, file_obj, mime_type = upload.to_multipart_tuple()
            # file_obj is automatically closed when exiting the context

    Or manually close opened files:

        upload = FileUpload(path="file.pdf")
        file_obj = upload.open()
        try:
            # use file_obj
        finally:
            upload.close()
    """

    path: str | None = Field(default=None, description="File path to upload")
    file_obj: BinaryIO | None = Field(default=None, description="File object to upload")
    filename: str | None = Field(default=None, description="Override filename")
    mime_type: str | None = Field(
        default=None, description="MIME type (auto-detected if not provided)"
    )

    # Track opened files for cleanup (not part of pydantic model)
    _opened_files: list[BinaryIO] = []

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        # Initialize tracking list for opened files
        object.__setattr__(self, "_opened_files", [])

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
        """Open the file for reading.

        Note: If opening from path, the file handle is tracked and can be
        closed by calling close() or using the context manager.
        """
        if self.file_obj:
            return self.file_obj

        if self.path:
            f = open(self.path, "rb")
            self._opened_files.append(f)
            return f

        raise ValueError("No file source available")

    def close(self) -> None:
        """Close all file handles opened by this FileUpload."""
        for f in self._opened_files:
            try:
                f.close()
            except Exception:
                pass  # Best effort cleanup
        self._opened_files.clear()

    def __enter__(self) -> "FileUpload":
        """Enter context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager, closing any opened files."""
        self.close()

    def to_multipart_tuple(self) -> tuple[str, BinaryIO, str]:
        """Convert to tuple format for multipart form data.

        Note: The returned file object should be closed after use,
        either by calling close() or using the context manager.
        """
        file_obj = self.open()
        return (self.effective_filename, file_obj, self.effective_mime_type)
