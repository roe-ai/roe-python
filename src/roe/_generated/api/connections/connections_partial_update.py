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
    body: PatchedUpdateConnectionRequest | Unset = UNSET,
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

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

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
    body: PatchedUpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[UpdateConnection]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

            Cross-state Pydantic validation (config + auth) lives in the view's
            ``update()`` method now -- see ``connections.views.
            ConnectionRetrieveUpdateDestroyView.update``. That path is the single
            source of truth for canonical validation + write, mirrors the create
            path's ``service.create_connection_with_secrets``, AND correctly
            handles the SM-fetch-failure case for the unchanged-auth branch
            (returns 502 / opportunistic backfill instead of silently corrupting
            the fingerprint by hashing ``{}``). Re-running the same validation
            here would (a) double the work, (b) bypass the SM-failure semantics,
            and (c) leak Pydantic field/value details through DRF's generic 400
            handler. The serializer only does shape checks.

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
    body: PatchedUpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> UpdateConnection | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

            Cross-state Pydantic validation (config + auth) lives in the view's
            ``update()`` method now -- see ``connections.views.
            ConnectionRetrieveUpdateDestroyView.update``. That path is the single
            source of truth for canonical validation + write, mirrors the create
            path's ``service.create_connection_with_secrets``, AND correctly
            handles the SM-fetch-failure case for the unchanged-auth branch
            (returns 502 / opportunistic backfill instead of silently corrupting
            the fingerprint by hashing ``{}``). Re-running the same validation
            here would (a) double the work, (b) bypass the SM-failure semantics,
            and (c) leak Pydantic field/value details through DRF's generic 400
            handler. The serializer only does shape checks.

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
    body: PatchedUpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[UpdateConnection]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

            Cross-state Pydantic validation (config + auth) lives in the view's
            ``update()`` method now -- see ``connections.views.
            ConnectionRetrieveUpdateDestroyView.update``. That path is the single
            source of truth for canonical validation + write, mirrors the create
            path's ``service.create_connection_with_secrets``, AND correctly
            handles the SM-fetch-failure case for the unchanged-auth branch
            (returns 502 / opportunistic backfill instead of silently corrupting
            the fingerprint by hashing ``{}``). Re-running the same validation
            here would (a) double the work, (b) bypass the SM-failure semantics,
            and (c) leak Pydantic field/value details through DRF's generic 400
            handler. The serializer only does shape checks.

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
    body: PatchedUpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> UpdateConnection | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (PatchedUpdateConnectionRequest | Unset): Serializer for updating connections.

            Cross-state Pydantic validation (config + auth) lives in the view's
            ``update()`` method now -- see ``connections.views.
            ConnectionRetrieveUpdateDestroyView.update``. That path is the single
            source of truth for canonical validation + write, mirrors the create
            path's ``service.create_connection_with_secrets``, AND correctly
            handles the SM-fetch-failure case for the unchanged-auth branch
            (returns 502 / opportunistic backfill instead of silently corrupting
            the fingerprint by hashing ``{}``). Re-running the same validation
            here would (a) double the work, (b) bypass the SM-failure semantics,
            and (c) leak Pydantic field/value details through DRF's generic 400
            handler. The serializer only does shape checks.

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
