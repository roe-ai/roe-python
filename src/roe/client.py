"""Main client for the Roe AI SDK."""

from roe.api.agents import AgentsAPI
from roe.auth import RoeAuth
from roe.config import RoeConfig
from roe.utils.http_client import RoeHTTPClient


class RoeClient:
    """Main client for interacting with the Roe AI API."""

    def __init__(
        self,
        api_key: str | None = None,
        organization_id: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ):
        """Initialize the Roe AI client.

        Args:
            api_key: API key for authentication. If not provided, will use ROE_API_KEY env var.
            organization_id: Organization ID. If not provided, will use ROE_ORGANIZATION_ID env var.
            base_url: Base URL for the API. If not provided, will use ROE_BASE_URL env var or default.
            timeout: Request timeout in seconds. If not provided, will use ROE_TIMEOUT env var or default.
            max_retries: Maximum number of retries. If not provided, will use ROE_MAX_RETRIES env var or default.

        Raises:
            ValueError: If required parameters (api_key, organization_id) are not provided.

        Examples:
            # Initialize with parameters
            client = RoeClient(
                api_key="your-api-key",
                organization_id="your-org-uuid"
            )

            # Initialize from environment variables
            # Set ROE_API_KEY and ROE_ORGANIZATION_ID env vars
            client = RoeClient()

            # Mixed approach
            client = RoeClient(
                api_key="your-api-key",
                # organization_id will be read from ROE_ORGANIZATION_ID env var
            )
        """
        # Create configuration
        self.config = RoeConfig.from_env(
            api_key=api_key,
            organization_id=organization_id,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )

        # Create authentication
        self.auth = RoeAuth(self.config)

        # Create HTTP client
        self.http_client = RoeHTTPClient(self.config, self.auth)

        # Create API instances
        self._agents = AgentsAPI(self.config, self.http_client)

    @property
    def agents(self) -> AgentsAPI:
        """Access the agents API.

        Returns:
            AgentsAPI instance for managing and running agents.

        Examples:
            # List agents
            agents = client.agents.list()

            # Run an agent
            result = client.agents.run(
                agent_id="agent-uuid",
                document="path/to/file.pdf",
                prompt="Analyze this document"
            )

            # Get agent details and run
            agent = client.agents.get("agent-uuid")
            result = agent.run(
                document="path/to/file.pdf",
                prompt="Analyze this document"
            )
        """
        return self._agents

    def close(self) -> None:
        """Close the HTTP client and clean up resources."""
        self.http_client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
