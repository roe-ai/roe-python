from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.table_query_request_request import TableQueryRequestRequest
from ...models.table_query_submit_response import TableQuerySubmitResponse
from typing import cast



def _get_kwargs(
    *,
    body: TableQueryRequestRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tables/query/",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TableQuerySubmitResponse | None:
    if response.status_code == 202:
        response_202 = TableQuerySubmitResponse.from_dict(response.json())



        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TableQuerySubmitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TableQueryRequestRequest,

) -> Response[TableQuerySubmitResponse]:
    """ Run a read-only Roe table query

     Run a read-only SQL query over public Roe tables.

    Args:
        body (TableQueryRequestRequest): Request payload for running a public Roe table query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TableQuerySubmitResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TableQueryRequestRequest,

) -> TableQuerySubmitResponse | None:
    """ Run a read-only Roe table query

     Run a read-only SQL query over public Roe tables.

    Args:
        body (TableQueryRequestRequest): Request payload for running a public Roe table query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TableQuerySubmitResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TableQueryRequestRequest,

) -> Response[TableQuerySubmitResponse]:
    """ Run a read-only Roe table query

     Run a read-only SQL query over public Roe tables.

    Args:
        body (TableQueryRequestRequest): Request payload for running a public Roe table query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TableQuerySubmitResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TableQueryRequestRequest,

) -> TableQuerySubmitResponse | None:
    """ Run a read-only Roe table query

     Run a read-only SQL query over public Roe tables.

    Args:
        body (TableQueryRequestRequest): Request payload for running a public Roe table query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TableQuerySubmitResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
