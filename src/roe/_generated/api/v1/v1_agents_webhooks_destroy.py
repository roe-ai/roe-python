from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    webhook_id: UUID,
    *,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/agents/{agent_id}/webhooks/{webhook_id}/".format(agent_id=quote(str(agent_id), safe=""),webhook_id=quote(str(webhook_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any]:
    """  Retrieve, update, or delete an agent webhook subscription.

    URL uses the Webhook ID (not subscription ID) for a more intuitive API.
    PATCH allows updating is_active status.
    DELETE removes the webhook from the agent.

    Args:
        agent_id (UUID):
        webhook_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
webhook_id=webhook_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    agent_id: UUID,
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any]:
    """  Retrieve, update, or delete an agent webhook subscription.

    URL uses the Webhook ID (not subscription ID) for a more intuitive API.
    PATCH allows updating is_active status.
    DELETE removes the webhook from the agent.

    Args:
        agent_id (UUID):
        webhook_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
webhook_id=webhook_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

