"""HTTP client wrapper for the Roe AI SDK."""

import io
import json as _json
import logging
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)

from roe.auth import RoeAuth
from roe.config import RoeConfig
from roe.exceptions import get_exception_for_status_code
from roe.models.file import FileUpload
from roe.utils.file_detection import is_file_path, is_uuid_string


class RoeHTTPClient:
    """HTTP client for making requests to the Roe AI API."""

    def __init__(self, config: RoeConfig, auth: RoeAuth):
        """Initialize the HTTP client.

        Args:
            config: Roe configuration.
            auth: Roe authentication handler.
        """
        self.config = config
        self.auth = auth

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

    def _process_inputs(
        self, inputs: dict[str, Any]
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """Process inputs to separate form data and files.

        Args:
            inputs: Dictionary of input values.

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
                    # File path - read and upload
                    files[key] = open(value, "rb")
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
            if response.status_code == 204 or not response.content:
                return None
            return response.json()

        # Get the appropriate exception class for the status code
        exception_class = get_exception_for_status_code(response.status_code)

        try:
            error_data = response.json()
            if isinstance(error_data, dict):
                message = error_data.get("detail", f"HTTP {response.status_code}")
            elif isinstance(error_data, list):
                # DRF returns a plain list when ValidationError is raised in a view
                # e.g. ["Worksheet query has been cancelled and cannot be executed"]
                message = "; ".join(str(e) for e in error_data) if error_data else f"HTTP {response.status_code}"
                error_data = None
            else:
                message = str(error_data) if error_data is not None else f"HTTP {response.status_code}"
                error_data = None
        except (ValueError, KeyError, AttributeError):
            message = f"HTTP {response.status_code}: {response.text}"
            error_data = None

        raise exception_class(
            message=message,
            status_code=response.status_code,
            response=error_data,
        )

    _RETRYABLE_STATUS_CODES = {502, 503, 504}
    _IDEMPOTENT_METHODS = {"get", "put", "delete"}

    def _request_with_retry(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Execute an HTTP request with retries for 502/503/504 errors.

        Only idempotent methods (GET, PUT, DELETE) are retried. POST requests
        are never retried to avoid duplicate submissions and file-handle
        exhaustion on multipart uploads.

        Uses exponential backoff: 1s, 2s, 4s, ...
        Retries up to config.max_retries times (default: 3).
        """
        response = getattr(self.client, method)(url, **kwargs)

        if method not in self._IDEMPOTENT_METHODS:
            return response

        if response.status_code not in self._RETRYABLE_STATUS_CODES:
            return response

        max_retries = self.config.max_retries
        last_response = response

        for attempt in range(max_retries):
            wait_time = 2 ** attempt  # 1, 2, 4, ...
            logger.warning(
                "Roe API returned %d for %s %s, retrying in %ds (attempt %d/%d)",
                last_response.status_code,
                method.upper(),
                url,
                wait_time,
                attempt + 1,
                max_retries,
            )
            time.sleep(wait_time)

            response = getattr(self.client, method)(url, **kwargs)

            if response.status_code not in self._RETRYABLE_STATUS_CODES:
                return response

            last_response = response

        # All retries exhausted — let _handle_response raise the exception
        return last_response

    def get(self, url: str, params: dict[str, Any] | None = None) -> Any:
        """Make a GET request.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        response = self._request_with_retry("get", url, params=params)
        return self._handle_response(response)

    def post(
        self,
        url: str,
        json_data: dict[str, Any] | list[Any] | None = None,
        form_data: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Make a POST request.

        Args:
            url: Request URL (relative to base URL).
            json_data: JSON data to send.
            form_data: Form data to send.
            files: Files to upload.
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        kwargs = {}

        if json_data:
            kwargs["json"] = json_data
        elif form_data or files:
            kwargs["data"] = form_data or {}
            kwargs["files"] = files or {}

        if params:
            kwargs["params"] = params

        response = self._request_with_retry("post", url, **kwargs)
        return self._handle_response(response)

    def post_with_dynamic_inputs(
        self,
        url: str,
        inputs: dict[str, Any],
        metadata: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Make a POST request with dynamic inputs (handles files automatically).

        Args:
            url: Request URL (relative to base URL).
            inputs: Dynamic input values.
            metadata: Optional metadata dictionary to attach to the job.
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        form_data, files = self._process_inputs(inputs)

        if metadata is not None:
            form_data["metadata"] = _json.dumps(metadata)

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
        """Make a PUT request.

        Args:
            url: Request URL (relative to base URL).
            json_data: JSON data to send.
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        kwargs = {}
        if json_data:
            kwargs["json"] = json_data
        if params:
            kwargs["params"] = params

        response = self._request_with_retry("put", url, **kwargs)
        return self._handle_response(response)

    def delete(self, url: str, params: dict[str, Any] | None = None) -> None:
        """Make a DELETE request.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            None on success (204 response).

        Raises:
            RoeAPIException: For API errors.
        """
        response = self._request_with_retry("delete", url, params=params)
        if response.status_code == 204:
            return None
        if response.is_success:
            return None
        # Handle error
        self._handle_response(response)

    def get_bytes(self, url: str, params: dict[str, Any] | None = None) -> bytes:
        """Make a GET request and return raw bytes.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            Raw bytes from response.

        Raises:
            RoeAPIException: For API errors.
        """
        response = self._request_with_retry("get", url, params=params)
        if response.is_success:
            return response.content

        # Reuse shared error handler — it always raises, never returns
        self._handle_response(response)
