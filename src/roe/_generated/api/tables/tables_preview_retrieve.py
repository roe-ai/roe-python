from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.table_preview_response import TablePreviewResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    table_name: str,
    *,
    limit: int | Unset = 3,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tables/{table_name}/preview/".format(table_name=quote(str(table_name), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorResponse | TablePreviewResponse | None:
    if response.status_code == 200:
        response_200 = TablePreviewResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorResponse | TablePreviewResponse]:
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
    limit: int | Unset = 3,

) -> Response[Any | ErrorResponse | TablePreviewResponse]:
    """ Preview a Roe table

     Return column metadata plus a bounded sample of rows from one Roe table in the authenticated
    organization.

    Args:
        table_name (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | TablePreviewResponse]
     """


    kwargs = _get_kwargs(
        table_name=table_name,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 3,

) -> Any | ErrorResponse | TablePreviewResponse | None:
    """ Preview a Roe table

     Return column metadata plus a bounded sample of rows from one Roe table in the authenticated
    organization.

    Args:
        table_name (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | TablePreviewResponse
     """


    return sync_detailed(
        table_name=table_name,
client=client,
limit=limit,

    ).parsed

async def asyncio_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 3,

) -> Response[Any | ErrorResponse | TablePreviewResponse]:
    """ Preview a Roe table

     Return column metadata plus a bounded sample of rows from one Roe table in the authenticated
    organization.

    Args:
        table_name (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | TablePreviewResponse]
     """


    kwargs = _get_kwargs(
        table_name=table_name,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 3,

) -> Any | ErrorResponse | TablePreviewResponse | None:
    """ Preview a Roe table

     Return column metadata plus a bounded sample of rows from one Roe table in the authenticated
    organization.

    Args:
        table_name (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | TablePreviewResponse
     """


    return (await asyncio_detailed(
        table_name=table_name,
client=client,
limit=limit,

    )).parsed
