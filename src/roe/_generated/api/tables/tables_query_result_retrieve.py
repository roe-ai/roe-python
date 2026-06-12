from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.table_query_result_response import TableQueryResultResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_query_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tables/query/{table_query_id}/result/".format(table_query_id=quote(str(table_query_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorDetailResponse | TableQueryResultResponse | None:
    if response.status_code == 200:
        response_200 = TableQueryResultResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorDetailResponse | TableQueryResultResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_query_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorDetailResponse | TableQueryResultResponse]:
    """ Get a Roe table query result

     Poll or fetch one public Roe table query result.

    Args:
        table_query_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | TableQueryResultResponse]
     """


    kwargs = _get_kwargs(
        table_query_id=table_query_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_query_id: UUID,
    *,
    client: AuthenticatedClient,

) -> ErrorDetailResponse | TableQueryResultResponse | None:
    """ Get a Roe table query result

     Poll or fetch one public Roe table query result.

    Args:
        table_query_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | TableQueryResultResponse
     """


    return sync_detailed(
        table_query_id=table_query_id,
client=client,

    ).parsed

async def asyncio_detailed(
    table_query_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorDetailResponse | TableQueryResultResponse]:
    """ Get a Roe table query result

     Poll or fetch one public Roe table query result.

    Args:
        table_query_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | TableQueryResultResponse]
     """


    kwargs = _get_kwargs(
        table_query_id=table_query_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_query_id: UUID,
    *,
    client: AuthenticatedClient,

) -> ErrorDetailResponse | TableQueryResultResponse | None:
    """ Get a Roe table query result

     Poll or fetch one public Roe table query result.

    Args:
        table_query_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | TableQueryResultResponse
     """


    return (await asyncio_detailed(
        table_query_id=table_query_id,
client=client,

    )).parsed
