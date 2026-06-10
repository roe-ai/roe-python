from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.table_describe_response import TableDescribeResponse
from typing import cast



def _get_kwargs(
    table_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tables/{table_name}/describe/".format(table_name=quote(str(table_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorResponse | TableDescribeResponse | None:
    if response.status_code == 200:
        response_200 = TableDescribeResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorResponse | TableDescribeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ErrorResponse | TableDescribeResponse]:
    """ Describe a Roe table

     Return table metadata only for one Roe table in the authenticated organization, including columns
    and cheap ClickHouse metadata such as row count and the latest metadata-modification timestamp when
    available.

    Args:
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | TableDescribeResponse]
     """


    kwargs = _get_kwargs(
        table_name=table_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ErrorResponse | TableDescribeResponse | None:
    """ Describe a Roe table

     Return table metadata only for one Roe table in the authenticated organization, including columns
    and cheap ClickHouse metadata such as row count and the latest metadata-modification timestamp when
    available.

    Args:
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | TableDescribeResponse
     """


    return sync_detailed(
        table_name=table_name,
client=client,

    ).parsed

async def asyncio_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ErrorResponse | TableDescribeResponse]:
    """ Describe a Roe table

     Return table metadata only for one Roe table in the authenticated organization, including columns
    and cheap ClickHouse metadata such as row count and the latest metadata-modification timestamp when
    available.

    Args:
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | TableDescribeResponse]
     """


    kwargs = _get_kwargs(
        table_name=table_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ErrorResponse | TableDescribeResponse | None:
    """ Describe a Roe table

     Return table metadata only for one Roe table in the authenticated organization, including columns
    and cheap ClickHouse metadata such as row count and the latest metadata-modification timestamp when
    available.

    Args:
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | TableDescribeResponse
     """


    return (await asyncio_detailed(
        table_name=table_name,
client=client,

    )).parsed
