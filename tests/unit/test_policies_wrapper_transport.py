"""Regression tests for public policy wrapper transport behavior."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import UUID

import httpx

from roe.api.policies import PoliciesAPI

ORG_ID = "00000000-0000-0000-0000-000000000123"
POLICY_ID = "00000000-0000-0000-0000-000000000444"


def _api(response: httpx.Response) -> tuple[PoliciesAPI, MagicMock]:
    request = MagicMock(return_value=response)
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = SimpleNamespace(request=request)
    config = SimpleNamespace(organization_id=ORG_ID)
    return PoliciesAPI(config, raw_client), request


def _update_policy_json() -> dict[str, object]:
    return {
        "id": POLICY_ID,
        "name": "Policy",
        "organization_id": ORG_ID,
        "current_version_id": None,
        "created_at": "2025-01-01T00:00:00Z",
        "updated_at": "2025-01-01T00:00:00Z",
        "description": "desc",
    }


def test_policy_replace_uses_put_with_org_query_and_model_body():
    api, request = _api(httpx.Response(200, json=_update_policy_json()))

    result = api.replace(POLICY_ID, name="Policy", description="desc")

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "put"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {"name": "Policy", "description": "desc"}
    assert result.id == UUID(POLICY_ID)
