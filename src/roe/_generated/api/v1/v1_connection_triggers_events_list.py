from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_connection_trigger_event_list import PaginatedConnectionTriggerEventList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trigger_id: UUID,
    *,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connection-triggers/{trigger_id}/events/".format(trigger_id=quote(str(trigger_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedConnectionTriggerEventList | None:
    if response.status_code == 200:
        response_200 = PaginatedConnectionTriggerEventList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedConnectionTriggerEventList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[PaginatedConnectionTriggerEventList]:
    """  GET /connection-triggers/{trigger_id}/events/ -- List events for a trigger.

    Args:
        trigger_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConnectionTriggerEventList]
     """


    kwargs = _get_kwargs(
        trigger_id=trigger_id,
page=page,
page_size=page_size,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> PaginatedConnectionTriggerEventList | None:
    """  GET /connection-triggers/{trigger_id}/events/ -- List events for a trigger.

    Args:
        trigger_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConnectionTriggerEventList
     """


    return sync_detailed(
        trigger_id=trigger_id,
client=client,
page=page,
page_size=page_size,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[PaginatedConnectionTriggerEventList]:
    """  GET /connection-triggers/{trigger_id}/events/ -- List events for a trigger.

    Args:
        trigger_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConnectionTriggerEventList]
     """


    kwargs = _get_kwargs(
        trigger_id=trigger_id,
page=page,
page_size=page_size,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> PaginatedConnectionTriggerEventList | None:
    """  GET /connection-triggers/{trigger_id}/events/ -- List events for a trigger.

    Args:
        trigger_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConnectionTriggerEventList
     """


    return (await asyncio_detailed(
        trigger_id=trigger_id,
client=client,
page=page,
page_size=page_size,
organization_id=organization_id,

    )).parsed
