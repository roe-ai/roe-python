from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection_delete_error_response import ConnectionDeleteErrorResponse
from ...models.error_detail_response import ErrorDetailResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
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
        "url": "/v1/connections/{id}/".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ConnectionDeleteErrorResponse | ErrorDetailResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ConnectionDeleteErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ConnectionDeleteErrorResponse.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = ConnectionDeleteErrorResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ConnectionDeleteErrorResponse | ErrorDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | ConnectionDeleteErrorResponse | ErrorDetailResponse]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConnectionDeleteErrorResponse | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        id=id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Any | ConnectionDeleteErrorResponse | ErrorDetailResponse | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConnectionDeleteErrorResponse | ErrorDetailResponse
     """


    return sync_detailed(
        id=id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | ConnectionDeleteErrorResponse | ErrorDetailResponse]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConnectionDeleteErrorResponse | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        id=id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Any | ConnectionDeleteErrorResponse | ErrorDetailResponse | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConnectionDeleteErrorResponse | ErrorDetailResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
organization_id=organization_id,

    )).parsed
