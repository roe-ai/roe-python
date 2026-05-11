from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_version import AgentVersion
from ...models.agent_version_create_request import AgentVersionCreateRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    *,
    body: AgentVersionCreateRequest,
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
        "url": "/v1/agents/{agent_id}/versions/".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentVersion | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = AgentVersion.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentVersion | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AgentVersionCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentVersion | ErrorResponse]:
    """ Create a new agent version.

     Create a new version of an existing agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentVersionCreateRequest): Serializer for creating new agent versions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVersion | ErrorResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AgentVersionCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> AgentVersion | ErrorResponse | None:
    """ Create a new agent version.

     Create a new version of an existing agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentVersionCreateRequest): Serializer for creating new agent versions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVersion | ErrorResponse
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AgentVersionCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentVersion | ErrorResponse]:
    """ Create a new agent version.

     Create a new version of an existing agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentVersionCreateRequest): Serializer for creating new agent versions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVersion | ErrorResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AgentVersionCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> AgentVersion | ErrorResponse | None:
    """ Create a new agent version.

     Create a new version of an existing agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentVersionCreateRequest): Serializer for creating new agent versions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVersion | ErrorResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
