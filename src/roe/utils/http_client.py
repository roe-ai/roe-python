"""HTTP client wrapper for the Roe AI SDK."""

import io
import time
from typing import Any, BinaryIO

import httpx

from roe.auth import RoeAuth
from roe.config import RoeConfig
from roe.exceptions import get_exception_for_status_code, ServerError
from roe.models.file import FileUpload
from roe.utils.file_detection import is_file_path, is_uuid_string


class ManagedFiles:
    """Context manager for tracking and closing opened file handles."""

    def __init__(self):
        self._files: list[BinaryIO] = []

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

    def close_all(self) -> None:
        """Close all tracked file handles."""
        for f in self._files:
            try:
                f.close()
            except Exception:
                pass  # Best effort cleanup
        self._files.clear()

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

    def _calculate_backoff(self, attempt: int) -> float:
        """Calculate exponential backoff delay.

        Args:
            attempt: Current attempt number (0-indexed).

        Returns:
            Delay in seconds before next retry.
        """
        # Exponential backoff: 1s, 2s, 4s, 8s... capped at 10s
        return min(1.0 * (2 ** attempt), 10.0)

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
                # Explicit file upload
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

    def get(self, url: str, params: dict[str, Any] | None = None) -> Any:
        """Make a GET request with retry logic.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        last_exception: Exception | None = None

        for attempt in range(self._max_retries + 1):
            try:
                response = self.client.get(url, params=params)
                if not self._should_retry(response.status_code, False) or attempt >= self._max_retries:
                    return self._handle_response(response)
            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_exception = e
                if attempt >= self._max_retries:
                    raise ServerError(
                        message=f"Request failed after {self._max_retries + 1} attempts: {str(e)}",
                        status_code=None,
                        response=None,
                    ) from e

            # Wait before retry
            if attempt < self._max_retries:
                time.sleep(self._calculate_backoff(attempt))

        if last_exception:
            raise last_exception
        raise ServerError(message="Request failed", status_code=None, response=None)

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
        """
        kwargs: dict[str, Any] = {}

        if json_data:
            kwargs["json"] = json_data
        elif form_data or files:
            kwargs["data"] = form_data or {}
            kwargs["files"] = files or {}

        if params:
            kwargs["params"] = params

        last_exception: Exception | None = None

        for attempt in range(self._max_retries + 1):
            try:
                response = self.client.post(url, **kwargs)
                if not self._should_retry(response.status_code, False) or attempt >= self._max_retries:
                    return self._handle_response(response)
            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_exception = e
                if attempt >= self._max_retries:
                    raise ServerError(
                        message=f"Request failed after {self._max_retries + 1} attempts: {str(e)}",
                        status_code=None,
                        response=None,
                    ) from e

            # Wait before retry
            if attempt < self._max_retries:
                time.sleep(self._calculate_backoff(attempt))

        if last_exception:
            raise last_exception
        raise ServerError(message="Request failed", status_code=None, response=None)

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
        if json_data:
            kwargs["json"] = json_data
        if params:
            kwargs["params"] = params

        last_exception: Exception | None = None

        for attempt in range(self._max_retries + 1):
            try:
                response = self.client.put(url, **kwargs)
                if not self._should_retry(response.status_code, False) or attempt >= self._max_retries:
                    return self._handle_response(response)
            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_exception = e
                if attempt >= self._max_retries:
                    raise ServerError(
                        message=f"Request failed after {self._max_retries + 1} attempts: {str(e)}",
                        status_code=None,
                        response=None,
                    ) from e

            # Wait before retry
            if attempt < self._max_retries:
                time.sleep(self._calculate_backoff(attempt))

        if last_exception:
            raise last_exception
        raise ServerError(message="Request failed", status_code=None, response=None)

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
        last_exception: Exception | None = None

        for attempt in range(self._max_retries + 1):
            try:
                response = self.client.delete(url, params=params)
                if response.status_code == 204 or response.is_success:
                    return None
                if not self._should_retry(response.status_code, False) or attempt >= self._max_retries:
                    # Handle error
                    self._handle_response(response)
            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_exception = e
                if attempt >= self._max_retries:
                    raise ServerError(
                        message=f"Request failed after {self._max_retries + 1} attempts: {str(e)}",
                        status_code=None,
                        response=None,
                    ) from e

            # Wait before retry
            if attempt < self._max_retries:
                time.sleep(self._calculate_backoff(attempt))

        if last_exception:
            raise last_exception

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
        last_exception: Exception | None = None

        for attempt in range(self._max_retries + 1):
            try:
                response = self.client.get(url, params=params)
                if response.is_success:
                    return response.content

                if not self._should_retry(response.status_code, False) or attempt >= self._max_retries:
                    # Handle error using standard handler
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
            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_exception = e
                if attempt >= self._max_retries:
                    raise ServerError(
                        message=f"Request failed after {self._max_retries + 1} attempts: {str(e)}",
                        status_code=None,
                        response=None,
                    ) from e

            # Wait before retry
            if attempt < self._max_retries:
                time.sleep(self._calculate_backoff(attempt))

        if last_exception:
            raise last_exception
        raise ServerError(message="Request failed", status_code=None, response=None)
