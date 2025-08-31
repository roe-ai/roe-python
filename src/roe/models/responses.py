"""Response models for API endpoints."""

from typing import Any, Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel, Field

T = TypeVar("T")


class JobStatus:
    """Constants for agent job status codes."""

    PENDING = 0
    STARTED = 1
    RETRY = 2
    SUCCESS = 3
    FAILURE = 4
    CANCELLED = 5
    CACHED = 6


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


class AgentJobStatus(BaseModel):
    """Agent job status response model."""

    status: int = Field(
        ...,
        description="Current status code (0=PENDING, 1=STARTED, 2=RETRY, 3=SUCCESS, 4=FAILURE, 5=CANCELLED, 6=CACHED)",
    )
    timestamp: float = Field(..., description="Unix timestamp in seconds")
    error_message: str | None = Field(
        default=None, description="Error message if status is RETRY or FAILURE"
    )


class AgentJobResult(BaseModel):
    """Agent job result response model."""

    agent_id: UUID = Field(..., description="The ID of the base agent")
    agent_version_id: UUID = Field(..., description="The ID of the agent version")
    inputs: list[Any] = Field(..., description="The input data provided to the agent")
    input_tokens: int | None = Field(..., description="Number of input tokens used")
    output_tokens: int | None = Field(
        ..., description="Number of output tokens generated"
    )
    outputs: list[AgentDatum] = Field(..., description="The output data from the agent")


class AgentJobStatusBatch(BaseModel):
    """Agent job status response model for batch operations."""

    id: str = Field(..., description="Agent job ID")
    status: int | None = Field(
        default=None,
        description="Current status code (0=PENDING, 1=STARTED, 2=RETRY, 3=SUCCESS, 4=FAILURE, 5=CANCELLED, 6=CACHED)",
    )
    created_at: Any | None = Field(default=None, description="When the job was created")
    last_updated_at: Any | None = Field(
        default=None, description="When the job was last updated"
    )


class AgentJobResultBatch(BaseModel):
    """Agent job result response model for batch operations."""

    id: str = Field(..., description="Agent job ID")
    status: int | None = Field(
        default=None,
        description="Job status code (0=PENDING, 1=STARTED, 2=RETRY, 3=SUCCESS, 4=FAILURE, 5=CANCELLED, 6=CACHED)",
    )
    result: list[AgentDatum] | Any | None = Field(
        default=None, description="List of job outputs, or error code if job failed"
    )
    corrected_outputs: list[AgentDatum] | None = Field(
        default=None,
        description="List of corrected outputs if any corrections were made",
    )
    agent_id: UUID | None = Field(default=None, description="Base agent ID")
    agent_version_id: UUID | None = Field(default=None, description="Agent version ID")
    cost: float | None = Field(
        default=None, description="Cost of the agent job execution"
    )
    inputs: list[Any] | None = Field(
        default=None, description="The input data provided to the agent"
    )
    input_tokens: int | None = Field(
        default=None, description="Number of input tokens used"
    )
    output_tokens: int | None = Field(
        default=None, description="Number of output tokens generated"
    )
