from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connections_list_response_400 import ConnectionsListResponse400
from ...models.error_detail_response import ErrorDetailResponse
from ...models.paginated_connection_list_list import PaginatedConnectionListList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    connector_type: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["connector_type"] = connector_type

    params["ordering"] = ordering

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connections/",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList | None:
    if response.status_code == 200:
        response_200 = PaginatedConnectionListList.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ConnectionsListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorDetailResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    connector_type: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList]:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        connector_type (str | Unset):
        ordering (str | Unset):
        organization_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList]
     """


    kwargs = _get_kwargs(
        connector_type=connector_type,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    connector_type: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList | None:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        connector_type (str | Unset):
        ordering (str | Unset):
        organization_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList
     """


    return sync_detailed(
        client=client,
connector_type=connector_type,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    connector_type: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList]:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        connector_type (str | Unset):
        ordering (str | Unset):
        organization_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList]
     """


    kwargs = _get_kwargs(
        connector_type=connector_type,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    connector_type: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList | None:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        connector_type (str | Unset):
        ordering (str | Unset):
        organization_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionsListResponse400 | ErrorDetailResponse | PaginatedConnectionListList
     """


    return (await asyncio_detailed(
        client=client,
connector_type=connector_type,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    )).parsed
