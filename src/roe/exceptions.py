"""Custom exceptions for the Roe AI SDK."""

from typing import Any


class RoeAPIException(Exception):
    """Base exception for all Roe AI API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response: dict[str, Any] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response


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
