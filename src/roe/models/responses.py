"""Response models for API endpoints."""

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ErrorResponse(BaseModel):
    """Error response model."""

    detail: str = Field(..., description="Error message")
    status_code: int = Field(..., description="HTTP status code")


class AgentDatum(BaseModel):
    """Agent execution result data."""

    key: str = Field(..., description="The key of the output")
    description: str = Field(..., description="The description of the output")
    data_type: str = Field(..., description="The MIME data type of the output")
    value: str = Field(
        ..., description="The value of the output, serialized as a string"
    )
    cost: float | None = Field(
        default=None, description="The cost of the agent job execution"
    )


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response model."""

    count: int = Field(..., description="Total number of items")
    next: str | None = Field(default=None, description="URL to next page")
    previous: str | None = Field(default=None, description="URL to previous page")
    results: list[T] = Field(..., description="List of results")

    @property
    def has_next(self) -> bool:
        """Check if there's a next page."""
        return self.next is not None

    @property
    def has_previous(self) -> bool:
        """Check if there's a previous page."""
        return self.previous is not None
