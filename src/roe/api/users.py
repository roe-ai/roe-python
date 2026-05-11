"""Users API — thin facade over the generated raw client.

Wraps ``GET /v1/users/current_user/`` and returns the parsed ``UserInfo``
model. Non-2xx responses are translated to the typed ``RoeAPIException``
family at the wrapper boundary.
"""

from __future__ import annotations

import json as _json

from roe._generated.api.users import users_current_user_retrieve
from roe._generated.client import AuthenticatedClient
from roe._generated.models.user_info import UserInfo
from roe.config import RoeConfig
from roe.exceptions import RoeAPIException, translate_response


class UsersAPI:
    """API for retrieving information about the authenticated user."""

    def __init__(self, config: RoeConfig, raw_client: AuthenticatedClient):
        self.config = config
        self._raw = raw_client

    def me(self) -> UserInfo:
        """Return the currently-authenticated user."""
        response = users_current_user_retrieve.sync_detailed(client=self._raw)
        translate_response(response)
        content = response.content or b""
        try:
            data = _json.loads(content.decode("utf-8")) if content else {}
        except (ValueError, UnicodeDecodeError) as exc:
            raise RoeAPIException(
                f"current_user returned non-JSON body: {content!r}"
            ) from exc
        if not isinstance(data, dict):
            raise RoeAPIException(
                f"current_user returned unexpected response shape: {data!r}"
            )
        return UserInfo.from_dict(data)
