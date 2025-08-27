"""Agents API implementation."""

import time
from typing import Any

from roe.config import RoeConfig
from roe.models.agent import AgentVersion, BaseAgent
from roe.models.responses import (
    AgentDatum,
    AgentJobResult,
    AgentJobStatus,
    JobStatus,
    PaginatedResponse,
)
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
        params = PaginationHelper.build_query_params(
            organization_id=self.config.organization_id,
            page=page,
            page_size=page_size,
        )

        response_data = self.http_client.get("/v1/agents/", params=params)

        base_agents = [
            BaseAgent(**agent_data) for agent_data in response_data["results"]
        ]

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
        response_data = self.http_client.get(f"/v1/agents/{agent_id}/")
        base_agent = BaseAgent(**response_data)
        base_agent.set_agents_api(self)
        return base_agent

    def list_versions(self, base_agent_id: str) -> list[AgentVersion]:
        """List all versions of a base agent.

        Args:
            base_agent_id: Base agent UUID.

        Returns:
            List of agent versions.
        """
        response_data = self.http_client.get(f"/v1/agents/{base_agent_id}/versions/")
        versions = [AgentVersion(**version_data) for version_data in response_data]
        for version in versions:
            version.set_agents_api(self)
        return versions

    def get_version(
        self, base_agent_id: str, version_id: str, get_supports_eval: bool | None = None
    ) -> AgentVersion:
        """Get a specific version of a base agent.

        Args:
            base_agent_id: Base agent UUID.
            version_id: Version UUID.
            get_supports_eval: Include information on whether the agent engine supports evaluation.

        Returns:
            AgentVersion instance.
        """
        params = {}
        if get_supports_eval is not None:
            params["get_supports_eval"] = str(get_supports_eval).lower()

        response_data = self.http_client.get(
            f"/v1/agents/{base_agent_id}/versions/{version_id}/", params=params
        )

        version = AgentVersion(**response_data)
        version.set_agents_api(self)
        return version

    def get_current_version(self, base_agent_id: str) -> AgentVersion:
        """Get the current version of a base agent.

        Args:
            base_agent_id: Base agent UUID.

        Returns:
            Current AgentVersion.
        """
        response_data = self.http_client.get(
            f"/v1/agents/{base_agent_id}/versions/current/"
        )
        version = AgentVersion(**response_data)
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
        response_data = self.http_client.post_with_dynamic_inputs(
            url=f"/v1/agents/run/{agent_id}/",
            inputs=inputs,
        )

        return [AgentDatum(**datum) for datum in response_data]

    def run_async(self, agent_id: str, **inputs: Any) -> str:
        """Run an agent asynchronously and return job ID.

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
            Agent job ID string.

        Examples:
            # With file path
            job_id = agents.run_async(
                agent_id="uuid",
                document="path/to/file.pdf",
                prompt="Analyze this document"
            )

            # With Roe file ID
            job_id = agents.run_async(
                agent_id="uuid",
                document="3c90c3cc-0d44-4b50-8888-8dd25736052a",
                prompt="Analyze this document"
            )
        """
        job_id = self.http_client.post_with_dynamic_inputs(
            url=f"/v1/agents/run/{agent_id}/async/",
            inputs=inputs,
        )

        return job_id

    def get_job_status(self, job_id: str) -> AgentJobStatus:
        """Get the status of an agent job.

        Args:
            job_id: Agent job UUID.

        Returns:
            AgentJobStatus instance.
        """
        response_data = self.http_client.get(f"/v1/agents/jobs/{job_id}/status/")
        return AgentJobStatus(**response_data)

    def get_job_result(self, job_id: str) -> AgentJobResult:
        """Get the result of an agent job.

        Args:
            job_id: Agent job UUID.

        Returns:
            AgentJobResult instance.
        """
        response_data = self.http_client.get(f"/v1/agents/jobs/{job_id}/result/")
        return AgentJobResult(**response_data)

    def wait_for_job_completion(
        self, job_id: str, poll_interval: float = 5.0, timeout: float | None = None
    ) -> AgentJobResult:
        """Wait for a job to complete and return its result.

        Args:
            job_id: Agent job UUID.
            poll_interval: Time in seconds between status checks (default: 5.0).
            timeout: Maximum time in seconds to wait. None means no timeout.

        Returns:
            AgentJobResult when the job completes successfully.

        Raises:
            TimeoutError: If the job doesn't complete within the timeout.
            RuntimeError: If the job fails or is cancelled.
        """
        start_time = time.time()

        while True:
            status = self.get_job_status(job_id)

            if status.status == JobStatus.SUCCESS:
                return self.get_job_result(job_id)
            elif status.status == JobStatus.FAILURE:
                raise RuntimeError(f"Job {job_id} failed")
            elif status.status == JobStatus.CANCELLED:
                raise RuntimeError(f"Job {job_id} was cancelled")
            elif status.status == JobStatus.CACHED:
                # Cached results are also successful
                return self.get_job_result(job_id)

            if timeout and (time.time() - start_time) > timeout:
                raise TimeoutError(
                    f"Job {job_id} did not complete within {timeout} seconds"
                )

            time.sleep(poll_interval)
