"""Agents API implementation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from roe.config import RoeConfig
from roe.models.agent import AgentVersion, BaseAgent
from roe.models.job import Job, JobBatch
from roe.models.responses import (
    AgentDatum,
    AgentJobResult,
    AgentJobResultBatch,
    AgentJobStatus,
    AgentJobStatusBatch,
    JobDataDeleteResponse,
    PaginatedResponse,
)
from roe.utils.http_client import RoeHTTPClient
from roe.utils.pagination import PaginationHelper

if TYPE_CHECKING:
    from roe.api.agents import AgentsAPI


class AgentVersionsAPI:
    """Nested API for agent version operations."""

    def __init__(self, agents_api: "AgentsAPI"):
        """Initialize the versions API.

        Args:
            agents_api: Parent AgentsAPI instance.
        """
        self._agents_api = agents_api

    @property
    def http_client(self) -> RoeHTTPClient:
        return self._agents_api.http_client

    def list(self, agent_id: str) -> list[AgentVersion]:
        """List all versions of an agent.

        Args:
            agent_id: Base agent UUID.

        Returns:
            List of agent versions.
        """
        response_data = self.http_client.get(f"/v1/agents/{agent_id}/versions/")
        versions = [AgentVersion(**version_data) for version_data in response_data]
        for version in versions:
            version.set_agents_api(self._agents_api)
        return versions

    def retrieve(
        self, agent_id: str, version_id: str, get_supports_eval: bool | None = None
    ) -> AgentVersion:
        """Retrieve a specific version of an agent.

        Args:
            agent_id: Base agent UUID.
            version_id: Version UUID.
            get_supports_eval: Include information on whether the agent engine supports evaluation.

        Returns:
            AgentVersion instance.
        """
        params = {}
        if get_supports_eval is not None:
            params["get_supports_eval"] = str(get_supports_eval).lower()

        response_data = self.http_client.get(
            f"/v1/agents/{agent_id}/versions/{version_id}/", params=params
        )

        version = AgentVersion(**response_data)
        version.set_agents_api(self._agents_api)
        return version

    def retrieve_current(self, agent_id: str) -> AgentVersion:
        """Retrieve the current version of an agent.

        Args:
            agent_id: Base agent UUID.

        Returns:
            Current AgentVersion.
        """
        response_data = self.http_client.get(f"/v1/agents/{agent_id}/versions/current/")
        version = AgentVersion(**response_data)
        version.set_agents_api(self._agents_api)
        return version

    def create(
        self,
        agent_id: str,
        input_definitions: list[dict[str, Any]] | None = None,
        engine_config: dict[str, Any] | None = None,
        version_name: str | None = None,
        description: str | None = None,
    ) -> AgentVersion:
        """Create a new version of an agent.

        Args:
            agent_id: Base agent UUID.
            input_definitions: List of input definitions for the version.
            engine_config: Engine configuration (model, instruction, output_schema, etc.).
            version_name: Name for the version.
            description: Description of the version.

        Returns:
            Created AgentVersion instance.
        """
        json_data: dict[str, Any] = {
            "input_definitions": input_definitions or [],
            "engine_config": engine_config or {},
        }

        if version_name is not None:
            json_data["version_name"] = version_name
        if description is not None:
            json_data["description"] = description

        response_data = self.http_client.post(
            f"/v1/agents/{agent_id}/versions/", json_data=json_data
        )
        version_id = response_data["id"]
        return self.retrieve(agent_id, version_id)

    def update(
        self,
        agent_id: str,
        version_id: str,
        version_name: str | None = None,
        description: str | None = None,
    ) -> None:
        """Update an agent version.

        Args:
            agent_id: Base agent UUID.
            version_id: Version UUID.
            version_name: New version name.
            description: New description.
        """
        json_data: dict[str, Any] = {}

        if version_name is not None:
            json_data["version_name"] = version_name
        if description is not None:
            json_data["description"] = description

        self.http_client.put(
            f"/v1/agents/{agent_id}/versions/{version_id}/", json_data=json_data
        )

    def delete(self, agent_id: str, version_id: str) -> None:
        """Delete an agent version.

        Args:
            agent_id: Base agent UUID.
            version_id: Version UUID to delete.
        """
        self.http_client.delete(f"/v1/agents/{agent_id}/versions/{version_id}/")


class AgentJobsAPI:
    """Nested API for agent job operations."""

    _MAX_BATCH_SIZE = 1000

    def __init__(self, agents_api: "AgentsAPI"):
        """Initialize the jobs API.

        Args:
            agents_api: Parent AgentsAPI instance.
        """
        self._agents_api = agents_api

    @property
    def http_client(self) -> RoeHTTPClient:
        return self._agents_api.http_client

    def _iter_chunks(self, items, chunk_size: int):
        """Yield successive chunks from a list."""
        for i in range(0, len(items), chunk_size):
            yield items[i : i + chunk_size]

    def retrieve_status(self, job_id: str) -> AgentJobStatus:
        """Retrieve the status of an agent job.

        Args:
            job_id: Agent job UUID.

        Returns:
            AgentJobStatus instance.
        """
        response_data = self.http_client.get(f"/v1/agents/jobs/{job_id}/status/")
        return AgentJobStatus(**response_data)

    def retrieve_result(self, job_id: str) -> AgentJobResult:
        """Retrieve the result of an agent job.

        Args:
            job_id: Agent job UUID.

        Returns:
            AgentJobResult instance.
        """
        response_data = self.http_client.get(f"/v1/agents/jobs/{job_id}/result/")
        return AgentJobResult(**response_data)

    def retrieve_status_many(self, job_ids: list[str]) -> list[AgentJobStatusBatch]:
        """Retrieve the status of multiple agent jobs.

        Args:
            job_ids: List of agent job UUIDs.

        Returns:
            List of AgentJobStatusBatch instances in the same order as job_ids.
        """
        results: list[AgentJobStatusBatch] = []
        for chunk in self._iter_chunks(job_ids, self._MAX_BATCH_SIZE):
            if not chunk:
                continue
            response_data = self.http_client.post(
                "/v1/agents/jobs/statuses/", json_data={"job_ids": chunk}
            )
            results.extend(
                AgentJobStatusBatch(**status_data) for status_data in response_data
            )
        return results

    def retrieve_result_many(self, job_ids: list[str]) -> list[AgentJobResultBatch]:
        """Retrieve the results of multiple agent jobs.

        Args:
            job_ids: List of agent job UUIDs.

        Returns:
            List of AgentJobResultBatch instances in the same order as job_ids.
        """
        results: list[AgentJobResultBatch] = []
        for chunk in self._iter_chunks(job_ids, self._MAX_BATCH_SIZE):
            if not chunk:
                continue
            response_data = self.http_client.post(
                "/v1/agents/jobs/results/", json_data={"job_ids": chunk}
            )
            results.extend(
                AgentJobResultBatch(**result_data) for result_data in response_data
            )
        return results

    def download_reference(
        self, job_id: str, resource_id: str, as_attachment: bool = False
    ) -> bytes:
        """Download a reference file from an agent job.

        Args:
            job_id: Agent job UUID.
            resource_id: Resource identifier (filename).
            as_attachment: Whether to download as attachment.

        Returns:
            Raw bytes of the file content.
        """
        params = {}
        if as_attachment:
            params["download"] = "true"

        return self.http_client.get_bytes(
            f"/v1/agents/jobs/{job_id}/references/{resource_id}/",
            params=params if params else None,
        )

    def delete_data(self, job_id: str) -> JobDataDeleteResponse:
        """Delete persisted data for an agent job.

        Deletes uploaded input files and sanitizes stored outputs.
        Only works for jobs in terminal states (SUCCESS, FAILURE, CANCELLED).

        Args:
            job_id: Agent job UUID.

        Returns:
            JobDataDeleteResponse with deletion status.
        """
        response_data = self.http_client.post(f"/v1/agents/jobs/{job_id}/delete-data/")
        return JobDataDeleteResponse(**response_data)


class AgentsAPI:
    """API for managing and running agents."""

    _MAX_BATCH_SIZE = 1000

    def __init__(self, config: RoeConfig, http_client: RoeHTTPClient):
        """Initialize the agents API.

        Args:
            config: Roe configuration.
            http_client: HTTP client instance.
        """
        self.config = config
        self.http_client = http_client
        self._versions = AgentVersionsAPI(self)
        self._jobs = AgentJobsAPI(self)

    @property
    def versions(self) -> AgentVersionsAPI:
        """Access the versions sub-API for version operations.

        Returns:
            AgentVersionsAPI instance.

        Examples:
            versions = client.agents.versions.list("agent-uuid")
            version = client.agents.versions.retrieve("agent-uuid", "version-uuid")
        """
        return self._versions

    @property
    def jobs(self) -> AgentJobsAPI:
        """Access the jobs sub-API for job operations.

        Returns:
            AgentJobsAPI instance.

        Examples:
            status = client.agents.jobs.retrieve_status("job-uuid")
            result = client.agents.jobs.retrieve_result("job-uuid")
        """
        return self._jobs

    def _iter_chunks(self, items, chunk_size: int):
        """Yield successive chunks from a list."""
        for i in range(0, len(items), chunk_size):
            yield items[i : i + chunk_size]

    def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedResponse[BaseAgent]:
        """List agents in the organization.

        Args:
            page: Page number (1-based).
            page_size: Number of results per page.

        Returns:
            Paginated list of agents.
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

    def retrieve(self, agent_id: str) -> BaseAgent:
        """Retrieve a specific agent by ID.

        Args:
            agent_id: Agent UUID.

        Returns:
            BaseAgent instance.
        """
        response_data = self.http_client.get(f"/v1/agents/{agent_id}/")
        base_agent = BaseAgent(**response_data)
        base_agent.set_agents_api(self)
        return base_agent

    def create(
        self,
        name: str,
        engine_class_id: str,
        input_definitions: list[dict[str, Any]] | None = None,
        engine_config: dict[str, Any] | None = None,
        version_name: str | None = None,
        description: str | None = None,
    ) -> BaseAgent:
        """Create a new agent.

        Args:
            name: Name of the agent.
            engine_class_id: Engine class ID (e.g., "TextExtractionEngine").
            input_definitions: List of input definitions for the agent.
            engine_config: Engine configuration (model, instruction, output_schema, etc.).
            version_name: Name for the first version (defaults to "version 1").
            description: Description of the first version.

        Returns:
            Created BaseAgent instance.
        """
        json_data: dict[str, Any] = {
            "name": name,
            "engine_class_id": engine_class_id,
            "organization_id": self.config.organization_id,
            "input_definitions": input_definitions or [],
            "engine_config": engine_config or {},
        }

        if version_name is not None:
            json_data["version_name"] = version_name
        if description is not None:
            json_data["description"] = description

        response_data = self.http_client.post("/v1/agents/", json_data=json_data)
        base_agent = BaseAgent(**response_data)
        base_agent.set_agents_api(self)
        return base_agent

    def update(
        self,
        agent_id: str,
        name: str | None = None,
        disable_cache: bool | None = None,
        cache_failed_jobs: bool | None = None,
    ) -> BaseAgent:
        """Update an agent.

        Args:
            agent_id: Agent UUID.
            name: New name for the agent.
            disable_cache: Whether to disable job cache fetching.
            cache_failed_jobs: Whether to cache failed jobs.

        Returns:
            Updated BaseAgent instance.
        """
        json_data: dict[str, Any] = {}

        if name is not None:
            json_data["name"] = name
        if disable_cache is not None:
            json_data["disable_cache"] = disable_cache
        if cache_failed_jobs is not None:
            json_data["cache_failed_jobs"] = cache_failed_jobs

        response_data = self.http_client.put(
            f"/v1/agents/{agent_id}/", json_data=json_data
        )
        base_agent = BaseAgent(**response_data)
        base_agent.set_agents_api(self)
        return base_agent

    def delete(self, agent_id: str) -> None:
        """Delete an agent and all its versions.

        Args:
            agent_id: Agent UUID.
        """
        self.http_client.delete(f"/v1/agents/{agent_id}/")

    def duplicate(self, agent_id: str) -> BaseAgent:
        """Duplicate an agent.

        Creates a new agent with the same configuration as the source agent.
        The new agent will have a different ID.

        Args:
            agent_id: Agent UUID to duplicate.

        Returns:
            BaseAgent instance of the newly created agent.
        """
        response_data = self.http_client.post(f"/v1/agents/{agent_id}/duplicate/")
        # The duplicate endpoint returns an AgentVersion, extract the base_agent
        base_agent = BaseAgent(**response_data["base_agent"])
        base_agent.set_agents_api(self)
        return base_agent

    def run(
        self, agent_id: str, timeout_seconds: int | None = None, **inputs: Any
    ) -> Job:
        """Run an agent and return a Job object.

        Args:
            agent_id: Agent UUID to run (can be base agent or version ID).
            timeout_seconds: Maximum time in seconds to wait for job completion.
                           Defaults to 7200 seconds (2 hours).
            **inputs: Dynamic inputs based on agent configuration.

        Returns:
            Job instance for tracking and waiting on the execution.

        Examples:
            job = client.agents.run(agent_id="uuid", text="Analyze this")
            result = job.wait()
        """
        job_id = self.http_client.post_with_dynamic_inputs(
            url=f"/v1/agents/run/{agent_id}/async/",
            inputs=inputs,
        )

        return Job(self, job_id, timeout_seconds)

    def run_many(
        self,
        agent_id: str,
        batch_inputs: list[dict[str, Any]],
        timeout_seconds: int | None = None,
    ) -> JobBatch:
        """Run an agent with multiple inputs and return a JobBatch.

        Args:
            agent_id: Agent UUID to run.
            batch_inputs: List of input dictionaries.
            timeout_seconds: Maximum time in seconds to wait for jobs completion.

        Returns:
            JobBatch instance for tracking and waiting on all executions.
        """
        all_job_ids: list[str] = []
        for chunk in self._iter_chunks(batch_inputs, self._MAX_BATCH_SIZE):
            if not chunk:
                continue
            json_data = {"inputs": chunk}
            response_data = self.http_client.post(
                url=f"/v1/agents/run/{agent_id}/async/many/",
                json_data=json_data,
            )
            all_job_ids.extend(response_data)

        return JobBatch(self, all_job_ids, timeout_seconds)

    def run_sync(self, agent_id: str, **inputs: Any) -> list[AgentDatum]:
        """Run an agent synchronously and return results directly.

        Args:
            agent_id: Agent UUID to run (uses current version).
            **inputs: Dynamic inputs based on agent configuration.

        Returns:
            List of AgentDatum outputs.
        """
        response_data = self.http_client.post_with_dynamic_inputs(
            url=f"/v1/agents/run/{agent_id}/",
            inputs=inputs,
        )
        return [AgentDatum(**datum) for datum in response_data]

    def run_version(
        self,
        agent_id: str,
        version_id: str,
        timeout_seconds: int | None = None,
        **inputs: Any,
    ) -> Job:
        """Run a specific agent version asynchronously.

        Args:
            agent_id: Base agent UUID.
            version_id: Version UUID to run.
            timeout_seconds: Maximum time in seconds to wait for job completion.
            **inputs: Dynamic inputs based on agent configuration.

        Returns:
            Job instance for tracking and waiting on the execution.
        """
        job_id = self.http_client.post_with_dynamic_inputs(
            url=f"/v1/agents/run/{agent_id}/versions/{version_id}/async/",
            inputs=inputs,
        )
        return Job(self, job_id, timeout_seconds)

    def run_version_sync(
        self, agent_id: str, version_id: str, **inputs: Any
    ) -> list[AgentDatum]:
        """Run a specific agent version synchronously.

        Args:
            agent_id: Base agent UUID.
            version_id: Version UUID to run.
            **inputs: Dynamic inputs based on agent configuration.

        Returns:
            List of AgentDatum outputs.
        """
        response_data = self.http_client.post_with_dynamic_inputs(
            url=f"/v1/agents/run/{agent_id}/versions/{version_id}/",
            inputs=inputs,
        )
        return [AgentDatum(**datum) for datum in response_data]
