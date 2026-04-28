from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.worksheet_query import WorksheetQuery
from ...models.worksheet_query_create_request import WorksheetQueryCreateRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body:    WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  | Unset = UNSET,
    worksheet_id: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["worksheet_id"] = worksheet_id

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/database/query/async/",
        "params": params,
    }

    if isinstance(body, WorksheetQueryCreateRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, WorksheetQueryCreateRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, WorksheetQueryCreateRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | WorksheetQuery | None:
    if response.status_code == 200:
        response_200 = WorksheetQuery.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | WorksheetQuery]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  | Unset = UNSET,
    worksheet_id: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | WorksheetQuery]:
    """  Execute a query asynchronously and return query object.

    Args:
        worksheet_id (str | Unset):
        organization_id (UUID | Unset):
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorksheetQuery]
     """


    kwargs = _get_kwargs(
        body=body,
worksheet_id=worksheet_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body:    WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  | Unset = UNSET,
    worksheet_id: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | WorksheetQuery | None:
    """  Execute a query asynchronously and return query object.

    Args:
        worksheet_id (str | Unset):
        organization_id (UUID | Unset):
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorksheetQuery
     """


    return sync_detailed(
        client=client,
body=body,
worksheet_id=worksheet_id,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  | Unset = UNSET,
    worksheet_id: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | WorksheetQuery]:
    """  Execute a query asynchronously and return query object.

    Args:
        worksheet_id (str | Unset):
        organization_id (UUID | Unset):
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorksheetQuery]
     """


    kwargs = _get_kwargs(
        body=body,
worksheet_id=worksheet_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body:    WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  |     WorksheetQueryCreateRequest  | Unset = UNSET,
    worksheet_id: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | WorksheetQuery | None:
    """  Execute a query asynchronously and return query object.

    Args:
        worksheet_id (str | Unset):
        organization_id (UUID | Unset):
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.
        body (WorksheetQueryCreateRequest): Serializer for creating worksheet queries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorksheetQuery
     """


    return (await asyncio_detailed(
        client=client,
body=body,
worksheet_id=worksheet_id,
organization_id=organization_id,

    )).parsed
