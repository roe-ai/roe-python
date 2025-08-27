"""Agents API implementation."""

from typing import Any

from roe.config import RoeConfig
from roe.exceptions import NotFoundError
from roe.models.agent import AgentVersion, BaseAgent
from roe.models.responses import AgentDatum, PaginatedResponse
from roe.utils.http_client import RoeHTTPClient
from roe.utils.pagination import PaginationHelper


class AgentsAPI:
    """API for managing and running agents."""

    def __init__(self, config: RoeConfig, http_client: RoeHTTPClient):
        """Initialize the agents API.

        Args:
            config: Roe configuration.
            http_client: HTTP client instance.
        """
        self.config = config
        self.http_client = http_client

    def list_base_agents(
        self,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedResponse[BaseAgent]:
        """List base agents in the organization.

        Args:
            page: Page number (1-based).
            page_size: Number of results per page.

        Returns:
            Paginated list of base agents.
        """
        # Build query parameters with organization_id
        params = PaginationHelper.build_query_params(
            organization_id=self.config.organization_id,
            page=page,
            page_size=page_size,
        )

        # Make the request
        response_data = self.http_client.get("/v1/agents/", params=params)

        # Parse the response
        base_agents = [
            BaseAgent(**agent_data) for agent_data in response_data["results"]
        ]

        # Set the agents API reference for each agent (for .run() method)
        for agent in base_agents:
            agent.set_agents_api(self)

        return PaginatedResponse[BaseAgent](
            count=response_data["count"],
            next=response_data.get("next"),
            previous=response_data.get("previous"),
            results=base_agents,
        )

    def get_base_agent(self, agent_id: str) -> BaseAgent:
        """Get a specific base agent by ID.

        Args:
            agent_id: Base agent UUID.

        Returns:
            BaseAgent instance.
        """
        # Build query parameters
        params = {"organization_id": self.config.organization_id}

        # Make the request to the dedicated GET endpoint
        response_data = self.http_client.get(f"/v1/agents/{agent_id}/", params=params)

        # Parse the response
        base_agent = BaseAgent(**response_data)

        # Set the agents API reference for the agent (for .run() method)
        base_agent.set_agents_api(self)

        return base_agent

    def list_versions(self, base_agent_id: str) -> list[AgentVersion]:
        """List all versions of a base agent.

        Args:
            base_agent_id: Base agent UUID.

        Returns:
            List of agent versions.
        """
        # Build query parameters
        params = {"organization_id": self.config.organization_id}

        # Make the request
        response_data = self.http_client.get(
            f"/v1/agents/{base_agent_id}/versions/", params=params
        )

        # Parse the response
        versions = [AgentVersion(**version_data) for version_data in response_data]

        # Set the agents API reference for each version
        for version in versions:
            version.set_agents_api(self)

        return versions

    def get_version(self, base_agent_id: str, version_id: str) -> AgentVersion:
        """Get a specific version of a base agent.

        Args:
            base_agent_id: Base agent UUID.
            version_id: Version UUID.

        Returns:
            AgentVersion instance.
        """
        # List all versions and find the one we want
        versions = self.list_versions(base_agent_id)

        for version in versions:
            if str(version.id) == version_id:
                return version

        raise NotFoundError(f"Version {version_id} not found for agent {base_agent_id}")

    def get_current_version(self, base_agent_id: str) -> AgentVersion:
        """Get the current version of a base agent.

        Args:
            base_agent_id: Base agent UUID.

        Returns:
            Current AgentVersion.
        """
        # Build query parameters
        params = {"organization_id": self.config.organization_id}

        # Make the request to the dedicated current version endpoint
        response_data = self.http_client.get(
            f"/v1/agents/{base_agent_id}/versions/current/", params=params
        )

        # Parse the response
        version = AgentVersion(**response_data)

        # Set the agents API reference for the version
        version.set_agents_api(self)

        return version

    def run(self, agent_id: str, **inputs: Any) -> list[AgentDatum]:
        """Run an agent with the provided inputs.

        Args:
            agent_id: Agent UUID to run (can be base agent or version ID).
            **inputs: Dynamic inputs based on agent configuration.
                     Can include files, text, numbers, etc.
                     Files can be provided as:
                     - File paths (strings): Will be uploaded
                     - File objects: Will be uploaded
                     - FileUpload objects: Explicit control
                     - UUID strings: Roe file references

        Returns:
            List of agent execution results.

        Examples:
            # With file path
            result = agents.run(
                agent_id="uuid",
                document="path/to/file.pdf",
                prompt="Analyze this document"
            )

            # With Roe file ID
            result = agents.run(
                agent_id="uuid",
                document="3c90c3cc-0d44-4b50-8888-8dd25736052a",
                prompt="Analyze this document"
            )

            # With file object
            with open("file.pdf", "rb") as f:
                result = agents.run(
                    agent_id="uuid",
                    document=f,
                    prompt="Analyze this document"
                )
        """
        url = f"/v1/agents/run/{agent_id}/"

        # Add organization_id as query parameter if needed
        params = {"organization_id": self.config.organization_id}

        # Make the request with dynamic inputs
        response_data = self.http_client.post_with_dynamic_inputs(
            url=url,
            inputs=inputs,
            params=params,
        )

        # Parse the response into AgentDatum objects
        return [AgentDatum(**datum) for datum in response_data]
