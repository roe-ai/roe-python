from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.import_roe_dataset_request import ImportRoeDatasetRequest
from ...models.import_roe_dataset_request_request import ImportRoeDatasetRequestRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body:    ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  | Unset = UNSET,
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
        "url": "/v1/database/table/import/roe-dataset/",
        "params": params,
    }

    if isinstance(body, ImportRoeDatasetRequestRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, ImportRoeDatasetRequestRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ImportRoeDatasetRequestRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ImportRoeDatasetRequest | None:
    if response.status_code == 200:
        response_200 = ImportRoeDatasetRequest.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ImportRoeDatasetRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ImportRoeDatasetRequest]:
    """  Import dataset into database table.

    Args:
        organization_id (UUID | Unset):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportRoeDatasetRequest]
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
    body:    ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ImportRoeDatasetRequest | None:
    """  Import dataset into database table.

    Args:
        organization_id (UUID | Unset):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportRoeDatasetRequest
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ImportRoeDatasetRequest]:
    """  Import dataset into database table.

    Args:
        organization_id (UUID | Unset):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportRoeDatasetRequest]
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
    body:    ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  |     ImportRoeDatasetRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ImportRoeDatasetRequest | None:
    """  Import dataset into database table.

    Args:
        organization_id (UUID | Unset):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):
        body (ImportRoeDatasetRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportRoeDatasetRequest
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
