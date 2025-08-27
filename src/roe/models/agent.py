"""Agent-related models."""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from roe.api.agents import AgentsAPI
from roe.models.responses import AgentDatum
from roe.models.user import UserInfo


class AgentInputDefinition(BaseModel):
    """Definition of an agent input parameter."""

    key: str = Field(..., description="The unique identifier for this input definition")
    data_type: str = Field(
        ..., description="The data type of the input (e.g., text, file, etc.)"
    )
    description: str = Field(..., description="Description of what this input is for")
    example: str = Field(default="", description="An example value for this input")
    accepts_multiple_files: bool = Field(
        default=False, description="Whether this input accepts multiple files"
    )


class BaseAgent(BaseModel):
    """Base agent configuration model."""

    id: UUID = Field(..., description="Agent UUID")
    name: str = Field(..., description="Agent name")
    creator: "UserInfo | None" = Field(default=None, description="Agent creator")
    created_at: datetime = Field(..., description="Creation timestamp")
    disable_cache: bool = Field(
        ..., description="Whether to disable job cache fetching"
    )
    cache_failed_jobs: bool = Field(..., description="Whether to cache failed jobs")
    organization_id: UUID = Field(..., description="Organization ID that owns this agent")
    engine_class_id: str = Field(..., description="Engine class identifier")
    current_version_id: UUID | None = Field(
        default=None, description="UUID of current agent version"
    )
    job_count: int = Field(..., description="Total number of jobs run")
    most_recent_job: datetime | None = Field(
        default=None, description="Most recent job timestamp"
    )
    engine_name: str = Field(..., description="Engine display name")

    # Reference to the agents API for running
    _agents_api: "AgentsAPI | None" = None

    class Config:
        from_attributes = True

    def set_agents_api(self, agents_api: "AgentsAPI") -> None:
        """Set the agents API reference for running."""
        self._agents_api = agents_api

    def run(self, **inputs) -> list["AgentDatum"]:
        """Run the agent with the provided inputs.

        Uses the agent's current version for execution.

        Args:
            **inputs: Dynamic inputs based on agent configuration.

        Returns:
            List of AgentDatum results.

        Raises:
            ValueError: If agents API is not set.
        """
        if not self._agents_api:
            raise ValueError("Agents API not set. Use client.agents.run() instead.")

        return self._agents_api.run(agent_id=str(self.id), **inputs)

    def run_async(self, **inputs) -> str:
        """Run the agent asynchronously and return job ID.

        Uses the agent's current version for execution.

        Args:
            **inputs: Dynamic inputs based on agent configuration.

        Returns:
            Agent job ID string.

        Raises:
            ValueError: If agents API is not set.
        """
        if not self._agents_api:
            raise ValueError("Agents API not set. Use client.agents.run_async() instead.")

        return self._agents_api.run_async(agent_id=str(self.id), **inputs)

    def list_versions(self) -> list["AgentVersion"]:
        """List all versions of this base agent.

        Returns:
            List of AgentVersion objects.

        Raises:
            ValueError: If agents API is not set.
        """
        if not self._agents_api:
            raise ValueError(
                "Agents API not set. Use client.agents.list_versions() instead."
            )

        return self._agents_api.list_versions(str(self.id))

    def get_current_version(self) -> "AgentVersion | None":
        """Get the current version of this agent.

        Returns:
            AgentVersion object or None if no current version.

        Raises:
            ValueError: If agents API is not set.
        """
        if not self._agents_api:
            raise ValueError(
                "Agents API not set. Use client.agents.get_current_version() instead."
            )

        if not self.current_version_id:
            return None

        return self._agents_api.get_version(str(self.id), str(self.current_version_id))


class AgentVersion(BaseModel):
    """Agent version model with input definitions and engine config."""

    id: UUID = Field(..., description="Agent version UUID")
    name: str = Field(..., description="Agent name (from base agent)")
    version_name: str = Field(..., description="Version name for the agent version")
    creator: "UserInfo | None" = Field(default=None, description="Version creator")
    created_at: datetime = Field(..., description="Creation timestamp")
    description: str | None = Field(
        default=None, description="Description of the agent version"
    )
    engine_class_id: str = Field(
        ..., description="Engine class identifier (from base agent)"
    )
    engine_name: str = Field(..., description="Engine display name")
    input_definitions: list[AgentInputDefinition] = Field(
        ..., description="List of input definitions for this version"
    )
    engine_config: dict[str, str] = Field(..., description="Engine configuration")
    organization_id: UUID = Field(..., description="Organization ID (from base agent)")
    readonly: bool = Field(..., description="Whether this version is readonly")
    base_agent: "BaseAgent" = Field(
        ..., description="The base agent this version belongs to"
    )

    # Reference to the agents API for running
    _agents_api: "AgentsAPI | None" = None

    class Config:
        from_attributes = True

    def set_agents_api(self, agents_api: "AgentsAPI") -> None:
        """Set the agents API reference for running."""
        self._agents_api = agents_api

    def run(self, **inputs) -> list["AgentDatum"]:
        """Run this specific version of the agent.

        Args:
            **inputs: Dynamic inputs based on this version's input definitions.

        Returns:
            List of AgentDatum results.

        Raises:
            ValueError: If agents API is not set.
        """
        if not self._agents_api:
            raise ValueError("Agents API not set. Use client.agents.run() instead.")

        # Run using the version ID directly
        return self._agents_api.run(agent_id=str(self.id), **inputs)

    def run_async(self, **inputs) -> str:
        """Run this specific version of the agent asynchronously and return job ID.

        Args:
            **inputs: Dynamic inputs based on this version's input definitions.

        Returns:
            Agent job ID string.

        Raises:
            ValueError: If agents API is not set.
        """
        if not self._agents_api:
            raise ValueError("Agents API not set. Use client.agents.run_async() instead.")

        # Run using the version ID directly
        return self._agents_api.run_async(agent_id=str(self.id), **inputs)
