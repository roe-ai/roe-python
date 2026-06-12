from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_version import AgentVersion
from ...models.error_detail_response import ErrorDetailResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    *,
    get_supports_eval: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["get_supports_eval"] = get_supports_eval

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{agent_id}/versions/current/".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentVersion | ErrorDetailResponse | None:
    if response.status_code == 200:
        response_200 = AgentVersion.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentVersion | ErrorDetailResponse]:
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
    get_supports_eval: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentVersion | ErrorDetailResponse]:
    """ Retrieve the current version of an agent.

     Retrieve details of the current version of a specific agent.

    Args:
        agent_id (UUID):
        get_supports_eval (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVersion | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
get_supports_eval=get_supports_eval,
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
    get_supports_eval: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentVersion | ErrorDetailResponse | None:
    """ Retrieve the current version of an agent.

     Retrieve details of the current version of a specific agent.

    Args:
        agent_id (UUID):
        get_supports_eval (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVersion | ErrorDetailResponse
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
get_supports_eval=get_supports_eval,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_id: UUID,
    *,
    client: AuthenticatedClient,
    get_supports_eval: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentVersion | ErrorDetailResponse]:
    """ Retrieve the current version of an agent.

     Retrieve details of the current version of a specific agent.

    Args:
        agent_id (UUID):
        get_supports_eval (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVersion | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
get_supports_eval=get_supports_eval,
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
    get_supports_eval: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentVersion | ErrorDetailResponse | None:
    """ Retrieve the current version of an agent.

     Retrieve details of the current version of a specific agent.

    Args:
        agent_id (UUID):
        get_supports_eval (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVersion | ErrorDetailResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
get_supports_eval=get_supports_eval,
organization_id=organization_id,

    )).parsed
