from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...types import File, FileTypes
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast



def _get_kwargs(
    file_str: str,
    *,
    page_range: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_range"] = page_range


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/datasets/files/{file_str}/download/".format(file_str=quote(str(file_str), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(
             payload = BytesIO(response.json())
        )



        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_str: str,
    *,
    client: AuthenticatedClient | Client,
    page_range: str | Unset = UNSET,

) -> Response[ErrorResponse | File]:
    """  Download a file by its file string identifier.

    Args:
        file_str (str):
        page_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
     """


    kwargs = _get_kwargs(
        file_str=file_str,
page_range=page_range,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    file_str: str,
    *,
    client: AuthenticatedClient | Client,
    page_range: str | Unset = UNSET,

) -> ErrorResponse | File | None:
    """  Download a file by its file string identifier.

    Args:
        file_str (str):
        page_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
     """


    return sync_detailed(
        file_str=file_str,
client=client,
page_range=page_range,

    ).parsed

async def asyncio_detailed(
    file_str: str,
    *,
    client: AuthenticatedClient | Client,
    page_range: str | Unset = UNSET,

) -> Response[ErrorResponse | File]:
    """  Download a file by its file string identifier.

    Args:
        file_str (str):
        page_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
     """


    kwargs = _get_kwargs(
        file_str=file_str,
page_range=page_range,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    file_str: str,
    *,
    client: AuthenticatedClient | Client,
    page_range: str | Unset = UNSET,

) -> ErrorResponse | File | None:
    """  Download a file by its file string identifier.

    Args:
        file_str (str):
        page_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
     """


    return (await asyncio_detailed(
        file_str=file_str,
client=client,
page_range=page_range,

    )).parsed
