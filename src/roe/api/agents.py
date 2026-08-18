"""Agents API — thin facade over the generated raw client.

Each public method delegates to a generated endpoint under
``roe._generated.api.v1`` (or v2 where applicable) and returns the generated
response model directly. Non-2xx responses are translated to the typed
``RoeAPIException`` family via ``translate_response`` at the wrapper boundary.

The dynamic-input multipart paths (``run``, ``run_sync``, ``run_version``,
``run_version_sync``) bypass the generated request model's broken
``to_multipart()`` and use ``call_dynamic`` to inject our own multipart body
through the generated endpoint's URL/auth/query machinery.
"""

from __future__ import annotations

import datetime
import time
from typing import Any
from uuid import UUID

from roe._generated.api.agents import (
    agents_create,
    agents_destroy,
    agents_duplicate_create,
    agents_jobs_artifacts_result_retrieve,
    agents_jobs_cancel_all_create,
    agents_jobs_cancel_create,
    agents_jobs_webhook_resend_create,
    agents_jobs_delete_data_create,
    agents_jobs_list,
    agents_jobs_references_retrieve,
    agents_jobs_result_retrieve,
    agents_jobs_results_create,
    agents_jobs_status_retrieve,
    agents_jobs_statuses_create,
    agents_list,
    agents_partial_update,
    agents_retrieve,
    agents_run,
    agents_run_async_create,
    agents_run_async_many,
    agents_run_version,
    agents_update,
    agents_run_versions_async_create,
    agents_versions_create,
    agents_versions_current_retrieve,
    agents_versions_destroy,
    agents_versions_list,
    agents_versions_partial_update,
    agents_versions_retrieve,
    agents_versions_update,
)
from roe._generated.client import AuthenticatedClient
from roe._generated.models.agent_datum import AgentDatum
from roe._generated.models.agent_execution_request import (
    AgentExecutionRequest,
)
from roe._generated.models.agent_job_artifact_result import AgentJobArtifactResult
from roe._generated.models.agent_job_cancel_all_response import (
    AgentJobCancelAllResponse,
)
from roe._generated.models.resend_agent_job_webhook_request import (
    ResendAgentJobWebhookRequest,
)
from roe._generated.models.agent_job_delete_data_response import (
    AgentJobDeleteDataResponse,
)
from roe._generated.models.agent_job_webhook_resend_response import (
    AgentJobWebhookResendResponse,
)
from roe._generated.models.agent_job_result_many_request import (
    AgentJobResultManyRequest,
)
from roe._generated.models.agent_job_result_item import AgentJobResultItem
from roe._generated.models.agent_job_result_response import AgentJobResultResponse
from roe._generated.models.agent_job_single_status import AgentJobSingleStatus
from roe._generated.models.agents_jobs_list_ordering_item import (
    AgentsJobsListOrderingItem,
)
from roe._generated.models.agent_job_status import AgentJobStatus
from roe._generated.models.agent_job_status_many_request import (
    AgentJobStatusManyRequest,
)
from roe._generated.models.agent_run_async_many_request import (
    AgentRunAsyncManyRequest,
)
from roe._generated.models.agent_version import AgentVersion
from roe._generated.models.agent_version_create_request import AgentVersionCreateRequest
from roe._generated.models.agent_version_update_request import AgentVersionUpdateRequest
from roe._generated.models.paginated_list_agent_job_list import (
    PaginatedListAgentJobList,
)
from roe._generated.models.base_agent import BaseAgent
from roe._generated.models.base_agent_create_request import BaseAgentCreateRequest
from roe._generated.models.base_agent_update_request import BaseAgentUpdateRequest
from roe._generated.models.message_response import MessageResponse
from roe._generated.models.paginated_base_agent_list import PaginatedBaseAgentList
from roe._generated.models.patched_base_agent_update_request import (
    PatchedBaseAgentUpdateRequest,
)
from roe._generated.models.patched_agent_version_update_request import (
    PatchedAgentVersionUpdateRequest,
)
from roe._generated.types import UNSET
from roe.config import RoeConfig
from roe.exceptions import RoeAPIException, translate_response
from roe.models.job import Job, JobBatch
from roe.utils._dynamic_call import call_dynamic
from roe.utils.generated_request import request_json, request_raw


def _build_run_headers(
    idempotency_key: str | None = None,
    skip_cache: bool = False,
) -> dict[str, str] | None:
    """Build the optional per-run request headers shared by the run methods."""
    headers: dict[str, str] = {}
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if skip_cache:
        headers["X-Skip-Cache"] = "true"
    return headers or None


def _build_aer(inputs: dict[str, Any]) -> AgentExecutionRequest:
    """Pack a free-form ``inputs`` dict into an ``AgentExecutionRequest``.

    Used for the JSON-only batch endpoint. The model's fixed fields are
    ignored; everything goes through ``additional_properties`` so the
    ``to_dict()`` serializer emits a flat ``{key: value}`` shape.
    """
    body = AgentExecutionRequest()
    for key, value in inputs.items():
        body.additional_properties[key] = value
    return body


class AgentVersionsAPI:
    """Nested API for agent version operations."""

    def __init__(self, agents_api: "AgentsAPI"):
        self._agents_api = agents_api

    @property
    def _raw(self) -> AuthenticatedClient:
        return self._agents_api._raw

    @property
    def _org_id(self) -> UUID:
        return UUID(str(self._agents_api.config.organization_id))

    def list(self, agent_id: str) -> list[AgentVersion]:
        response = request_raw(
            self._raw,
            agents_versions_list,
            UUID(str(agent_id)),
            organization_id=self._org_id,
        )
        data = response.json()
        if not isinstance(data, list):
            raise RoeAPIException(
                f"agent versions returned unexpected response shape: {data!r}"
            )
        return [AgentVersion.from_dict(item) for item in data]

    def retrieve(
        self, agent_id: str, version_id: str, get_supports_eval: bool | None = None
    ) -> AgentVersion:
        response = request_raw(
            self._raw,
            agents_versions_retrieve,
            UUID(str(agent_id)),
            UUID(str(version_id)),
            get_supports_eval=get_supports_eval
            if get_supports_eval is not None
            else UNSET,
            organization_id=self._org_id,
        )
        return AgentVersion.from_dict(response.json())

    def retrieve_current(self, agent_id: str) -> AgentVersion:
        response = request_raw(
            self._raw,
            agents_versions_current_retrieve,
            UUID(str(agent_id)),
            organization_id=self._org_id,
        )
        return AgentVersion.from_dict(response.json())

    def create(
        self,
        agent_id: str,
        input_definitions: list[dict[str, Any]] | None = None,
        engine_config: dict[str, Any] | None = None,
        version_name: str | None = None,
        description: str | None = None,
    ) -> AgentVersion:
        body = AgentVersionCreateRequest(
            input_definitions=input_definitions or [],
            engine_config=engine_config or {},
            version_name=version_name if version_name is not None else UNSET,
            description=description if description is not None else UNSET,
        )
        response = request_raw(
            self._raw,
            agents_versions_create,
            UUID(str(agent_id)),
            body=body,
            organization_id=self._org_id,
        )
        data = response.json()
        version_id = data.get("id") if isinstance(data, dict) else None
        if version_id is None:
            raise RoeAPIException(
                f"Unexpected response from server: status={response.status_code}"
            )
        # POST returns a partial create payload; re-fetch to get the full version.
        return self.retrieve(agent_id, str(version_id))

    def update(
        self,
        agent_id: str,
        version_id: str,
        version_name: str | None = None,
        description: str | None = None,
    ) -> None:
        """Update an agent version via PATCH (partial update)."""
        body = PatchedAgentVersionUpdateRequest(
            version_name=version_name if version_name is not None else UNSET,
            description=description if description is not None else UNSET,
        )
        request_json(
            self._raw,
            agents_versions_partial_update,
            UUID(str(agent_id)),
            UUID(str(version_id)),
            body=body,
            organization_id=self._org_id,
        )

    def replace(
        self,
        agent_id: str,
        version_id: str,
        version_name: str | None = None,
        description: str | None = None,
    ) -> MessageResponse:
        """Replace an agent version via PUT."""
        body = AgentVersionUpdateRequest(
            version_name=version_name if version_name is not None else UNSET,
            description=description if description is not None else UNSET,
        )
        resp = request_json(
            self._raw,
            agents_versions_update,
            UUID(str(agent_id)),
            UUID(str(version_id)),
            body=body,
            organization_id=self._org_id,
        )
        return resp.parsed  # type: ignore[return-value]

    def delete(self, agent_id: str, version_id: str) -> None:
        request_raw(
            self._raw,
            agents_versions_destroy,
            UUID(str(agent_id)),
            UUID(str(version_id)),
            organization_id=self._org_id,
        )


class AgentJobsAPI:
    """Nested API for agent job operations."""

    _MAX_BATCH_SIZE = 1000

    def __init__(self, agents_api: "AgentsAPI"):
        self._agents_api = agents_api

    @property
    def _raw(self) -> AuthenticatedClient:
        return self._agents_api._raw

    @property
    def _org_id(self) -> UUID:
        return UUID(str(self._agents_api.config.organization_id))

    @staticmethod
    def _iter_chunks(items, chunk_size: int):
        for i in range(0, len(items), chunk_size):
            yield items[i : i + chunk_size]

    def list(
        self,
        agent_id: str,
        page: int | None = None,
        page_size: int | None = None,
        status_code: str | None = None,
        version_name: str | None = None,
        metadata: str | None = None,
        created_from: str | None = None,
        created_to: str | None = None,
        search: str | None = None,
        ordering: str | None = None,
    ) -> PaginatedListAgentJobList:
        """List an agent's jobs (paginated), with filter and sort options."""
        response = request_raw(
            self._raw,
            agents_jobs_list,
            UUID(str(agent_id)),
            page=page if page is not None else UNSET,
            page_size=page_size if page_size is not None else UNSET,
            status_code=status_code if status_code is not None else UNSET,
            version_name=version_name if version_name is not None else UNSET,
            metadata=metadata if metadata is not None else UNSET,
            created_from=datetime.datetime.fromisoformat(created_from)
            if created_from is not None
            else UNSET,
            created_to=datetime.datetime.fromisoformat(created_to)
            if created_to is not None
            else UNSET,
            search=search if search is not None else UNSET,
            ordering=[AgentsJobsListOrderingItem(ordering)]
            if ordering is not None
            else UNSET,
            organization_id=self._org_id,
        )
        return PaginatedListAgentJobList.from_dict(response.json())

    def retrieve_status(self, job_id: str) -> AgentJobSingleStatus:
        response = request_raw(
            self._raw,
            agents_jobs_status_retrieve,
            UUID(str(job_id)),
            organization_id=self._org_id,
        )
        return AgentJobSingleStatus.from_dict(response.json())

    def retrieve_result(self, job_id: str) -> AgentJobResultResponse:
        response = request_raw(
            self._raw,
            agents_jobs_result_retrieve,
            UUID(str(job_id)),
            organization_id=self._org_id,
        )
        return AgentJobResultResponse.from_dict(response.json())

    def retrieve_status_many(self, job_ids: list[str]) -> list[AgentJobStatus]:
        results: list[AgentJobStatus] = []
        is_first_chunk = True
        for chunk in self._iter_chunks(job_ids, self._MAX_BATCH_SIZE):
            if not chunk:
                continue
            if not is_first_chunk:
                time.sleep(self._agents_api.config.batch_chunk_delay)
            is_first_chunk = False
            body = AgentJobStatusManyRequest(
                job_ids=[UUID(str(job_id)) for job_id in chunk]
            )
            resp = request_json(
                self._raw,
                agents_jobs_statuses_create,
                body=body,
                organization_id=self._org_id,
            )
            chunk_result = resp.parsed
            if chunk_result is not None:
                results.extend(chunk_result)
        return results

    def retrieve_result_many(
        self, job_ids: list[str]
    ) -> list[Any]:  # AgentJobResultItem
        results: list[Any] = []
        is_first_chunk = True
        for chunk in self._iter_chunks(job_ids, self._MAX_BATCH_SIZE):
            if not chunk:
                continue
            if not is_first_chunk:
                time.sleep(self._agents_api.config.batch_chunk_delay)
            is_first_chunk = False
            body = AgentJobResultManyRequest(
                job_ids=[UUID(str(job_id)) for job_id in chunk]
            )
            response = request_raw(
                self._raw,
                agents_jobs_results_create,
                body=body,
                organization_id=self._org_id,
            )
            data = response.json()
            items = data.get("results", []) if isinstance(data, dict) else data
            if not isinstance(items, list):
                raise RoeAPIException(
                    f"jobs/results returned unexpected response shape: {data!r}"
                )
            results.extend(AgentJobResultItem.from_dict(item) for item in items)
        return results

    def download_reference(
        self, job_id: str, resource_id: str, as_attachment: bool = False
    ) -> bytes:
        kwargs = agents_jobs_references_retrieve._get_kwargs(
            agent_job_id=UUID(str(job_id)),
            resource_id=resource_id,
        )
        if as_attachment:
            kwargs.setdefault("params", {})["download"] = "true"
        response = self._raw.get_httpx_client().request(**kwargs)
        translate_response(response)
        return response.content

    def retrieve_artifact(
        self, job_id: str, artifact_key: str
    ) -> AgentJobArtifactResult:
        response = request_raw(
            self._raw,
            agents_jobs_artifacts_result_retrieve,
            str(job_id),
            artifact_key=artifact_key,
            organization_id=self._org_id,
        )
        return AgentJobArtifactResult.from_dict(response.json())

    def cancel(self, job_id: str) -> None:
        request_raw(
            self._raw,
            agents_jobs_cancel_create,
            UUID(str(job_id)),
            organization_id=self._org_id,
        )

    def resend_webhook(
        self, job_id: str, webhook_id: str | None = None
    ) -> AgentJobWebhookResendResponse:
        """Re-send a finished job's completion webhook.

        Sends to every webhook attached to the job's agent, or only to
        ``webhook_id`` when given. The job is not re-run and its status is
        unchanged. ``queued`` reports how many deliveries were queued; zero
        means nothing was eligible.
        """
        body = ResendAgentJobWebhookRequest(
            webhook_id=UUID(str(webhook_id)) if webhook_id is not None else UNSET,
        )
        response = request_raw(
            self._raw,
            agents_jobs_webhook_resend_create,
            UUID(str(job_id)),
            body=body,
            organization_id=self._org_id,
        )
        return AgentJobWebhookResendResponse.from_dict(response.json())

    def cancel_all(self, agent_id: str) -> AgentJobCancelAllResponse:
        response = request_raw(
            self._raw,
            agents_jobs_cancel_all_create,
            UUID(str(agent_id)),
            organization_id=self._org_id,
        )
        return AgentJobCancelAllResponse.from_dict(response.json())

    def delete_data(self, job_id: str) -> AgentJobDeleteDataResponse:
        response = request_raw(
            self._raw,
            agents_jobs_delete_data_create,
            UUID(str(job_id)),
            organization_id=self._org_id,
        )
        return AgentJobDeleteDataResponse.from_dict(response.json())


class AgentsAPI:
    """API for managing and running agents."""

    _MAX_BATCH_SIZE = 1000

    def __init__(self, config: RoeConfig, raw_client: AuthenticatedClient):
        self.config = config
        self._raw = raw_client
        self._versions = AgentVersionsAPI(self)
        self._jobs = AgentJobsAPI(self)

    @property
    def _org_id(self) -> UUID:
        return UUID(str(self.config.organization_id))

    @property
    def versions(self) -> AgentVersionsAPI:
        return self._versions

    @property
    def jobs(self) -> AgentJobsAPI:
        return self._jobs

    @staticmethod
    def _iter_chunks(items, chunk_size: int):
        for i in range(0, len(items), chunk_size):
            yield items[i : i + chunk_size]

    def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedBaseAgentList:
        response = request_raw(
            self._raw,
            agents_list,
            page=page if page is not None else UNSET,
            page_size=page_size if page_size is not None else UNSET,
            organization_id=self._org_id,
        )
        return PaginatedBaseAgentList.from_dict(response.json())

    def retrieve(self, agent_id: str) -> BaseAgent:
        response = request_raw(
            self._raw,
            agents_retrieve,
            UUID(str(agent_id)),
            organization_id=self._org_id,
        )
        return BaseAgent.from_dict(response.json())

    def create(
        self,
        name: str,
        engine_class_id: str,
        input_definitions: list[dict[str, Any]] | None = None,
        engine_config: dict[str, Any] | None = None,
        version_name: str | None = None,
        description: str | None = None,
    ) -> BaseAgent:
        body = BaseAgentCreateRequest(
            name=name,
            engine_class_id=engine_class_id,
            organization_id=self._org_id,
            input_definitions=input_definitions or [],
            engine_config=engine_config or {},
            version_name=version_name if version_name is not None else UNSET,
            description=description if description is not None else UNSET,
        )
        resp = request_json(
            self._raw,
            agents_create,
            body=body,
            organization_id=self._org_id,
        )
        return resp.parsed  # type: ignore[return-value]

    def update(
        self,
        agent_id: str,
        name: str | None = None,
        disable_cache: bool | None = None,
        cache_failed_jobs: bool | None = None,
    ) -> BaseAgent:
        """Update an agent via PATCH (partial update)."""
        body = PatchedBaseAgentUpdateRequest(
            name=name if name is not None else UNSET,
            disable_cache=disable_cache if disable_cache is not None else UNSET,
            cache_failed_jobs=cache_failed_jobs
            if cache_failed_jobs is not None
            else UNSET,
        )
        resp = request_json(
            self._raw,
            agents_partial_update,
            UUID(str(agent_id)),
            body=body,
            organization_id=self._org_id,
        )
        return resp.parsed  # type: ignore[return-value]

    def replace(
        self,
        agent_id: str,
        name: str | None = None,
        disable_cache: bool | None = None,
        cache_failed_jobs: bool | None = None,
    ) -> BaseAgent:
        """Replace an agent via PUT."""
        body = BaseAgentUpdateRequest(
            name=name if name is not None else UNSET,
            disable_cache=disable_cache if disable_cache is not None else UNSET,
            cache_failed_jobs=cache_failed_jobs
            if cache_failed_jobs is not None
            else UNSET,
        )
        resp = request_json(
            self._raw,
            agents_update,
            UUID(str(agent_id)),
            body=body,
            organization_id=self._org_id,
        )
        return resp.parsed  # type: ignore[return-value]

    def delete(self, agent_id: str) -> None:
        request_raw(
            self._raw,
            agents_destroy,
            UUID(str(agent_id)),
            organization_id=self._org_id,
        )

    def duplicate(self, agent_id: str) -> AgentVersion:
        """Duplicate an agent. Returns the resulting ``AgentVersion``.

        The endpoint historically returned a JSON object with a ``base_agent``
        key wrapping the new agent; the generated client now models the
        response as ``AgentVersion`` directly. Callers wanting the new base
        agent should read ``result.base_agent`` (already populated).
        """
        response = request_raw(
            self._raw,
            agents_duplicate_create,
            UUID(str(agent_id)),
            organization_id=self._org_id,
        )
        return AgentVersion.from_dict(response.json())

    def run(
        self,
        agent_id: str,
        timeout_seconds: int | None = None,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
        skip_cache: bool = False,
        **inputs: Any,
    ) -> Job:
        """Run an agent asynchronously and return a ``Job`` handle.

        Set ``skip_cache=True`` to bypass the job-result cache and force a
        fresh run (the fresh result still refreshes the cache).
        """
        response = call_dynamic(
            self._raw,
            agents_run_async_create,
            inputs=inputs,
            metadata=metadata,
            organization_id=self._org_id,
            agent_id=UUID(str(agent_id)),
            extra_headers=_build_run_headers(idempotency_key, skip_cache),
        )
        job_id = response.json()
        if not isinstance(job_id, str):
            raise RoeAPIException(
                f"run_async returned unexpected job ID shape: {job_id!r}"
            )
        return Job(self, job_id, timeout_seconds)

    def run_many(
        self,
        agent_id: str,
        batch_inputs: list[dict[str, Any]],
        timeout_seconds: int | None = None,
        metadata: dict[str, Any] | None = None,
        skip_cache: bool = False,
    ) -> JobBatch:
        """Run an agent across many inputs (JSON body, no multipart).

        Set ``skip_cache=True`` to bypass the job-result cache and force
        fresh runs (the fresh results still refresh the cache).
        """
        all_job_ids: list[str] = []
        is_first_chunk = True
        for chunk in self._iter_chunks(batch_inputs, self._MAX_BATCH_SIZE):
            if not chunk:
                continue
            if not is_first_chunk:
                time.sleep(self.config.batch_chunk_delay)
            is_first_chunk = False
            body = AgentRunAsyncManyRequest(inputs=[_build_aer(item) for item in chunk])
            if metadata is not None:
                body.additional_properties["metadata"] = metadata
            response = request_raw(
                self._raw,
                agents_run_async_many,
                UUID(str(agent_id)),
                body=body,
                organization_id=self._org_id,
                extra_headers=_build_run_headers(skip_cache=skip_cache),
            )
            chunk_ids = response.json()
            if not isinstance(chunk_ids, list):
                raise RoeAPIException(
                    f"run_async_many returned unexpected response shape: {chunk_ids!r}"
                )
            for job_id in chunk_ids:
                if not isinstance(job_id, str):
                    raise RoeAPIException(
                        f"run_async_many returned invalid job ID: {job_id!r}"
                    )
                all_job_ids.append(job_id)
        return JobBatch(self, all_job_ids, timeout_seconds)

    def run_sync(
        self,
        agent_id: str,
        metadata: dict[str, Any] | None = None,
        skip_cache: bool = False,
        **inputs: Any,
    ) -> list[AgentDatum]:
        """Run an agent synchronously and return the outputs.

        Set ``skip_cache=True`` to bypass the job-result cache and force a
        fresh run (the fresh result still refreshes the cache).
        """
        response = call_dynamic(
            self._raw,
            agents_run,
            inputs=inputs,
            metadata=metadata,
            organization_id=self._org_id,
            agent_id=UUID(str(agent_id)),
            extra_headers=_build_run_headers(skip_cache=skip_cache),
        )
        return [AgentDatum.from_dict(d) for d in response.json()]

    def run_version(
        self,
        agent_id: str,
        version_id: str,
        timeout_seconds: int | None = None,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
        skip_cache: bool = False,
        **inputs: Any,
    ) -> Job:
        """Run a specific agent version asynchronously and return a ``Job``.

        Set ``skip_cache=True`` to bypass the job-result cache and force a
        fresh run (the fresh result still refreshes the cache).
        """
        response = call_dynamic(
            self._raw,
            agents_run_versions_async_create,
            inputs=inputs,
            metadata=metadata,
            organization_id=self._org_id,
            agent_id=UUID(str(agent_id)),
            agent_version_id=UUID(str(version_id)),
            extra_headers=_build_run_headers(idempotency_key, skip_cache),
        )
        job_id = response.json()
        if not isinstance(job_id, str):
            raise RoeAPIException(
                f"run_async returned unexpected job ID shape: {job_id!r}"
            )
        return Job(self, job_id, timeout_seconds)

    def run_version_sync(
        self,
        agent_id: str,
        version_id: str,
        metadata: dict[str, Any] | None = None,
        skip_cache: bool = False,
        **inputs: Any,
    ) -> list[AgentDatum]:
        """Run a specific agent version synchronously and return the outputs.

        Set ``skip_cache=True`` to bypass the job-result cache and force a
        fresh run (the fresh result still refreshes the cache).
        """
        response = call_dynamic(
            self._raw,
            agents_run_version,
            inputs=inputs,
            metadata=metadata,
            organization_id=self._org_id,
            agent_id=UUID(str(agent_id)),
            agent_version_id=UUID(str(version_id)),
            extra_headers=_build_run_headers(skip_cache=skip_cache),
        )
        return [AgentDatum.from_dict(d) for d in response.json()]
