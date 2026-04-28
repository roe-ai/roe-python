from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patched_update_connection_request import PatchedUpdateConnectionRequest
from ...models.update_connection import UpdateConnection
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body:    PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  | Unset = UNSET,
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
        "method": "patch",
        "url": "/v1/connections/{id}/".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    if isinstance(body, PatchedUpdateConnectionRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedUpdateConnectionRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedUpdateConnectionRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateConnection | None:
    if response.status_code == 200:
        response_200 = UpdateConnection.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateConnection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[UpdateConnection]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateConnection]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> UpdateConnection | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateConnection
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[UpdateConnection]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateConnection]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  |     PatchedUpdateConnectionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> UpdateConnection | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateConnection
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
