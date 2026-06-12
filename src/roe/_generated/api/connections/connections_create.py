from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection import Connection
from ...models.connections_create_response_400_type_1 import ConnectionsCreateResponse400Type1
from ...models.connections_create_response_400_type_2 import ConnectionsCreateResponse400Type2
from ...models.create_connection_request import CreateConnectionRequest
from ...models.duplicate_connection_response import DuplicateConnectionResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body: CreateConnectionRequest,
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
        "url": "/v1/connections/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse | None:
    if response.status_code == 201:
        response_201 = Connection.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        def _parse_response_400(data: object) -> ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str]:
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
                response_400_type_1 = ConnectionsCreateResponse400Type1.from_dict(data)



                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = ConnectionsCreateResponse400Type2.from_dict(data)



            return response_400_type_2

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = DuplicateConnectionResponse.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateConnectionRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse]:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        organization_id (UUID | Unset):
        body (CreateConnectionRequest): Serializer for creating connections.
            Accepts full config, splits into config (DB) and auth (Secrets Manager).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse]
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
    client: AuthenticatedClient,
    body: CreateConnectionRequest,
    organization_id: UUID | Unset = UNSET,

) -> Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse | None:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        organization_id (UUID | Unset):
        body (CreateConnectionRequest): Serializer for creating connections.
            Accepts full config, splits into config (DB) and auth (Secrets Manager).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateConnectionRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse]:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        organization_id (UUID | Unset):
        body (CreateConnectionRequest): Serializer for creating connections.
            Accepts full config, splits into config (DB) and auth (Secrets Manager).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse]
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
    client: AuthenticatedClient,
    body: CreateConnectionRequest,
    organization_id: UUID | Unset = UNSET,

) -> Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse | None:
    """  Public API: GET/POST /api/v1/connections/ - List/create connections.

    Args:
        organization_id (UUID | Unset):
        body (CreateConnectionRequest): Serializer for creating connections.
            Accepts full config, splits into config (DB) and auth (Secrets Manager).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Connection | ConnectionsCreateResponse400Type1 | ConnectionsCreateResponse400Type2 | list[str] | DuplicateConnectionResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
