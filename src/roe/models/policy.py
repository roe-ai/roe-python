"""Policy-related models."""

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class Policy(BaseModel):
    """Policy model representing a set of rules/SOPs for agentic workflows."""

    id: UUID = Field(..., description="Policy UUID")
    name: str = Field(..., description="Policy name")
    description: str = Field(default="", description="Policy description")
    organization_id: UUID = Field(
        ..., description="Organization ID that owns this policy"
    )
    current_version_id: UUID | None = Field(
        default=None, description="UUID of the current active version"
    )
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

    class Config:
        from_attributes = True


class PolicyVersion(BaseModel):
    """Policy version model containing the actual policy content."""

    id: UUID = Field(..., description="Policy version UUID")
    version_name: str = Field(..., description="Version name")
    content: dict[str, Any] = Field(
        ..., description="Policy content (guidelines, instructions, dispositions)"
    )
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    policy: Policy | None = Field(
        default=None, description="Parent policy (included in list/retrieve responses)"
    )
    created_by: dict[str, Any] | None = Field(
        default=None, description="User who created this version"
    )
    base_version_id: UUID | None = Field(
        default=None, description="ID of the version this was derived from"
    )

    class Config:
        from_attributes = True
