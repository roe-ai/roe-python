from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.base_agent import BaseAgent
from ...models.base_agent_create_request import BaseAgentCreateRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body: BaseAgentCreateRequest,
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
        "url": "/v1/agents/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BaseAgent | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = BaseAgent.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BaseAgent | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BaseAgentCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[BaseAgent | ErrorResponse]:
    """ Create a new base agent.

     Create a new base agent.

    Args:
        organization_id (UUID | Unset):
        body (BaseAgentCreateRequest): Serializer for creating base agents with proper JSON field
            handling

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseAgent | ErrorResponse]
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
    body: BaseAgentCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> BaseAgent | ErrorResponse | None:
    """ Create a new base agent.

     Create a new base agent.

    Args:
        organization_id (UUID | Unset):
        body (BaseAgentCreateRequest): Serializer for creating base agents with proper JSON field
            handling

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseAgent | ErrorResponse
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BaseAgentCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[BaseAgent | ErrorResponse]:
    """ Create a new base agent.

     Create a new base agent.

    Args:
        organization_id (UUID | Unset):
        body (BaseAgentCreateRequest): Serializer for creating base agents with proper JSON field
            handling

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseAgent | ErrorResponse]
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
    body: BaseAgentCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> BaseAgent | ErrorResponse | None:
    """ Create a new base agent.

     Create a new base agent.

    Args:
        organization_id (UUID | Unset):
        body (BaseAgentCreateRequest): Serializer for creating base agents with proper JSON field
            handling

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseAgent | ErrorResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
