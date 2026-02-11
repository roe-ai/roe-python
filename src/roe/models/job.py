"""Job and JobBatch models for agent execution tracking."""

import time
from typing import TYPE_CHECKING

from roe.exceptions import NotFoundError, RoeAPIException
from roe.models.responses import (
    AgentJobResource,
    AgentJobResult,
    AgentJobStatus,
    JobStatus,
)

if TYPE_CHECKING:
    from roe.api.agents import AgentsAPI


class Job:
    """Represents a single agent job for tracking and waiting."""

    def __init__(
        self,
        agents_api: "AgentsAPI",
        job_id: str,
        agent_id: str | None = None,
        timeout_seconds: int | None = None,
    ):
        """Initialize a Job instance.

        Args:
            agents_api: AgentsAPI instance for making requests.
            job_id: Agent job UUID.
            agent_id: Base agent UUID (enables server-side wait).
            timeout_seconds: Maximum time in seconds to wait for job completion.
                Defaults to 7200 (2 hours). Must be positive if provided.

        Raises:
            ValueError: If timeout_seconds is not positive.
        """
        self.agents_api = agents_api
        self._job_id = job_id
        self._agent_id = agent_id

        if timeout_seconds is None:
            self._timeout_seconds = 7200
        else:
            if timeout_seconds <= 0:
                raise ValueError(
                    f"timeout_seconds must be positive, got {timeout_seconds}"
                )
            self._timeout_seconds = timeout_seconds

    @property
    def id(self) -> str:
        """Get the job ID."""
        return self._job_id

    @property
    def agent_id(self) -> str | None:
        """Get the base agent ID (may be None for legacy jobs)."""
        return self._agent_id

    @property
    def timeout_seconds(self) -> int:
        """Get the configured timeout in seconds."""
        return self._timeout_seconds

    def wait(
        self, interval: float = 5.0, timeout: float | None = None
    ) -> AgentJobResult:
        """Wait for the job to complete and return its result.

        When *agent_id* is available the server-side wait endpoint is
        used for efficiency.  Otherwise falls back to client-side polling.

        Args:
            interval: Seconds between status checks (client-side fallback
                only; default 5.0).
            timeout: Maximum wait time in seconds.  Falls back to the
                instance *timeout_seconds*.

        Returns:
            AgentJobResult when the job reaches a terminal state.

        Raises:
            TimeoutError: If the job does not complete within the timeout.
            ValueError: If timeout is not positive.
        """
        if timeout is not None and timeout <= 0:
            raise ValueError(f"timeout must be positive, got {timeout}")

        effective_timeout = timeout if timeout is not None else self._timeout_seconds

        # Prefer server-side wait when agent_id is known
        if self._agent_id:
            start_time = time.time()
            try:
                resource = self.agents_api.jobs.wait(
                    agent_id=self._agent_id,
                    job_id=self._job_id,
                    timeout_seconds=int(effective_timeout),
                    poll_interval=interval,
                )
                return resource.to_result()
            except RoeAPIException as e:
                if e.status_code == 408:
                    raise TimeoutError(
                        f"Job {self._job_id} did not complete within {effective_timeout} seconds"
                    )
            except Exception:
                # Fall through to client-side polling on any transport error
                pass

            elapsed = time.time() - start_time
            remaining = effective_timeout - elapsed
            if remaining <= 0:
                raise TimeoutError(
                    f"Job {self._job_id} did not complete within {effective_timeout} seconds"
                )
            return self._poll_until_done(interval, remaining)

        # Client-side polling fallback
        return self._poll_until_done(interval, effective_timeout)

    def _poll_until_done(self, interval: float, timeout: float) -> AgentJobResult:
        """Client-side poll loop used when server-side wait is unavailable."""
        start_time = time.time()
        while True:
            status = self.retrieve_status()
            if status.status in (
                JobStatus.SUCCESS,
                JobStatus.FAILURE,
                JobStatus.CANCELLED,
                JobStatus.CACHED,
            ):
                return self.retrieve_result()

            if (time.time() - start_time) > timeout:
                raise TimeoutError(
                    f"Job {self._job_id} did not complete within {timeout} seconds"
                )
            time.sleep(interval)

    def wait_for_resource(
        self, interval: float = 5.0, timeout: float | None = None
    ) -> AgentJobResource:
        """Like :meth:`wait` but returns the full job resource.

        Requires *agent_id* to be set.

        Args:
            interval: Poll interval for server-side wait.
            timeout: Maximum wait time.

        Returns:
            AgentJobResource in terminal state.
        """
        effective_timeout = timeout if timeout is not None else self._timeout_seconds
        if not self._agent_id:
            raise ValueError("agent_id is required for wait_for_resource")
        return self.agents_api.jobs.wait(
            agent_id=self._agent_id,
            job_id=self._job_id,
            timeout_seconds=int(effective_timeout),
            poll_interval=interval,
        )

    def retrieve_status(self) -> AgentJobStatus:
        """Retrieve the current status of the job.

        Returns:
            AgentJobStatus instance.
        """
        return self.agents_api.jobs.retrieve_status(self._job_id)

    def retrieve_result(self) -> AgentJobResult:
        """Retrieve the result of the job.

        Returns:
            AgentJobResult instance.
        """
        return self.agents_api.jobs.retrieve_result(self._job_id)


class JobBatch:
    """Represents a batch of agent jobs for tracking and waiting."""

    def __init__(
        self,
        agents_api: "AgentsAPI",
        job_ids: list[str],
        agent_id: str | None = None,
        timeout_seconds: int | None = None,
    ):
        """Initialize a JobBatch instance.

        Args:
            agents_api: AgentsAPI instance for making requests.
            job_ids: List of agent job UUIDs.
            agent_id: Base agent UUID.
            timeout_seconds: Maximum wait time. Defaults to 7200 (2 hours).

        Raises:
            ValueError: If timeout_seconds is not positive.
        """
        self.agents_api = agents_api
        self._job_ids = job_ids
        self._agent_id = agent_id
        self._completed_jobs: dict[str, AgentJobResult] = {}
        self._job_statuses: dict[str, int] = {}

        if timeout_seconds is None:
            self._timeout_seconds = 7200
        else:
            if timeout_seconds <= 0:
                raise ValueError(
                    f"timeout_seconds must be positive, got {timeout_seconds}"
                )
            self._timeout_seconds = timeout_seconds

    @property
    def job_ids(self) -> list[str]:
        """Get the list of job IDs."""
        return self._job_ids.copy()

    @property
    def agent_id(self) -> str | None:
        """Get the base agent ID."""
        return self._agent_id

    @property
    def timeout_seconds(self) -> int:
        """Get the configured timeout in seconds."""
        return self._timeout_seconds

    @property
    def jobs(self) -> list[Job]:
        """Get individual Job objects for each job in the batch."""
        return [
            Job(
                self.agents_api,
                job_id,
                agent_id=self._agent_id,
                timeout_seconds=self._timeout_seconds,
            )
            for job_id in self._job_ids
        ]

    def wait(
        self,
        interval: float = 5.0,
        timeout: float | None = None,
        raise_on_timeout: bool = True,
    ) -> list[AgentJobResult | None]:
        """Wait for jobs in the batch to complete and return their results.

        Args:
            interval: Time in seconds between status checks (default 5.0).
            timeout: Maximum wait time.  Falls back to instance timeout.
            raise_on_timeout: If ``True`` (default), raises ``TimeoutError``
                when the timeout is reached and some jobs are still running.
                If ``False``, returns partial results instead — completed
                jobs get their ``AgentJobResult``, incomplete jobs are
                ``None``.

        Returns:
            List of ``AgentJobResult | None`` in the same order as
            ``job_ids``.  When ``raise_on_timeout=True`` all entries are
            guaranteed to be non-None (or a ``TimeoutError`` is raised).
            When ``raise_on_timeout=False``, incomplete jobs are ``None``.

        Raises:
            TimeoutError: If ``raise_on_timeout=True`` and jobs don't
                complete within the timeout.
            ValueError: If timeout is not positive.
        """
        if timeout is not None and timeout <= 0:
            raise ValueError(f"timeout must be positive, got {timeout}")

        effective_timeout = timeout if timeout is not None else self._timeout_seconds
        start_time = time.time()

        while len(self._completed_jobs) < len(self._job_ids):
            pending_job_ids = [
                job_id
                for job_id in self._job_ids
                if job_id not in self._completed_jobs
            ]

            if not pending_job_ids:
                break

            status_batch = self.agents_api.jobs.retrieve_status_many(pending_job_ids)

            completed_in_this_batch: list[str] = []
            for status_item in status_batch:
                job_id = status_item.id
                if status_item.status in (
                    JobStatus.SUCCESS,
                    JobStatus.FAILURE,
                    JobStatus.CANCELLED,
                    JobStatus.CACHED,
                ):
                    completed_in_this_batch.append(job_id)
                if status_item.status is not None:
                    self._job_statuses[job_id] = status_item.status

            if completed_in_this_batch:
                result_batch = self.agents_api.jobs.retrieve_result_many(
                    completed_in_this_batch
                )

                for result_item in result_batch:
                    job_id = result_item.id

                    if (
                        result_item.agent_id is None
                        or result_item.agent_version_id is None
                    ):
                        raise NotFoundError(
                            f"Job {job_id} not found or has been deleted"
                        )

                    job_result = AgentJobResult(
                        agent_id=result_item.agent_id,
                        agent_version_id=result_item.agent_version_id,
                        inputs=result_item.inputs or [],
                        input_tokens=result_item.input_tokens,
                        output_tokens=result_item.output_tokens,
                        outputs=result_item.result
                        if isinstance(result_item.result, list)
                        else [],
                    )

                    self._completed_jobs[job_id] = job_result

            if len(self._completed_jobs) < len(self._job_ids):
                if (time.time() - start_time) > effective_timeout:
                    if raise_on_timeout:
                        remaining_jobs = set(self._job_ids) - set(
                            self._completed_jobs.keys()
                        )
                        raise TimeoutError(
                            f"Jobs {remaining_jobs} did not complete within {effective_timeout} seconds"
                        )
                    break

                time.sleep(interval)

        return [self._completed_jobs.get(job_id) for job_id in self._job_ids]

    def retrieve_status(self) -> dict[str, int]:
        """Retrieve the current status of all jobs in the batch.

        Returns:
            Dictionary mapping job IDs to their current status codes.
        """
        status_map = {}
        jobs_to_query = []

        for job_id in self._job_ids:
            if job_id in self._job_statuses:
                status_map[job_id] = self._job_statuses[job_id]
            else:
                jobs_to_query.append(job_id)

        if jobs_to_query:
            status_batch = self.agents_api.jobs.retrieve_status_many(jobs_to_query)
            for status_item in status_batch:
                if status_item.status is not None:
                    status_map[status_item.id] = status_item.status
                    self._job_statuses[status_item.id] = status_item.status

        return status_map
