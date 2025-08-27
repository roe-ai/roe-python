"""HTTP client wrapper for the Roe AI SDK."""

import io
from typing import Any

import httpx

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
        """Make a GET request.

        Args:
            url: Request URL (relative to base URL).
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        response = self.client.get(url, params=params)
        return self._handle_response(response)

    def post(
        self,
        url: str,
        json_data: dict[str, Any] | None = None,
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

        response = self.client.post(url, **kwargs)
        return self._handle_response(response)

    def post_with_dynamic_inputs(
        self,
        url: str,
        inputs: dict[str, Any],
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Make a POST request with dynamic inputs (handles files automatically).

        Args:
            url: Request URL (relative to base URL).
            inputs: Dynamic input values.
            params: Query parameters.

        Returns:
            Parsed JSON response.
        """
        form_data, files = self._process_inputs(inputs)

        return self.post(
            url=url,
            form_data=form_data,
            files=files,
            params=params,
        )
