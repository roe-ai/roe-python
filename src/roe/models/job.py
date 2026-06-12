"""Stateful Job and JobBatch helpers for tracking agent executions.

These are the only data classes that survive the migration in their
hand-written form — they own the polling loop and convert the generated
status codes into a familiar terminal-vs-pending decision. Body shapes
returned to callers come from the generated client.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any
from uuid import UUID

from roe._generated.models.agent_job_result_item import AgentJobResultItem
from roe._generated.models.agent_job_result_response import AgentJobResultResponse
from roe._generated.models.agent_job_single_status import AgentJobSingleStatus
from roe._generated.models.agent_job_status import AgentJobStatus
from roe.exceptions import NotFoundError, RoeAPIException

if TYPE_CHECKING:
    from roe.api.agents import AgentsAPI


class JobStatus:
    """Integer status codes the backend uses for an agent job.

    Mirrors the codes documented on ``AgentJobStatus.status``: 0 PENDING,
    1 STARTED, 2 RETRY, 3 SUCCESS, 4 FAILURE, 5 CANCELLED, 6 CACHED.
    """

    PENDING = 0
    STARTED = 1
    RETRY = 2
    SUCCESS = 3
    FAILURE = 4
    CANCELLED = 5
    CACHED = 6


_TERMINAL_STATUSES = (
    JobStatus.SUCCESS,
    JobStatus.FAILURE,
    JobStatus.CANCELLED,
    JobStatus.CACHED,
)
_FAILED_STATUSES = (JobStatus.FAILURE, JobStatus.CANCELLED)


def _empty_result(status: int, error_message: str | None) -> AgentJobResultResponse:
    """Synthesize a placeholder result for failed/cancelled jobs whose result fetch fails."""
    result = AgentJobResultResponse(
        agent_id=UUID(int=0),
        agent_version_id=UUID(int=0),
        inputs=[],
        input_tokens=None,
        output_tokens=None,
        outputs=[],
    )
    result.additional_properties["status"] = status
    result.additional_properties["error_message"] = error_message
    return result


def _attach_status(
    result: AgentJobResultResponse, status: int, error_message: str | None
) -> AgentJobResultResponse:
    result.additional_properties["status"] = status
    result.additional_properties["error_message"] = error_message
    return result


class Job:
    """Single-job handle with polling and status helpers."""

    def __init__(
        self, agents_api: "AgentsAPI", job_id: str, timeout_seconds: int | None = None
    ):
        self.agents_api = agents_api
        self._job_id = job_id

        if timeout_seconds is None:
            self._timeout_seconds = 7200  # 2 hours default
        else:
            if timeout_seconds <= 0:
                raise ValueError(
                    f"timeout_seconds must be positive, got {timeout_seconds}"
                )
            self._timeout_seconds = timeout_seconds

    @property
    def id(self) -> str:
        return self._job_id

    @property
    def timeout_seconds(self) -> int:
        return self._timeout_seconds

    def wait(
        self, interval: float = 5.0, timeout: float | None = None
    ) -> AgentJobResultResponse:
        """Poll until the job reaches a terminal state and return its result.

        Returns the generated ``AgentJobResultResponse`` with the terminal
        ``status`` (int code) and any ``error_message`` attached via the
        model's ``additional_properties`` dict — accessible as
        ``result["status"]`` and ``result["error_message"]``.
        """
        if timeout is not None and timeout <= 0:
            raise ValueError(f"timeout must be positive, got {timeout}")

        effective_timeout = timeout if timeout is not None else self._timeout_seconds
        start_time = time.time()

        from roe._generated.types import Unset

        while True:
            status = self.retrieve_status()
            error_message = (
                None if isinstance(status.error_message, Unset) else status.error_message
            )

            if status.status in _TERMINAL_STATUSES:
                is_failed = status.status in _FAILED_STATUSES
                try:
                    result = self.retrieve_result()
                except RoeAPIException:
                    if not is_failed:
                        raise
                    return _empty_result(status.status, error_message)
                return _attach_status(result, status.status, error_message)

            if (time.time() - start_time) > effective_timeout:
                raise TimeoutError(
                    f"Job {self._job_id} did not complete within {effective_timeout} seconds"
                )

            time.sleep(interval)

    def retrieve_status(self) -> AgentJobSingleStatus:
        """Generated ``AgentJobSingleStatus`` for the job."""
        return self.agents_api.jobs.retrieve_status(self._job_id)

    def retrieve_result(self) -> AgentJobResultResponse:
        """Generated ``AgentJobResultResponse`` for the job (may 404 if not terminal)."""
        return self.agents_api.jobs.retrieve_result(self._job_id)


class JobBatch:
    """Batch handle that polls many jobs in chunked status calls."""

    def __init__(
        self,
        agents_api: "AgentsAPI",
        job_ids: list[str],
        timeout_seconds: int | None = None,
    ):
        self.agents_api = agents_api
        self._job_ids = job_ids
        self._completed_jobs: dict[str, AgentJobResultItem] = {}
        self._job_statuses: dict[str, dict[str, Any]] = {}

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
        return self._job_ids.copy()

    @property
    def timeout_seconds(self) -> int:
        return self._timeout_seconds

    @property
    def jobs(self) -> list[Job]:
        return [
            Job(self.agents_api, job_id, self._timeout_seconds)
            for job_id in self._job_ids
        ]

    def wait(
        self,
        interval: float = 5.0,
        timeout: float | None = None,
        raise_on_timeout: bool = True,
    ) -> list[AgentJobResultItem | None]:
        """Poll and return per-job ``AgentJobResultItem`` (or ``None`` if not finished and ``raise_on_timeout=False``).

        ``AgentJobResultItem.status`` (the int code) is already populated by
        the batch results endpoint — no extra attachment needed.
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
                job_id = self._extract_id(status_item)
                if job_id is None:
                    continue
                stat_code = self._extract_status(status_item)
                if stat_code in _TERMINAL_STATUSES:
                    completed_in_this_batch.append(job_id)
                if stat_code is not None:
                    self._job_statuses[job_id] = {
                        "status": stat_code,
                        "error_message": self._extract_error_message(status_item),
                        "timestamp": self._extract_timestamp(status_item),
                    }

            if completed_in_this_batch:
                result_batch = self.agents_api.jobs.retrieve_result_many(
                    completed_in_this_batch
                )
                for result_item in result_batch:
                    job_id = str(result_item.id)
                    cached = self._job_statuses.get(job_id)
                    is_failed = (
                        cached is not None and cached["status"] in _FAILED_STATUSES
                    )
                    if (
                        result_item.agent_id is None
                        or result_item.agent_version_id is None
                    ):
                        if not is_failed:
                            raise NotFoundError(
                                f"Job {job_id} not found or has been deleted"
                            )
                    self._completed_jobs[job_id] = result_item

            if len(self._completed_jobs) < len(self._job_ids):
                if (time.time() - start_time) > effective_timeout:
                    if raise_on_timeout:
                        remaining = set(self._job_ids) - set(self._completed_jobs)
                        raise TimeoutError(
                            f"Jobs {remaining} did not complete within {effective_timeout} seconds"
                        )
                    break

                time.sleep(interval)

        return [self._completed_jobs.get(job_id) for job_id in self._job_ids]

    def retrieve_status(self) -> dict[str, AgentJobStatus]:
        """Return a ``{job_id: AgentJobStatus}`` map, querying only uncached jobs."""
        status_map: dict[str, AgentJobStatus] = {}
        jobs_to_query: list[str] = []

        for job_id in self._job_ids:
            cached = self._job_statuses.get(job_id)
            if cached is not None and cached["status"] in _TERMINAL_STATUSES:
                status_map[job_id] = AgentJobStatus(
                    id=UUID(str(job_id)),
                    status=cached["status"],
                    created_at=None,
                    last_updated_at=None,
                    timestamp=cached.get("timestamp", 0),
                    error_message=cached["error_message"]
                    if cached["error_message"] is not None
                    else _UNSET_SENTINEL(),
                )
            else:
                jobs_to_query.append(job_id)

        if jobs_to_query:
            status_batch = self.agents_api.jobs.retrieve_status_many(jobs_to_query)
            for status_item in status_batch:
                job_id = self._extract_id(status_item)
                if job_id is None:
                    continue
                stat_code = self._extract_status(status_item)
                if stat_code is None:
                    continue
                err = self._extract_error_message(status_item)
                status_map[job_id] = AgentJobStatus(
                    id=UUID(str(job_id)),
                    status=stat_code,
                    created_at=None,
                    last_updated_at=None,
                    timestamp=self._extract_timestamp(status_item),
                    error_message=err if err is not None else _UNSET_SENTINEL(),
                )
                self._job_statuses[job_id] = {
                    "status": stat_code,
                    "error_message": err,
                    "timestamp": self._extract_timestamp(status_item),
                }

        return status_map

    @staticmethod
    def _extract_id(status_item: Any) -> str | None:
        for key in ("id", "agent_job_id", "job_id"):
            value = getattr(status_item, key, None)
            if value is None:
                value = (
                    status_item.additional_properties.get(key)
                    if hasattr(status_item, "additional_properties")
                    else None
                )
            if value is not None:
                return str(value)
        return None

    @staticmethod
    def _extract_status(status_item: Any) -> int | None:
        from roe._generated.types import Unset

        value = getattr(status_item, "status", None)
        if isinstance(value, Unset) or value is None:
            return None
        return int(value)

    @staticmethod
    def _extract_error_message(status_item: Any) -> str | None:
        from roe._generated.types import Unset

        value = getattr(status_item, "error_message", None)
        if isinstance(value, Unset) or value is None:
            return None
        return str(value)

    @staticmethod
    def _extract_timestamp(status_item: Any) -> int:
        from roe._generated.types import Unset

        value = getattr(status_item, "timestamp", 0)
        if isinstance(value, Unset) or value is None:
            return 0
        return int(value)


def _UNSET_SENTINEL():  # noqa: N802 — match generated naming style
    """Return the ``Unset`` sentinel from the generated types module."""
    from roe._generated.types import UNSET

    return UNSET
