"""Regression tests for public connection wrapper transport behavior."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import UUID

import httpx

from roe.api.connections import ConnectionsAPI

ORG_ID = "00000000-0000-0000-0000-000000000123"
CONNECTION_ID = "00000000-0000-0000-0000-000000000555"


def _connection_json() -> dict[str, object]:
    return {
        "id": CONNECTION_ID,
        "user": None,
        "organization": ORG_ID,
        "connector_type": "salesforce",
        "connector_display_name": "Salesforce",
        "name": "CRM",
        "auth_config": {},
        "created_at": "2025-01-01T00:00:00Z",
        "updated_at": "2025-01-01T00:00:00Z",
        "description": "desc",
        "config": {"region": "us"},
        "credentials_configured": True,
        "dynamic_inputs": {},
        "dynamic_input_test_disabled_reason": None,
        "status": "active",
    }


def _api(response: httpx.Response) -> tuple[ConnectionsAPI, MagicMock]:
    request = MagicMock(return_value=response)
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = SimpleNamespace(request=request)
    config = SimpleNamespace(organization_id=ORG_ID)
    return ConnectionsAPI(config, raw_client), request


def test_connection_create_keeps_org_id_in_body_and_query():
    api, request = _api(httpx.Response(201, json=_connection_json()))

    result = api.create(
        connector_type="salesforce",
        name="CRM",
        config={"region": "us"},
    )

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "post"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {
        "organization_id": ORG_ID,
        "connector_type": "salesforce",
        "name": "CRM",
        "config": {"region": "us"},
    }
    assert result.id == UUID(CONNECTION_ID)


def test_connection_update_keeps_org_id_out_of_patch_body():
    api, request = _api(httpx.Response(200, json=_connection_json()))

    result = api.update(
        CONNECTION_ID,
        name="CRM",
        config={"region": "us"},
    )

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "patch"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {"name": "CRM", "config": {"region": "us"}}
    assert result.id == UUID(CONNECTION_ID)


def test_connection_replace_keeps_org_id_out_of_put_body():
    api, request = _api(httpx.Response(200, json=_connection_json()))

    result = api.replace(
        CONNECTION_ID,
        name="CRM",
        config={"region": "us"},
    )

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "put"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {"name": "CRM", "config": {"region": "us"}}
    assert result.id == UUID(CONNECTION_ID)
