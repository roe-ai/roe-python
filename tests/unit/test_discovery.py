"""Unit tests for the generated ``roe.api.discovery.DiscoveryAPI`` facade."""

from __future__ import annotations

from http import HTTPStatus
from unittest.mock import MagicMock, patch

import pytest

from roe._generated.models.agent_engine_type_list import AgentEngineTypeList
from roe._generated.models.supported_llm_model_list import SupportedLLMModelList
from roe._generated.types import UNSET, Response
from roe.api.discovery import DiscoveryAPI
from roe.exceptions import BadRequestError


ORG_ID = "00000000-0000-0000-0000-000000000000"


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
    payload = AgentEngineTypeList(
        engine_types=["ResearchEngine"], total_count=1, engines=[]
    )

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
    payload = SupportedLLMModelList(
        models=[], total_count=0, tenant_scope="all_tenants"
    )

    with patch(
        "roe.api.discovery.discovery_supported_models_list.sync_detailed",
        return_value=_response(payload),
    ) as mocked:
        result = api.list_supported_models(capability="image")

    mocked.assert_called_once_with(client=raw_client, capability="image")
    assert result.tenant_scope == "all_tenants"


def test_list_supported_models_translates_none_capability_to_unset():
    raw_client = MagicMock()
    api = DiscoveryAPI(MagicMock(), raw_client)
    payload = SupportedLLMModelList(
        models=[], total_count=0, tenant_scope="all_tenants"
    )

    with patch(
        "roe.api.discovery.discovery_supported_models_list.sync_detailed",
        return_value=_response(payload),
    ) as mocked:
        api.list_supported_models()

    mocked.assert_called_once_with(client=raw_client, capability=UNSET)


def test_list_supported_models_translates_bad_request():
    raw_client = MagicMock()
    api = DiscoveryAPI(MagicMock(), raw_client)

    with patch(
        "roe.api.discovery.discovery_supported_models_list.sync_detailed",
        return_value=_response(None, status=400),
    ):
        with pytest.raises(BadRequestError):
            api.list_supported_models(capability="spreadsheet")


def test_discovery_via_roe_client_generated_registry():
    payload = AgentEngineTypeList(
        engine_types=["ResearchEngine"], total_count=1, engines=[]
    )

    with patch(
        "roe.api.discovery.discovery_agent_engine_types_list.sync_detailed",
        return_value=_response(payload),
    ):
        from roe import RoeClient

        client = RoeClient(
            api_key="test-key",
            organization_id=ORG_ID,
            base_url="https://example.invalid",
        )
        try:
            result = client.discovery.list_agent_engine_types()
        finally:
            client.close()

    assert result.engine_types == ["ResearchEngine"]


def test_agent_engine_type_list_deserializes_public_engine_payload():
    backend_response = {
        "engine_types": ["ResearchEngine"],
        "total_count": 1,
        "engines": [
            {
                "class_id": "ResearchEngine",
                "display_name": "Research Engine",
                "description": "Researches things.",
                "summary": "Research workflow.",
                "input_schema": {"type": "object", "properties": {}},
                "default_values": {},
            }
        ],
    }

    parsed = AgentEngineTypeList.from_dict(backend_response)

    assert parsed.engine_types == ["ResearchEngine"]
    assert parsed.total_count == 1
    assert len(parsed.engines) == 1
    engine = parsed.engines[0]
    assert engine["class_id"] == "ResearchEngine"
    assert engine["display_name"] == "Research Engine"
    assert engine["input_schema"] == {"type": "object", "properties": {}}
    assert engine["default_values"] == {}


def test_supported_llm_model_list_deserializes_public_model_payload():
    backend_response = {
        "models": [
            {
                "id": "gpt-5",
                "providers": ["openai"],
                "capabilities": ["text"],
                "context_window": 200000,
                "max_output_tokens": 8192,
                "supports_system_message": True,
                "supports_temperature": True,
                "supports_reasoning_effort": False,
                "supports_json_output": True,
                "supports_json_schema": True,
            }
        ],
        "total_count": 1,
        "tenant_scope": "all_tenants",
    }

    parsed = SupportedLLMModelList.from_dict(backend_response)

    assert parsed.tenant_scope == "all_tenants"
    assert parsed.total_count == 1
    assert parsed.models[0].id == "gpt-5"
    assert parsed.models[0].capabilities == ["text"]
