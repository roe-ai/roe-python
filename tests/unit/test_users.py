"""Unit tests for ``roe.api.users.UsersAPI``."""

from __future__ import annotations

import json
from http import HTTPStatus
from unittest.mock import MagicMock, patch

from roe._generated.models.user_info import UserInfo
from roe._generated.types import Response
from roe.api.users import UsersAPI


def _fake_response(status: int, payload: dict) -> Response:
    body = json.dumps(payload).encode("utf-8")
    return Response(
        status_code=HTTPStatus(status),
        content=body,
        headers={},
        parsed=None,
    )


def test_users_me_returns_user_info():
    raw_client = MagicMock()
    config = MagicMock()
    api = UsersAPI(config, raw_client)

    payload = {
        "id": 42,
        "email": "jaden@roe-ai.com",
        "display_name": "Jaden",
        "first_name": "Jaden",
        "last_name": "Fix",
    }

    with patch(
        "roe.api.users.v1_users_current_user_retrieve.sync_detailed",
        return_value=_fake_response(200, payload),
    ) as mocked:
        user = api.me()

    mocked.assert_called_once_with(client=raw_client)
    assert isinstance(user, UserInfo)
    assert user.id == 42
    assert user.email == "jaden@roe-ai.com"
    assert user.display_name == "Jaden"
    assert user.first_name == "Jaden"
    assert user.last_name == "Fix"


def test_users_me_via_roe_client_property():
    """``RoeClient.users.me()`` should round-trip the same payload."""
    payload = {
        "id": 7,
        "email": "founder@roe-ai.com",
        "display_name": "Founder",
    }

    with patch(
        "roe.api.users.v1_users_current_user_retrieve.sync_detailed",
        return_value=_fake_response(200, payload),
    ):
        from roe import RoeClient

        client = RoeClient(
            api_key="test-key",
            organization_id="00000000-0000-0000-0000-000000000000",
            base_url="https://example.invalid",
        )
        try:
            user = client.users.me()
        finally:
            client.close()

    assert user.id == 7
    assert user.email == "founder@roe-ai.com"
    assert user.display_name == "Founder"
