from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dataset import Dataset
from ...models.dataset_create_request_request import DatasetCreateRequestRequest
from ...models.error_response import ErrorResponse
from typing import cast



def _get_kwargs(
    *,
    body:    DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/datasets/",
    }

    if isinstance(body, DatasetCreateRequestRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, DatasetCreateRequestRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, DatasetCreateRequestRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dataset | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = Dataset.from_dict(response.json())



        return response_201

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Dataset | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  | Unset = UNSET,

) -> Response[Dataset | ErrorResponse]:
    """ Create a new dataset.

     Create a new dataset.

    Args:
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dataset | ErrorResponse]
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
    body:    DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  | Unset = UNSET,

) -> Dataset | ErrorResponse | None:
    """ Create a new dataset.

     Create a new dataset.

    Args:
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dataset | ErrorResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  | Unset = UNSET,

) -> Response[Dataset | ErrorResponse]:
    """ Create a new dataset.

     Create a new dataset.

    Args:
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dataset | ErrorResponse]
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
    body:    DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  |     DatasetCreateRequestRequest  | Unset = UNSET,

) -> Dataset | ErrorResponse | None:
    """ Create a new dataset.

     Create a new dataset.

    Args:
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):
        body (DatasetCreateRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dataset | ErrorResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
