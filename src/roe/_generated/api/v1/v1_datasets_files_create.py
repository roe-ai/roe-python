from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.file import File
from ...models.file_upload_request_request import FileUploadRequestRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    dataset_id: UUID,
    *,
    body:    FileUploadRequestRequest  |     FileUploadRequestRequest  |     FileUploadRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/datasets/{dataset_id}/files/".format(dataset_id=quote(str(dataset_id), safe=""),),
        "params": params,
    }

    if isinstance(body, FileUploadRequestRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, FileUploadRequestRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FileUploadRequestRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())



        return response_403

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
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    FileUploadRequestRequest  |     FileUploadRequestRequest  |     FileUploadRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | File]:
    """  Upload a file to a dataset.

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
     """


    kwargs = _get_kwargs(
        dataset_id=dataset_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    FileUploadRequestRequest  |     FileUploadRequestRequest  |     FileUploadRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | File | None:
    """  Upload a file to a dataset.

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
     """


    return sync_detailed(
        dataset_id=dataset_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    FileUploadRequestRequest  |     FileUploadRequestRequest  |     FileUploadRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | File]:
    """  Upload a file to a dataset.

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
     """


    kwargs = _get_kwargs(
        dataset_id=dataset_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    FileUploadRequestRequest  |     FileUploadRequestRequest  |     FileUploadRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | File | None:
    """  Upload a file to a dataset.

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):
        body (FileUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
     """


    return (await asyncio_detailed(
        dataset_id=dataset_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
