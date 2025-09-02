"""Agents API implementation."""

from typing import Any

from roe.config import RoeConfig
from roe.models.agent import AgentVersion, BaseAgent
from roe.models.job import Job, JobBatch
from roe.models.responses import (
    AgentJobResult,
    AgentJobResultBatch,
    AgentJobStatus,
    AgentJobStatusBatch,
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

    def run(self, agent_id: str, **inputs: Any) -> "Job":
        """Run an agent and return a Job object.

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
            Job instance for tracking and waiting on the execution.

        Examples:
            # With file path
            job = agents.run(
                agent_id="uuid",
                document="path/to/file.pdf",
                prompt="Analyze this document"
            )
            result = job.wait()

            # With Roe file ID
            job = agents.run(
                agent_id="uuid",
                document="3c90c3cc-0d44-4b50-8888-8dd25736052a",
                prompt="Analyze this document"
            )

            # Check status before waiting
            status = job.get_status()
            if status.status == JobStatus.SUCCESS:
                result = job.get_result()
        """
        job_id = self.http_client.post_with_dynamic_inputs(
            url=f"/v1/agents/run/{agent_id}/async/",
            inputs=inputs,
        )

        return Job(self, job_id)

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

    def get_job_status_many(self, job_ids: list[str]) -> list[AgentJobStatusBatch]:
        """Get the status of multiple agent jobs.

        Args:
            job_ids: List of agent job UUIDs.

        Returns:
            List of AgentJobStatusBatch instances in the same order as job_ids.
        """
        response_data = self.http_client.post(
            "/v1/agents/jobs/statuses/", json_data={"job_ids": job_ids}
        )
        return [AgentJobStatusBatch(**status_data) for status_data in response_data]

    def get_job_result_many(self, job_ids: list[str]) -> list[AgentJobResultBatch]:
        """Get the results of multiple agent jobs.

        Args:
            job_ids: List of agent job UUIDs.

        Returns:
            List of AgentJobResultBatch instances in the same order as job_ids.
        """
        response_data = self.http_client.post(
            "/v1/agents/jobs/results/", json_data={"job_ids": job_ids}
        )
        return [AgentJobResultBatch(**result_data) for result_data in response_data]

    def run_many(self, agent_id: str, batch_inputs: list[dict[str, Any]]) -> "JobBatch":
        """Run an agent with multiple inputs and return a JobBatch.

        Args:
            agent_id: Agent UUID to run (can be base agent or version ID).
            batch_inputs: List of input dictionaries, each containing dynamic inputs
                        based on agent configuration. Can include files, text, numbers, etc.
                        Files can be provided as:
                        - File paths (strings): Will be uploaded
                        - File objects: Will be uploaded
                        - FileUpload objects: Explicit control
                        - UUID strings: Roe file references

        Returns:
            JobBatch instance for tracking and waiting on all executions.

        Examples:
            # With multiple file paths
            batch = agents.run_many(
                agent_id="uuid",
                batch_inputs=[
                    {"document": "file1.pdf", "prompt": "Analyze this document"},
                    {"document": "file2.pdf", "prompt": "Analyze this document"},
                    {"document": "file3.pdf", "prompt": "Analyze this document"}
                ]
            )
            results = batch.wait()

            # With mixed input types
            batch = agents.run_many(
                agent_id="uuid",
                batch_inputs=[
                    {"text": "Hello world", "count": 5},
                    {"text": "Goodbye world", "count": 3}
                ]
            )

            # Wait for all jobs to complete
            results = batch.wait()

            # Or access individual jobs
            first_job = batch.jobs[0]
            first_result = first_job.wait()
        """

        response_data = self.http_client.post(
            url=f"/v1/agents/run/{agent_id}/async/many/",
            json_data={"inputs": batch_inputs},
        )

        return JobBatch(self, response_data)
