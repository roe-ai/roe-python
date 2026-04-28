from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_connection_trigger_list import PaginatedConnectionTriggerList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    agent_id: str | Unset = UNSET,
    connection_id: str | Unset = UNSET,
    drive_name: str | Unset = UNSET,
    organization_id: str,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["agent_id"] = agent_id

    params["connection_id"] = connection_id

    params["drive_name"] = drive_name

    params["organization_id"] = organization_id

    params["page"] = page

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connection-triggers/",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedConnectionTriggerList | None:
    if response.status_code == 200:
        response_200 = PaginatedConnectionTriggerList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedConnectionTriggerList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    connection_id: str | Unset = UNSET,
    drive_name: str | Unset = UNSET,
    organization_id: str,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[PaginatedConnectionTriggerList]:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        agent_id (str | Unset):
        connection_id (str | Unset):
        drive_name (str | Unset):
        organization_id (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConnectionTriggerList]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
connection_id=connection_id,
drive_name=drive_name,
organization_id=organization_id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    connection_id: str | Unset = UNSET,
    drive_name: str | Unset = UNSET,
    organization_id: str,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> PaginatedConnectionTriggerList | None:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        agent_id (str | Unset):
        connection_id (str | Unset):
        drive_name (str | Unset):
        organization_id (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConnectionTriggerList
     """


    return sync_detailed(
        client=client,
agent_id=agent_id,
connection_id=connection_id,
drive_name=drive_name,
organization_id=organization_id,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    connection_id: str | Unset = UNSET,
    drive_name: str | Unset = UNSET,
    organization_id: str,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[PaginatedConnectionTriggerList]:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        agent_id (str | Unset):
        connection_id (str | Unset):
        drive_name (str | Unset):
        organization_id (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConnectionTriggerList]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
connection_id=connection_id,
drive_name=drive_name,
organization_id=organization_id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    connection_id: str | Unset = UNSET,
    drive_name: str | Unset = UNSET,
    organization_id: str,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> PaginatedConnectionTriggerList | None:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        agent_id (str | Unset):
        connection_id (str | Unset):
        drive_name (str | Unset):
        organization_id (str):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConnectionTriggerList
     """


    return (await asyncio_detailed(
        client=client,
agent_id=agent_id,
connection_id=connection_id,
drive_name=drive_name,
organization_id=organization_id,
page=page,
page_size=page_size,

    )).parsed
