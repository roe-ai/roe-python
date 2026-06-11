from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.table_preview_response import TablePreviewResponse
from ...models.tables_preview_retrieve_response_400_type_1 import TablesPreviewRetrieveResponse400Type1
from ...models.tables_preview_retrieve_response_400_type_2 import TablesPreviewRetrieveResponse400Type2
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2 | None:
    if response.status_code == 200:
        response_200 = TablePreviewResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        def _parse_response_400(data: object) -> list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_400_type_0 = cast(list[str], data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_1 = TablesPreviewRetrieveResponse400Type1.from_dict(data)



                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = TablesPreviewRetrieveResponse400Type2.from_dict(data)



            return response_400_type_2

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 3,

) -> Response[ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2]:
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
        Response[ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2]
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
    client: AuthenticatedClient,
    limit: int | Unset = 3,

) -> ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2 | None:
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
        ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2
     """


    return sync_detailed(
        table_name=table_name,
client=client,
limit=limit,

    ).parsed

async def asyncio_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 3,

) -> Response[ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2]:
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
        Response[ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2]
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
    client: AuthenticatedClient,
    limit: int | Unset = 3,

) -> ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2 | None:
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
        ErrorDetailResponse | TablePreviewResponse | list[str] | TablesPreviewRetrieveResponse400Type1 | TablesPreviewRetrieveResponse400Type2
     """


    return (await asyncio_detailed(
        table_name=table_name,
client=client,
limit=limit,

    )).parsed
