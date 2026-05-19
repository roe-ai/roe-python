"""Unit tests for ``roe.api.discovery.DiscoveryAPI``."""

from __future__ import annotations

from http import HTTPStatus
from unittest.mock import MagicMock, patch

import pytest

from roe._generated.models.agent_engine_type_list import AgentEngineTypeList
from roe._generated.models.supported_llm_model_list import SupportedLLMModelList
from roe._generated.types import Response
from roe.api.discovery import DiscoveryAPI
from roe.exceptions import BadRequestError


def _response(parsed, status: int = 200) -> Response:
    return Response(
        status_code=HTTPStatus(status),
        content=b"{}",
        headers={},
        parsed=parsed,
    )


def test_list_agent_engine_types_calls_generated_endpoint():
    raw_client = MagicMock()
    api = DiscoveryAPI(MagicMock(), raw_client)
    payload = AgentEngineTypeList(engine_types=["ResearchEngine"], total_count=1, engines=[])

    with patch(
        "roe.api.discovery.discovery_agent_engine_types_list.sync_detailed",
        return_value=_response(payload),
    ) as mocked:
        result = api.list_agent_engine_types()

    mocked.assert_called_once_with(client=raw_client)
    assert result.engine_types == ["ResearchEngine"]


def test_list_supported_models_passes_capability_filter():
    raw_client = MagicMock()
    api = DiscoveryAPI(MagicMock(), raw_client)
    payload = SupportedLLMModelList(models=[], total_count=0, tenant_scope="all_tenants")

    with patch(
        "roe.api.discovery.discovery_supported_models_list.sync_detailed",
        return_value=_response(payload),
    ) as mocked:
        result = api.list_supported_models(capability="image")

    mocked.assert_called_once_with(client=raw_client, capability="image")
    assert result.tenant_scope == "all_tenants"


def test_list_supported_models_translates_bad_request():
    raw_client = MagicMock()
    api = DiscoveryAPI(MagicMock(), raw_client)

    with patch(
        "roe.api.discovery.discovery_supported_models_list.sync_detailed",
        return_value=_response(None, status=400),
    ):
        with pytest.raises(BadRequestError):
            api.list_supported_models(capability="spreadsheet")
