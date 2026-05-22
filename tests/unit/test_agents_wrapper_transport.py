"""Regression tests for SDK wrappers that MCP depends on directly."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import httpx
import pytest

from roe.api.agents import AgentsAPI
from roe.exceptions import NotFoundError

ORG_ID = "00000000-0000-0000-0000-000000000123"
AGENT_ID = "00000000-0000-0000-0000-000000000111"
VERSION_ID = "00000000-0000-0000-0000-000000000222"
JOB_ID = "00000000-0000-0000-0000-000000000333"


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
