"""Main client for the Roe AI SDK."""

import httpx

from roe._generated.client import AuthenticatedClient as RawClient
from roe.api.agents import AgentsAPI
from roe.api.policies import PoliciesAPI
from roe.api.users import UsersAPI
from roe.auth import RoeAuth
from roe.config import RoeConfig
from roe.utils.transport import RoeRetryTransport


class RoeClient:
    """Main client for interacting with the Roe AI API."""

    def __init__(
        self,
        api_key: str | None = None,
        organization_id: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        batch_chunk_delay: float | None = None,
    ):
        """Initialize the Roe AI client.

        Args:
            api_key: API key for authentication. If not provided, will use ROE_API_KEY env var.
            organization_id: Organization ID. If not provided, will use ROE_ORGANIZATION_ID env var.
            base_url: Base URL for the API. If not provided, will use ROE_BASE_URL env var or default.
            timeout: Request timeout in seconds. If not provided, will use ROE_TIMEOUT env var or default.
            max_retries: Maximum number of retries. If not provided, will use ROE_MAX_RETRIES env var or default.
            batch_chunk_delay: Delay in seconds between batch chunk requests. If not provided, will use ROE_BATCH_CHUNK_DELAY env var or default (10.0).

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
            batch_chunk_delay=batch_chunk_delay,
        )

        # Create authentication
        self.auth = RoeAuth(self.config)

        # Build the shared httpx.Client. Retry on 502/503/504 (idempotent
        # methods only) lives in RoeRetryTransport so SDK calls and raw-client
        # calls share the same retry budget.
        self._httpx_client = httpx.Client(
            base_url=self.config.base_url,
            timeout=self.config.timeout,
            headers=self.auth.get_headers(),
            transport=RoeRetryTransport(max_retries=self.config.max_retries),
        )
        # token= and base_url= satisfy required AuthenticatedClient fields but
        # are not read at request time once set_httpx_client supplies the
        # underlying sync client. headers= and timeout= keep raw async calls
        # aligned with RoeClient configuration if users call client.raw directly.
        # raise_on_unexpected_status=False so non-2xx responses surface as a
        # parsed Response that translate_response() can map to a typed
        # RoeAPIException at the wrapper boundary.
        self._raw = RawClient(
            base_url=self.config.base_url,
            token=self.config.api_key,
            headers=self.auth.get_headers(),
            timeout=self.config.timeout,
            raise_on_unexpected_status=False,
        ).set_httpx_client(self._httpx_client)

        # Create API instances. All APIs delegate to the generated raw client.
        self._agents = AgentsAPI(self.config, self._raw)
        self._policies = PoliciesAPI(self.config, self._raw)
        self._users = UsersAPI(self.config, self._raw)

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

    @property
    def policies(self) -> PoliciesAPI:
        """Access the policies API for managing policies used by agentic workflows.

        Returns:
            PoliciesAPI instance for managing policies and policy versions.

        Examples:
            # Create a policy
            policy = client.policies.create(
                name="Investigation SOP",
                content={"guidelines": {...}, "instructions": "..."}
            )

            # List policies
            policies = client.policies.list()

            # Manage versions
            versions = client.policies.versions.list("policy-uuid")
        """
        return self._policies

    @property
    def users(self) -> UsersAPI:
        """Access the users API.

        Returns:
            UsersAPI instance for retrieving information about the
            authenticated user.

        Examples:
            # Get the current user
            me = client.users.me()
        """
        return self._users

    @property
    def raw(self) -> RawClient:
        """Access the generated raw client."""
        return self._raw

    def close(self) -> None:
        """Close the HTTP client and clean up resources."""
        self._httpx_client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
