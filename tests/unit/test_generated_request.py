from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import httpx

from roe.utils.generated_request import request_json


class _DictBodyEndpoint:
    @staticmethod
    def _get_kwargs(*, body, organization_id):
        return {
            "method": "post",
            "url": "/v1/connections/",
            "params": {"organization_id": str(organization_id)},
            "json": body.to_dict(),
            "headers": {"Content-Type": "application/json"},
        }

    @staticmethod
    def _build_response(*, client, response):
        return SimpleNamespace(parsed=response.json())


def test_request_json_accepts_plain_dict_body_before_generated_serialization():
    request = MagicMock(return_value=httpx.Response(200, json={"ok": True}))
    raw_client = MagicMock()
    raw_client.get_httpx_client.return_value = SimpleNamespace(request=request)

    result = request_json(
        raw_client,
        _DictBodyEndpoint,
        body={"connector_type": "salesforce", "config": {"domain": "example"}},
        organization_id="00000000-0000-0000-0000-000000000000",
    )

    assert result.parsed == {"ok": True}
    assert request.call_args.kwargs["json"] == {
        "connector_type": "salesforce",
        "config": {"domain": "example"},
    }
