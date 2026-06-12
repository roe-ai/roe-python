from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection import Connection
from ...models.connections_update_response_400_type_1 import ConnectionsUpdateResponse400Type1
from ...models.connections_update_response_400_type_2 import ConnectionsUpdateResponse400Type2
from ...models.duplicate_connection_response import DuplicateConnectionResponse
from ...models.error_detail_response import ErrorDetailResponse
from ...models.update_connection_request import UpdateConnectionRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: UpdateConnectionRequest | Unset = UNSET,
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
        "method": "put",
        "url": "/v1/connections/{id}/".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse | None:
    if response.status_code == 200:
        response_200 = Connection.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        def _parse_response_400(data: object) -> ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_400_type_0 = cast(list[str], data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_1 = ConnectionsUpdateResponse400Type1.from_dict(data)



                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = ConnectionsUpdateResponse400Type2.from_dict(data)



            return response_400_type_2

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = DuplicateConnectionResponse.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (UpdateConnectionRequest | Unset): Serializer for updating connections.

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
        Response[Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse]
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
    client: AuthenticatedClient,
    body: UpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (UpdateConnectionRequest | Unset): Serializer for updating connections.

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
        Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse
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
    client: AuthenticatedClient,
    body: UpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse]:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (UpdateConnectionRequest | Unset): Serializer for updating connections.

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
        Response[Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse]
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
    client: AuthenticatedClient,
    body: UpdateConnectionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse | None:
    """  Public API: GET/PATCH/DELETE /api/v1/connections/{id}/ - Manage connection.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (UpdateConnectionRequest | Unset): Serializer for updating connections.

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
        Connection | ConnectionsUpdateResponse400Type1 | ConnectionsUpdateResponse400Type2 | list[str] | DuplicateConnectionResponse | ErrorDetailResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
