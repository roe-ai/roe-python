from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.database_query_result_retrieve_response import DatabaseQueryResultRetrieveResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    worksheet_query_id: UUID,
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
        "method": "get",
        "url": "/v1/database/query/{worksheet_query_id}/result/".format(worksheet_query_id=quote(str(worksheet_query_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DatabaseQueryResultRetrieveResponse | None:
    if response.status_code == 200:
        response_200 = DatabaseQueryResultRetrieveResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DatabaseQueryResultRetrieveResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    worksheet_query_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | DatabaseQueryResultRetrieveResponse]:
    """  Get the results of a query.

    Args:
        worksheet_query_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DatabaseQueryResultRetrieveResponse]
     """


    kwargs = _get_kwargs(
        worksheet_query_id=worksheet_query_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    worksheet_query_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Any | DatabaseQueryResultRetrieveResponse | None:
    """  Get the results of a query.

    Args:
        worksheet_query_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DatabaseQueryResultRetrieveResponse
     """


    return sync_detailed(
        worksheet_query_id=worksheet_query_id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    worksheet_query_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | DatabaseQueryResultRetrieveResponse]:
    """  Get the results of a query.

    Args:
        worksheet_query_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DatabaseQueryResultRetrieveResponse]
     """


    kwargs = _get_kwargs(
        worksheet_query_id=worksheet_query_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    worksheet_query_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Any | DatabaseQueryResultRetrieveResponse | None:
    """  Get the results of a query.

    Args:
        worksheet_query_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DatabaseQueryResultRetrieveResponse
     """


    return (await asyncio_detailed(
        worksheet_query_id=worksheet_query_id,
client=client,
organization_id=organization_id,

    )).parsed
