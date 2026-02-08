"""HTTP client wrapper for the Roe AI SDK."""

import io
import random
import time
from typing import Any, BinaryIO

import httpx

from roe.auth import RoeAuth
from roe.config import RoeConfig
from roe.exceptions import get_exception_for_status_code, ServerError
from roe.models.file import FileUpload
from roe.utils.file_detection import is_file_path, is_uuid_string


class ManagedFiles:
    """Context manager for tracking and closing opened file handles.

    Tracks handles opened both by path (via :meth:`add_file`) and by
    :class:`FileUpload` objects (via :meth:`track_file_upload`) so that
    *all* handles are closed on cleanup — even across retries.
    """

    def __init__(self):
        self._files: list[BinaryIO] = []
        self._file_uploads: list[FileUpload] = []

    def add_file(self, path: str) -> BinaryIO:
        """Open a file and track it for cleanup.

        Args:
            path: Path to the file to open.

        Returns:
            Opened file handle.
        """
        f = open(path, "rb")
        self._files.append(f)
        return f

    def track_file_upload(self, upload: FileUpload) -> None:
        """Register a :class:`FileUpload` so its handles are closed on cleanup."""
        self._file_uploads.append(upload)

    def close_all(self) -> None:
        """Close all tracked file handles and FileUpload objects."""
        for f in self._files:
            try:
                f.close()
            except Exception:
                pass  # Best effort cleanup
        self._files.clear()

        for upload in self._file_uploads:
            try:
                upload.close()
            except Exception:
                pass
        self._file_uploads.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_all()


class RoeHTTPClient:
    """HTTP client for making requests to the Roe AI API."""

    # Status codes that trigger retry
    RETRIABLE_STATUS_CODES = {429, 408, 500, 502, 503, 504}

    def __init__(self, config: RoeConfig, auth: RoeAuth):
        """Initialize the HTTP client.

        Args:
            config: Roe configuration.
            auth: Roe authentication handler.
        """
        self.config = config
        self.auth = auth
        self._max_retries = config.max_retries

        # Create httpx client with configuration
        self.client = httpx.Client(
            base_url=config.base_url,
            timeout=config.timeout,
            headers=auth.get_headers(),
        )

    def close(self) -> None:
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # ------------------------------------------------------------------
    # Retry helpers
    # ------------------------------------------------------------------

    def _calculate_backoff(self, attempt: int, response: httpx.Response | None = None) -> float:
        """Calculate backoff delay with jitter, respecting Retry-After on 429.

        Args:
            attempt: Current attempt number (0-indexed).
            response: The HTTP response (used to read ``Retry-After`` on 429).

        Returns:
            Delay in seconds before next retry.
        """
        # Honour Retry-After header when the server sends one (typically 429)
        if response is not None and response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            if retry_after is not None:
                try:
                    return max(float(retry_after), 0.0)
                except (ValueError, TypeError):
                    pass  # Fall through to exponential backoff

        # Exponential backoff: 1s, 2s, 4s, 8s… capped at 10s, plus ±25 % jitter
        base = min(1.0 * (2 ** attempt), 10.0)
        jitter = base * 0.25 * (2 * random.random() - 1)  # ±25 %
        return max(base + jitter, 0.0)

    def _should_retry(self, status_code: int | None, is_network_error: bool) -> bool:
        """Determine if a request should be retried.

        Args:
            status_code: HTTP status code (None for network errors).
            is_network_error: Whether this was a network-level error.

        Returns:
            True if the request should be retried.
        """
        if is_network_error:
            return True
        if status_code is not None and status_code in self.RETRIABLE_STATUS_CODES:
            return True
        return False

    def _request_with_retry(
        self,
        method: str,
        url: str,
        *,
        raw_bytes: bool = False,
        **kwargs: Any,
    ) -> Any:
        """Execute an HTTP request with retry logic (single implementation).

        All public HTTP helpers delegate to this method so that retry
        policy, backoff, and error handling live in exactly one place.

        Args:
            method: HTTP method (``GET``, ``POST``, ``PUT``, ``DELETE``).
            url: Request URL (relative to base URL).
            raw_bytes: If ``True``, return ``response.content`` instead of
                       parsed JSON on success.
            **kwargs: Forwarded to ``httpx.Client.request``.

        Returns:
            Parsed JSON response, raw ``bytes``, or ``None`` (for 204).

        Raises:
            RoeAPIException: For non-retriable API errors.
            ServerError: After exhausting retries on network errors.
        """
        last_exception: Exception | None = None

        for attempt in range(self._max_retries + 1):
            response: httpx.Response | None = None
            try:
                response = self.client.request(method, url, **kwargs)

                # DELETE → 204 is a normal success
                if method == "DELETE" and (response.status_code == 204 or response.is_success):
                    return None

                if not self._should_retry(response.status_code, False) or attempt >= self._max_retries:
                    if raw_bytes:
                        if response.is_success:
                            return response.content
                        # Error path for raw-bytes requests
                        exception_class = get_exception_for_status_code(response.status_code)
                        try:
                            error_data = response.json()
                            message = error_data.get("detail", f"HTTP {response.status_code}")
                            raise exception_class(
                                message=message,
                                status_code=response.status_code,
                                response=error_data,
                            )
                        except (ValueError, KeyError):
                            raise exception_class(
                                message=f"HTTP {response.status_code}: {response.text}",
                                status_code=response.status_code,
                                response=None,
                            )
                    return self._handle_response(response)

            except httpx.RequestError as e:
                last_exception = e
                if attempt >= self._max_retries:
                    raise ServerError(
                        message=f"Request failed after {self._max_retries + 1} attempts: {e}",
                        status_code=None,
                        response=None,
                    ) from e

            # Wait before retry
            if attempt < self._max_retries:
                time.sleep(self._calculate_backoff(attempt, response))

        # Fallback — should rarely be reached
        if last_exception:
            raise last_exception
        raise ServerError(message="Request failed", status_code=None, response=None)

    # ------------------------------------------------------------------
    # Input / response processing
    # ------------------------------------------------------------------

    def _process_inputs(
        self, inputs: dict[str, Any], managed_files: ManagedFiles
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """Process inputs to separate form data and files.

        Args:
            inputs: Dictionary of input values.
            managed_files: ManagedFiles instance to track opened files.

        Returns:
            Tuple of (form_data, files) dictionaries.
        """
        form_data = {}
        files = {}

        for key, value in inputs.items():
            if isinstance(value, FileUpload):
                # Explicit file upload — track for cleanup via ManagedFiles
                managed_files.track_file_upload(value)
                filename, file_obj, mime_type = value.to_multipart_tuple()
                files[key] = (filename, file_obj, mime_type)
            elif isinstance(value, (io.IOBase, io.BytesIO)) or hasattr(value, "read"):
                # File-like object
                files[key] = value
            elif isinstance(value, str):
                if is_uuid_string(value):
                    # Roe file ID reference
                    form_data[key] = value
                elif is_file_path(value):
                    # File path - open and track for cleanup
                    files[key] = managed_files.add_file(value)
                else:
                    # Regular string value
                    form_data[key] = value
            else:
                # Other data types (numbers, booleans, etc.)
                form_data[key] = str(value) if value is not None else ""

        return form_data, files

    def _handle_response(self, response: httpx.Response) -> Any:
        """Handle HTTP response and raise appropriate exceptions.

        Args:
            response: HTTP response object.

        Returns:
            Parsed JSON response.

        Raises:
            RoeAPIException: For API errors.
        """
        if response.is_success:
            return response.json()

        # Get the appropriate exception class for the status code
        exception_class = get_exception_for_status_code(response.status_code)

        try:
            error_data = response.json()
            message = error_data.get("detail", f"HTTP {response.status_code}")

            raise exception_class(
                message=message,
                status_code=response.status_code,
                response=error_data,
            )
        except (ValueError, KeyError):
            # If we can't parse the error response, use the status text
            raise exception_class(
                message=f"HTTP {response.status_code}: {response.text}",
                status_code=response.status_code,
                response=None,
            )

    # ------------------------------------------------------------------
    # Public HTTP methods
    # ------------------------------------------------------------------

    def get(self, url: str, params: dict[str, Any] | None = None) -> Any:
        """Make a GET request with retry logic.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        return self._request_with_retry("GET", url, params=params)

    def post(
        self,
        url: str,
        json_data: dict[str, Any] | list[Any] | None = None,
        form_data: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Make a POST request with retry logic.

        Args:
            url: Request URL (relative to base URL).
            json_data: JSON data to send.
            form_data: Form data to send.
            files: Files to upload.
            params: Query parameters.

        Returns:
            Parsed JSON response.

        Note:
            File uploads with retries require files to be seekable (file paths or BytesIO).
            Raw streams cannot be retried safely.
        """
        # Build kwargs — only set keys that are not None.
        kwargs: dict[str, Any] = {}

        if json_data is not None:
            kwargs["json"] = json_data
        elif form_data is not None or files is not None:
            kwargs["data"] = form_data or {}
            if files:
                # Seek every file handle to the start so retries work.
                rebuilt_files = {}
                for key, file_value in files.items():
                    if hasattr(file_value, "seek"):
                        file_value.seek(0)
                        rebuilt_files[key] = file_value
                    elif isinstance(file_value, tuple) and len(file_value) >= 2:
                        file_obj = file_value[1]
                        if hasattr(file_obj, "seek"):
                            file_obj.seek(0)
                        rebuilt_files[key] = file_value
                    else:
                        rebuilt_files[key] = file_value
                kwargs["files"] = rebuilt_files
            else:
                kwargs["files"] = {}

        if params:
            kwargs["params"] = params

        return self._request_with_retry("POST", url, **kwargs)

    def post_with_dynamic_inputs(
        self,
        url: str,
        inputs: dict[str, Any],
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Make a POST request with dynamic inputs (handles files automatically).

        Files opened during processing are automatically closed after the request.

        Args:
            url: Request URL (relative to base URL).
            inputs: Dynamic input values.
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        # Use ManagedFiles to track and close opened file handles
        with ManagedFiles() as managed_files:
            form_data, files = self._process_inputs(inputs, managed_files)

            return self.post(
                url=url,
                form_data=form_data,
                files=files,
                params=params,
            )

    def put(
        self,
        url: str,
        json_data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Make a PUT request with retry logic.

        Args:
            url: Request URL (relative to base URL).
            json_data: JSON data to send.
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        kwargs: dict[str, Any] = {}
        if json_data is not None:
            kwargs["json"] = json_data
        if params:
            kwargs["params"] = params

        return self._request_with_retry("PUT", url, **kwargs)

    def delete(self, url: str, params: dict[str, Any] | None = None) -> None:
        """Make a DELETE request with retry logic.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            None on success (204 response).

        Raises:
            RoeAPIException: For API errors.
        """
        self._request_with_retry("DELETE", url, params=params)

    def get_bytes(self, url: str, params: dict[str, Any] | None = None) -> bytes:
        """Make a GET request and return raw bytes with retry logic.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            Raw bytes from response.

        Raises:
            RoeAPIException: For API errors.
        """
        return self._request_with_retry("GET", url, raw_bytes=True, params=params)
