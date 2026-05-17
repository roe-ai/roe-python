"""Custom exceptions for the Roe AI SDK."""

from __future__ import annotations

import json as _json
from collections.abc import Mapping
from http import HTTPStatus
from typing import Any


class RoeAPIException(Exception):
    """Base exception for all Roe AI API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response: dict[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response
        self.headers = dict(headers) if headers is not None else None


class BadRequestError(RoeAPIException):
    """400 Bad Request - Invalid input data."""

    pass


class AuthenticationError(RoeAPIException):
    """401 Unauthorized - Invalid or missing API key."""

    pass


class InsufficientCreditsError(RoeAPIException):
    """402 Payment Required - Insufficient credits."""

    pass


class ForbiddenError(RoeAPIException):
    """403 Forbidden - Access denied or organization access forbidden."""

    pass


class NotFoundError(RoeAPIException):
    """404 Not Found - Resource not found."""

    pass


class ServerError(RoeAPIException):
    """500+ Server Error - Internal server errors."""

    pass


def get_exception_for_status_code(status_code: int) -> type[RoeAPIException]:
    """Get the appropriate exception class for an HTTP status code."""
    exception_map = {
        400: BadRequestError,
        401: AuthenticationError,
        402: InsufficientCreditsError,
        403: ForbiddenError,
        404: NotFoundError,
    }

    if status_code in exception_map:
        return exception_map[status_code]
    elif status_code >= 500:
        return ServerError
    else:
        return RoeAPIException


def translate_response(response: Any) -> None:
    """Raise the appropriate ``RoeAPIException`` for a non-2xx response.

    Accepts either an ``httpx.Response`` or a generated
    ``roe._generated.types.Response`` — both expose ``status_code`` and
    ``content``. No-op on 2xx.
    """
    raw_status = getattr(response, "status_code", None)
    status_code = int(raw_status) if isinstance(raw_status, HTTPStatus) else raw_status
    if status_code is None or 200 <= status_code < 300:
        return

    content = getattr(response, "content", None)
    if isinstance(content, (bytes, bytearray)):
        try:
            content_str = bytes(content).decode("utf-8", errors="replace")
        except Exception:
            content_str = ""
    else:
        content_str = content or ""

    error_data: dict[str, Any] | None = None
    try:
        body = _json.loads(content_str) if content_str else None
    except (ValueError, TypeError):
        body = None

    if isinstance(body, dict):
        message = body.get("detail") or body.get("error") or body.get("message")
        if not message:
            for value in body.values():
                if isinstance(value, list) and value:
                    message = "; ".join(str(e) for e in value)
                    break
                if isinstance(value, str) and value:
                    message = value
                    break
        if not message:
            message = f"HTTP {status_code}"
        error_data = body
    elif isinstance(body, list):
        # DRF returns a plain list when ValidationError is raised in a view
        # e.g. ["Worksheet query has been cancelled and cannot be executed"]
        message = "; ".join(str(e) for e in body) if body else f"HTTP {status_code}"
    else:
        snippet = content_str[:200] if content_str else ""
        message = f"HTTP {status_code}: {snippet}" if snippet else f"HTTP {status_code}"

    raw_headers = getattr(response, "headers", None)
    cls = get_exception_for_status_code(status_code)
    raise cls(message=message, status_code=status_code, response=error_data, headers=raw_headers)
