"""Job and JobBatch models for agent execution tracking."""

import time
from typing import TYPE_CHECKING

from roe.exceptions import NotFoundError
from roe.models.responses import AgentJobResult, AgentJobStatus, JobStatus

if TYPE_CHECKING:
    from roe.api.agents import AgentsAPI


class Job:
    """Represents a single agent job for tracking and waiting."""

    def __init__(self, agents_api: "AgentsAPI", job_id: str, timeout_seconds: int | None = None):
        """Initialize a Job instance.

        Args:
            agents_api: AgentsAPI instance for making requests.
            job_id: Agent job UUID.
            timeout_seconds: Maximum time in seconds to wait for job completion. Defaults to 7200 (2 hours).
                           Must be positive if provided.

        Raises:
            ValueError: If timeout_seconds is not positive.

        Examples:
            # Typically created by run_async
            job = client.agents.run_async(agent_id, inputs)
            result = job.wait()
        """
        self.agents_api = agents_api
        self._job_id = job_id
        
        # Set default timeout
        if timeout_seconds is None:
            self._timeout_seconds = 7200  # 2 hours default
        else:
            # Validate timeout is positive
            if timeout_seconds <= 0:
                raise ValueError(f"timeout_seconds must be positive, got {timeout_seconds}")
            self._timeout_seconds = timeout_seconds

    @property
    def id(self) -> str:
        """Get the job ID.

        Returns:
            Agent job UUID string.
        """
        return self._job_id

    @property
    def timeout_seconds(self) -> int:
        """Get the configured timeout in seconds.

        Returns:
            Timeout value in seconds.
        """
        return self._timeout_seconds

    def wait(
        self, interval: float = 5.0, timeout: float | None = None
    ) -> AgentJobResult:
        """Wait for the job to complete and return its result.

        Args:
            interval: Time in seconds between status checks (default: 5.0).
            timeout: Maximum time in seconds to wait. If None, uses the timeout_seconds
                    specified when creating the job (default: 7200 seconds).
                    Must be positive if provided.

        Returns:
            AgentJobResult when the job completes successfully.

        Raises:
            TimeoutError: If the job doesn't complete within the timeout.
            ValueError: If timeout is not positive.

        Examples:
            # Basic usage - uses default timeout of 7200 seconds
            result = job.wait()

            # With custom interval and timeout
            result = job.wait(interval=2.0, timeout=300)
        """
        # Use provided timeout or fall back to instance timeout
        if timeout is not None and timeout <= 0:
            raise ValueError(f"timeout must be positive, got {timeout}")
        
        effective_timeout = timeout if timeout is not None else self._timeout_seconds
        start_time = time.time()

        while True:
            status = self.get_status()

            if status.status in (
                JobStatus.SUCCESS,
                JobStatus.FAILURE,
                JobStatus.CANCELLED,
                JobStatus.CACHED,
            ):
                # Return result regardless of success/failure - let user check status if needed
                return self.get_result()

            if (time.time() - start_time) > effective_timeout:
                raise TimeoutError(
                    f"Job {self._job_id} did not complete within {effective_timeout} seconds"
                )

            time.sleep(interval)

    def get_status(self) -> AgentJobStatus:
        """Get the current status of the job.

        Returns:
            AgentJobStatus instance with current job status.

        Examples:
            status = job.get_status()
            if status.status == JobStatus.SUCCESS:
                result = job.get_result()
        """
        return self.agents_api.get_job_status(self._job_id)

    def get_result(self) -> AgentJobResult:
        """Get the result of the job.

        Returns:
            AgentJobResult instance.

        Note:
            This method will return the result regardless of job status.
            For completed jobs only, use wait() which handles status checking.

        Examples:
            # Get result (may fail if job not complete)
            try:
                result = job.get_result()
            except Exception:
                # Job may not be complete yet
                result = job.wait()  # Wait for completion
        """
        return self.agents_api.get_job_result(self._job_id)


class JobBatch:
    """Represents a batch of agent jobs for tracking and waiting."""

    def __init__(self, agents_api: "AgentsAPI", job_ids: list[str], timeout_seconds: int | None = None):
        """Initialize a JobBatch instance.

        Args:
            agents_api: AgentsAPI instance for making requests.
            job_ids: List of agent job UUIDs.
            timeout_seconds: Maximum time in seconds to wait for jobs completion. Defaults to 7200 (2 hours).
                           Must be positive if provided.

        Raises:
            ValueError: If timeout_seconds is not positive.

        Examples:
            # Typically created by run_async_many
            batch = client.agents.run_async_many(agent_id, inputs_list)
            results = batch.wait()
        """
        self.agents_api = agents_api
        self._job_ids = job_ids
        self._completed_jobs: dict[str, AgentJobResult] = {}
        self._job_statuses: dict[str, int] = {}
        
        # Set default timeout
        if timeout_seconds is None:
            self._timeout_seconds = 7200  # 2 hours default
        else:
            # Validate timeout is positive
            if timeout_seconds <= 0:
                raise ValueError(f"timeout_seconds must be positive, got {timeout_seconds}")
            self._timeout_seconds = timeout_seconds

    @property
    def job_ids(self) -> list[str]:
        """Get the list of job IDs.

        Returns:
            List of agent job UUID strings.
        """
        return self._job_ids.copy()

    @property
    def timeout_seconds(self) -> int:
        """Get the configured timeout in seconds.

        Returns:
            Timeout value in seconds.
        """
        return self._timeout_seconds

    @property
    def jobs(self) -> list[Job]:
        """Get individual Job objects for each job in the batch.

        Returns:
            List of Job instances for individual job operations.

        Examples:
            batch = client.agents.run_async_many(agent_id, inputs_list)

            # Access individual jobs
            first_job = batch.jobs[0]
            first_result = first_job.wait()

            # Or wait for all
            all_results = batch.wait()
        """
        return [Job(self.agents_api, job_id, self._timeout_seconds) for job_id in self._job_ids]

    def wait(
        self, interval: float = 5.0, timeout: float | None = None
    ) -> list[AgentJobResult]:
        """Wait for all jobs in the batch to complete and return their results.

        Args:
            interval: Time in seconds between status checks (default: 5.0).
            timeout: Maximum time in seconds to wait. If None, uses the timeout_seconds
                    specified when creating the batch (default: 7200 seconds).
                    Must be positive if provided.

        Returns:
            List of AgentJobResult instances in the same order as job_ids.

        Raises:
            TimeoutError: If jobs don't complete within the timeout.
            ValueError: If timeout is not positive.

        Examples:
            # Basic usage - wait for all jobs to complete with default timeout
            results = batch.wait()

            # With custom interval and timeout
            results = batch.wait(interval=2.0, timeout=300)
        """
        # Use provided timeout or fall back to instance timeout
        if timeout is not None and timeout <= 0:
            raise ValueError(f"timeout must be positive, got {timeout}")
        
        effective_timeout = timeout if timeout is not None else self._timeout_seconds
        start_time = time.time()

        while len(self._completed_jobs) < len(self._job_ids):
            pending_job_ids = [
                job_id for job_id in self._job_ids if job_id not in self._completed_jobs
            ]

            if not pending_job_ids:
                break

            status_batch = self.agents_api.get_job_status_many(pending_job_ids)

            # Find jobs that moved to terminal states
            completed_in_this_batch = []
            for status_item in status_batch:
                job_id = status_item.id
                if status_item.status in (
                    JobStatus.SUCCESS,
                    JobStatus.FAILURE,
                    JobStatus.CANCELLED,
                    JobStatus.CACHED,
                ):
                    completed_in_this_batch.append(job_id)

                # Update status cache (only if status is not None)
                if status_item.status is not None:
                    self._job_statuses[job_id] = status_item.status

            if completed_in_this_batch:
                result_batch = self.agents_api.get_job_result_many(
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
                    remaining_jobs = set(self._job_ids) - set(
                        self._completed_jobs.keys()
                    )
                    raise TimeoutError(
                        f"Jobs {remaining_jobs} did not complete within {effective_timeout} seconds"
                    )

                time.sleep(interval)

        return [self._completed_jobs[job_id] for job_id in self._job_ids]

    def get_status(self) -> dict[str, int]:
        """Get the current status of all jobs in the batch.

        Returns:
            Dictionary mapping job IDs to their current status codes.
            Status codes: 0=PENDING, 1=STARTED, 2=RETRY, 3=SUCCESS, 4=FAILURE, 5=CANCELLED, 6=CACHED

        Examples:
            status_map = batch.get_status()
            print(f"Batch status: {status_map}")

            # Check individual statuses
            for job_id, status_code in status_map.items():
                if status_code == JobStatus.SUCCESS:
                    print(f"Job {job_id} completed successfully")
        """
        # Return cached status for completed jobs, query for others
        status_map = {}
        jobs_to_query = []

        for job_id in self._job_ids:
            if job_id in self._job_statuses:
                status_map[job_id] = self._job_statuses[job_id]
            else:
                jobs_to_query.append(job_id)

        # Query only jobs we don't have cached status for
        if jobs_to_query:
            status_batch = self.agents_api.get_job_status_many(jobs_to_query)
            for status_item in status_batch:
                if status_item.status is not None:
                    status_map[status_item.id] = status_item.status
                    self._job_statuses[status_item.id] = status_item.status

        return status_map
