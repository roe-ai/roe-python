from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection_trigger import ConnectionTrigger
from ...models.connection_trigger_create_request import ConnectionTriggerCreateRequest
from typing import cast



def _get_kwargs(
    *,
    body:    ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  | Unset = UNSET,
    organization_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["organization_id"] = organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connection-triggers/",
        "params": params,
    }

    if isinstance(body, ConnectionTriggerCreateRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, ConnectionTriggerCreateRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConnectionTriggerCreateRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectionTrigger | None:
    if response.status_code == 201:
        response_201 = ConnectionTrigger.from_dict(response.json())



        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body:    ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  | Unset = UNSET,
    organization_id: str,

) -> Response[ConnectionTrigger]:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        organization_id (str):
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionTrigger]
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
    body:    ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  | Unset = UNSET,
    organization_id: str,

) -> ConnectionTrigger | None:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        organization_id (str):
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionTrigger
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  | Unset = UNSET,
    organization_id: str,

) -> Response[ConnectionTrigger]:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        organization_id (str):
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionTrigger]
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
    body:    ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  |     ConnectionTriggerCreateRequest  | Unset = UNSET,
    organization_id: str,

) -> ConnectionTrigger | None:
    """  GET /connection-triggers/ -- List triggers for an organization.
    POST /connection-triggers/ -- Create a new trigger.

    Args:
        organization_id (str):
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.
        body (ConnectionTriggerCreateRequest): Write serializer for creating a connection trigger.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionTrigger
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
