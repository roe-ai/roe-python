from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.file_import import FileImport
from ...models.file_import_request import FileImportRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body:    FileImportRequest  |     FileImportRequest  |     FileImportRequest  | Unset = UNSET,
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
        "url": "/v1/database/table/import/file/",
        "params": params,
    }

    if isinstance(body, FileImportRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, FileImportRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FileImportRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FileImport | None:
    if response.status_code == 200:
        response_200 = FileImport.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FileImport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    FileImportRequest  |     FileImportRequest  |     FileImportRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[FileImport]:
    """  Import a file (CSV or Parquet) into a table.

    Args:
        organization_id (UUID | Unset):
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileImport]
     """


    kwargs = _get_kwargs(
        body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body:    FileImportRequest  |     FileImportRequest  |     FileImportRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> FileImport | None:
    """  Import a file (CSV or Parquet) into a table.

    Args:
        organization_id (UUID | Unset):
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileImport
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    FileImportRequest  |     FileImportRequest  |     FileImportRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[FileImport]:
    """  Import a file (CSV or Parquet) into a table.

    Args:
        organization_id (UUID | Unset):
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileImport]
     """


    kwargs = _get_kwargs(
        body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body:    FileImportRequest  |     FileImportRequest  |     FileImportRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> FileImport | None:
    """  Import a file (CSV or Parquet) into a table.

    Args:
        organization_id (UUID | Unset):
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).
        body (FileImportRequest): Serializer for file import (CSV or Parquet).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileImport
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
