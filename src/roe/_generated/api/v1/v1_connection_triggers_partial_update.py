from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection_trigger import ConnectionTrigger
from ...models.patched_connection_trigger_update_request import PatchedConnectionTriggerUpdateRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trigger_id: UUID,
    *,
    body:    PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  | Unset = UNSET,
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
        "url": "/v1/connection-triggers/{trigger_id}/".format(trigger_id=quote(str(trigger_id), safe=""),),
        "params": params,
    }

    if isinstance(body, PatchedConnectionTriggerUpdateRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedConnectionTriggerUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedConnectionTriggerUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectionTrigger | None:
    if response.status_code == 200:
        response_200 = ConnectionTrigger.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectionTrigger]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ConnectionTrigger]:
    """  Update trigger (enable/disable, change input_key).

    Args:
        trigger_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionTrigger]
     """


    kwargs = _get_kwargs(
        trigger_id=trigger_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ConnectionTrigger | None:
    """  Update trigger (enable/disable, change input_key).

    Args:
        trigger_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionTrigger
     """


    return sync_detailed(
        trigger_id=trigger_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ConnectionTrigger]:
    """  Update trigger (enable/disable, change input_key).

    Args:
        trigger_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionTrigger]
     """


    kwargs = _get_kwargs(
        trigger_id=trigger_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  |     PatchedConnectionTriggerUpdateRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ConnectionTrigger | None:
    """  Update trigger (enable/disable, change input_key).

    Args:
        trigger_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).
        body (PatchedConnectionTriggerUpdateRequest | Unset): Write serializer for updating a
            connection trigger (enable/disable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionTrigger
     """


    return (await asyncio_detailed(
        trigger_id=trigger_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
