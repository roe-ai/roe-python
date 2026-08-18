"""Regression tests for public SDK wrapper transport behavior."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import UUID

import httpx
import pytest

from roe.api.agents import AgentsAPI
from roe.exceptions import NotFoundError

ORG_ID = "00000000-0000-0000-0000-000000000123"
AGENT_ID = "00000000-0000-0000-0000-000000000111"
VERSION_ID = "00000000-0000-0000-0000-000000000222"
JOB_ID = "00000000-0000-0000-0000-000000000333"


def _base_agent_json() -> dict[str, object]:
    return {
        "id": AGENT_ID,
        "created_at": "2025-01-01T00:00:00Z",
        "updated_at": "2025-01-01T00:00:00Z",
        "name": "Agent",
        "disable_cache": False,
        "cache_failed_jobs": False,
        "organization_id": ORG_ID,
        "engine_class_id": "engine",
        "current_version_id": VERSION_ID,
        "job_count": None,
        "most_recent_job": None,
        "engine_name": "Engine",
        "tags": [],
    }


def _api(response: httpx.Response) -> tuple[AgentsAPI, MagicMock]:
    request = MagicMock(return_value=response)
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = SimpleNamespace(request=request)
    config = SimpleNamespace(organization_id=ORG_ID, batch_chunk_delay=0)
    return AgentsAPI(config, raw_client), request


def test_agent_version_retrieve_404_uses_sdk_error_not_generated_error_parser():
    api, _ = _api(
        httpx.Response(404, json={"detail": "No Agent matches the given query."})
    )

    with pytest.raises(NotFoundError) as exc_info:
        api.versions.retrieve(AGENT_ID, VERSION_ID)

    assert exc_info.value.message == "No Agent matches the given query."


def test_job_cancel_404_uses_sdk_error_not_generated_error_parser():
    api, _ = _api(httpx.Response(404, json={"detail": "No AgentJob found."}))

    with pytest.raises(NotFoundError) as exc_info:
        api.jobs.cancel(JOB_ID)

    assert exc_info.value.message == "No AgentJob found."


def test_run_passes_idempotency_key_through_dynamic_wrapper():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    job = api.run(AGENT_ID, idempotency_key="idem-123", prompt="hello")

    kwargs = request.call_args.kwargs
    assert kwargs["headers"]["Idempotency-Key"] == "idem-123"
    assert kwargs["headers"]["x-roe-skip-retry"] == "1"
    assert job.id == JOB_ID


def test_run_passes_skip_cache_header_through_dynamic_wrapper():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    job = api.run(AGENT_ID, skip_cache=True, prompt="hello")

    kwargs = request.call_args.kwargs
    assert kwargs["headers"]["X-Skip-Cache"] == "true"
    assert job.id == JOB_ID


def test_run_omits_skip_cache_header_by_default():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run(AGENT_ID, prompt="hello")

    kwargs = request.call_args.kwargs
    assert "X-Skip-Cache" not in kwargs["headers"]


def test_run_sync_passes_skip_cache_header():
    api, request = _api(httpx.Response(200, json=[]))

    api.run_sync(AGENT_ID, skip_cache=True, prompt="hello")

    kwargs = request.call_args.kwargs
    assert kwargs["headers"]["X-Skip-Cache"] == "true"


def test_run_version_passes_skip_cache_and_idempotency_headers():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run_version(
        AGENT_ID,
        VERSION_ID,
        idempotency_key="idem-456",
        skip_cache=True,
        prompt="hello",
    )

    kwargs = request.call_args.kwargs
    assert kwargs["headers"]["Idempotency-Key"] == "idem-456"
    assert kwargs["headers"]["X-Skip-Cache"] == "true"


def test_run_version_sync_passes_skip_cache_header():
    api, request = _api(httpx.Response(200, json=[]))

    api.run_version_sync(AGENT_ID, VERSION_ID, skip_cache=True, prompt="hello")

    kwargs = request.call_args.kwargs
    assert kwargs["headers"]["X-Skip-Cache"] == "true"


def test_run_many_passes_skip_cache_header_on_json_batch():
    api, request = _api(httpx.Response(200, json=[JOB_ID]))

    batch = api.run_many(AGENT_ID, [{"prompt": "hello"}], skip_cache=True)

    kwargs = request.call_args.kwargs
    assert kwargs["headers"]["X-Skip-Cache"] == "true"
    assert kwargs["headers"]["Content-Type"] == "application/json"
    assert batch.job_ids == [JOB_ID]


def test_run_many_omits_skip_cache_header_by_default():
    api, request = _api(httpx.Response(200, json=[JOB_ID]))

    api.run_many(AGENT_ID, [{"prompt": "hello"}])

    kwargs = request.call_args.kwargs
    assert "X-Skip-Cache" not in kwargs["headers"]


def test_run_many_sends_skip_cache_header_on_every_chunk():
    api, request = _api(httpx.Response(200, json=[JOB_ID]))

    api.run_many(AGENT_ID, [{"prompt": "hello"}] * 1001, skip_cache=True)

    assert request.call_count == 2
    for call in request.call_args_list:
        assert call.kwargs["headers"]["X-Skip-Cache"] == "true"


def test_sync_and_version_runs_omit_skip_cache_header_by_default():
    api, request = _api(httpx.Response(200, json=[]))

    api.run_sync(AGENT_ID, prompt="hello")
    api.run_version_sync(AGENT_ID, VERSION_ID, prompt="hello")

    for call in request.call_args_list:
        assert "X-Skip-Cache" not in call.kwargs["headers"]


def test_run_version_omits_skip_cache_header_by_default():
    api, request = _api(httpx.Response(200, json=JOB_ID))

    api.run_version(AGENT_ID, VERSION_ID, prompt="hello")

    kwargs = request.call_args.kwargs
    assert "X-Skip-Cache" not in kwargs["headers"]


def test_agent_replace_uses_put_with_org_query_and_model_body():
    api, request = _api(httpx.Response(200, json=_base_agent_json()))

    result = api.replace(AGENT_ID, name="Renamed", disable_cache=True)

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "put"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {"name": "Renamed", "disable_cache": True}
    assert result.id == UUID(AGENT_ID)


def test_agent_version_replace_uses_put_with_org_query_and_model_body():
    api, request = _api(httpx.Response(200, json={"message": "ok"}))

    result = api.versions.replace(
        AGENT_ID,
        VERSION_ID,
        version_name="v2",
        description="desc",
    )

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "put"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {"version_name": "v2", "description": "desc"}
    assert result.message == "ok"


def test_jobs_list_sends_filters_and_parses_paginated_response():
    api, request = _api(httpx.Response(200, json={"count": 0, "results": []}))

    result = api.jobs.list(
        AGENT_ID,
        page=2,
        page_size=10,
        status_code="4",
        created_from="2026-01-01T00:00:00+00:00",
        ordering="-created_at",
    )

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "get"
    params = kwargs["params"]
    assert params["organization_id"] == ORG_ID
    assert params["page"] == 2
    assert params["page_size"] == 10
    assert params["status_code"] == "4"
    # created_from is accepted as an ISO string and serialized back to ISO
    assert params["created_from"] == "2026-01-01T00:00:00+00:00"
    assert params["ordering"] == ["-created_at"]
    assert "version_name" not in params
    assert AGENT_ID in kwargs["url"]
    assert result.count == 0


def test_download_reference_omits_organization_id_query_param():
    # The references endpoint dropped organization_id; the wrapper must not send
    # it, or _get_kwargs raises TypeError (org is derived from the job).
    api, request = _api(httpx.Response(200, content=b"file-bytes"))

    content = api.jobs.download_reference(JOB_ID, "resource-1")

    kwargs = request.call_args.kwargs
    assert "organization_id" not in (kwargs.get("params") or {})
    assert content == b"file-bytes"


def test_retrieve_artifact_sends_artifact_key_and_org_query():
    api, request = _api(httpx.Response(200, json={"result": {"value": 1}}))

    result = api.jobs.retrieve_artifact(JOB_ID, artifact_key="evidence_data")

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "get"
    assert kwargs["params"]["artifact_key"] == "evidence_data"
    assert kwargs["params"]["organization_id"] == ORG_ID
    assert JOB_ID in kwargs["url"]
    assert result.result == {"value": 1}


def test_cancel_all_returns_structured_response_body():
    api, request = _api(
        httpx.Response(
            200,
            json={"task_id": "task-1", "targeted_count": 3, "note": "cancelling"},
        )
    )

    result = api.jobs.cancel_all(AGENT_ID)

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "post"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert result.targeted_count == 3
    assert result.note == "cancelling"


def test_resend_webhook_posts_to_the_job_and_returns_queued_count():
    api, request = _api(httpx.Response(200, json={"status": "queued", "queued": 2}))

    result = api.jobs.resend_webhook(JOB_ID)

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "post"
    assert kwargs["url"].endswith(f"/v1/agents/jobs/{JOB_ID}/webhook/resend/")
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert result.queued == 2


def test_retrieve_status_parses_single_status_shape_without_id():
    # GET /v1/agents/jobs/{job_id}/status/ returns AgentJobSingleStatus
    # ({status, timestamp, error_message?}) with no "id" field — parsing it
    # with the batch AgentJobStatus model raises KeyError("id").
    api, _ = _api(
        httpx.Response(
            200,
            json={
                "status": 4,
                "timestamp": 1781211849.964229,
                "error_message": "boom",
            },
        )
    )

    status = api.jobs.retrieve_status(JOB_ID)

    assert status.status == 4
    assert status.timestamp == pytest.approx(1781211849.964229)
    assert status.error_message == "boom"
