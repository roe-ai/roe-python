"""Regression tests for public knowledge base wrapper transport behavior."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import UUID

import httpx

from roe.api.knowledge_base import KnowledgeBaseAPI

ORG_ID = "00000000-0000-0000-0000-000000000123"
KB_ID = "00000000-0000-0000-0000-000000000444"


def _api(response: httpx.Response) -> tuple[KnowledgeBaseAPI, MagicMock]:
    request = MagicMock(return_value=response)
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = SimpleNamespace(request=request)
    config = SimpleNamespace(organization_id=ORG_ID)
    return KnowledgeBaseAPI(config, raw_client), request


def _draft_json() -> dict[str, object]:
    return {
        "id": "draft-1",
        "status": "ready",
        "company": "Acme",
        "suggestedName": "Acme Lens",
        "productSummary": "summary",
        "iterationCount": 1,
        "refs": [],
    }


def test_create_posts_body_with_org_query():
    api, request = _api(
        httpx.Response(201, json={"company": "Acme", "brief": "a long enough brief"})
    )

    result = api.create(company="Acme", brief="a long enough brief")

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "post"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {"company": "Acme", "brief": "a long enough brief"}
    assert result.company == "Acme"


def test_list_sends_pagination_and_org_query():
    api, request = _api(httpx.Response(200, json={"count": 0, "results": []}))

    result = api.list(page=2, page_size=10)

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "get"
    assert kwargs["params"] == {
        "page": 2,
        "page_size": 10,
        "organization_id": ORG_ID,
    }
    assert result.count == 0


def test_patch_selection_round_trips_refs_in_body():
    api, request = _api(httpx.Response(200, json=_draft_json()))

    refs = [{"typologyId": "t1", "relevance": "core"}]
    api.patch_selection(KB_ID, refs=refs, suggested_name="Acme Lens")

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "patch"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["json"] == {"refs": refs, "suggested_name": "Acme Lens"}


def test_delete_sends_delete_with_org_query_and_no_body():
    api, request = _api(httpx.Response(204))

    assert api.delete(KB_ID) is None

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "delete"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert "json" not in kwargs
    # path-arg is interpolated into the URL, not sent as a query param
    assert UUID(KB_ID).hex in kwargs["url"].replace("-", "")


def test_unlink_sends_delete_to_unlink_endpoint_with_org_query():
    api, request = _api(httpx.Response(204))

    assert api.unlink(KB_ID) is None

    kwargs = request.call_args.kwargs
    assert kwargs["method"] == "delete"
    assert kwargs["params"] == {"organization_id": ORG_ID}
    assert kwargs["url"].endswith(f"/v1/knowledge-base/{KB_ID}/unlink/")
