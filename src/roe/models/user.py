"""User-related models."""

from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    """User information model."""

    id: int = Field(..., description="User ID")
    email: str = Field(..., description="User email address")
    first_name: str = Field(default="", description="User first name")
    last_name: str = Field(default="", description="User last name")
