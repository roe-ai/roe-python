from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_partial_update_response_400 import AgentsPartialUpdateResponse400
from ...models.base_agent import BaseAgent
from ...models.error_detail_response import ErrorDetailResponse
from ...models.patched_base_agent_update_request import PatchedBaseAgentUpdateRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    *,
    body: PatchedBaseAgentUpdateRequest | Unset = UNSET,
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
        "url": "/v1/agents/{agent_id}/".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse | None:
    if response.status_code == 200:
        response_200 = BaseAgent.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = AgentsPartialUpdateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorDetailResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedBaseAgentUpdateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse]:
    """ Partially update an agent.

     Partially update details of a specific base agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedBaseAgentUpdateRequest | Unset): Serializer for updating BaseAgent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse]
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
    client: AuthenticatedClient,
    body: PatchedBaseAgentUpdateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse | None:
    """ Partially update an agent.

     Partially update details of a specific base agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedBaseAgentUpdateRequest | Unset): Serializer for updating BaseAgent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse
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
    client: AuthenticatedClient,
    body: PatchedBaseAgentUpdateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse]:
    """ Partially update an agent.

     Partially update details of a specific base agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedBaseAgentUpdateRequest | Unset): Serializer for updating BaseAgent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse]
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
    client: AuthenticatedClient,
    body: PatchedBaseAgentUpdateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse | None:
    """ Partially update an agent.

     Partially update details of a specific base agent.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedBaseAgentUpdateRequest | Unset): Serializer for updating BaseAgent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsPartialUpdateResponse400 | BaseAgent | ErrorDetailResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
