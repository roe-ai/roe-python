from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.table_upload_request import TableUploadRequest
from ...models.table_upload_response import TableUploadResponse
from typing import cast



def _get_kwargs(
    *,
    body: TableUploadRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tables/upload/",
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | TableUploadResponse | None:
    if response.status_code == 201:
        response_201 = TableUploadResponse.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | TableUploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TableUploadRequest,

) -> Response[ErrorResponse | TableUploadResponse]:
    """ Upload a CSV as a Roe table

     Create a Roe table in the authenticated organization from an uploaded CSV file. Organization API
    keys are scoped to one organization; if organization_id is supplied, it must match that
    organization.

    Args:
        body (TableUploadRequest): Serializer for public CSV table uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TableUploadResponse]
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
    body: TableUploadRequest,

) -> ErrorResponse | TableUploadResponse | None:
    """ Upload a CSV as a Roe table

     Create a Roe table in the authenticated organization from an uploaded CSV file. Organization API
    keys are scoped to one organization; if organization_id is supplied, it must match that
    organization.

    Args:
        body (TableUploadRequest): Serializer for public CSV table uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TableUploadResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TableUploadRequest,

) -> Response[ErrorResponse | TableUploadResponse]:
    """ Upload a CSV as a Roe table

     Create a Roe table in the authenticated organization from an uploaded CSV file. Organization API
    keys are scoped to one organization; if organization_id is supplied, it must match that
    organization.

    Args:
        body (TableUploadRequest): Serializer for public CSV table uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TableUploadResponse]
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
    body: TableUploadRequest,

) -> ErrorResponse | TableUploadResponse | None:
    """ Upload a CSV as a Roe table

     Create a Roe table in the authenticated organization from an uploaded CSV file. Organization API
    keys are scoped to one organization; if organization_id is supplied, it must match that
    organization.

    Args:
        body (TableUploadRequest): Serializer for public CSV table uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TableUploadResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
