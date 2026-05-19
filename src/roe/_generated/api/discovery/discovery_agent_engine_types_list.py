from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_engine_type_list import AgentEngineTypeList
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/discovery/agent-engine-types/",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentEngineTypeList | None:
    if response.status_code == 200:
        response_200 = AgentEngineTypeList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentEngineTypeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AgentEngineTypeList]:
    """ List supported agent engine types

     Returns the production engine_class_id values accepted by agent creation APIs, plus human-readable
    metadata and input schemas. Use this before create_agent or create_agent_version when choosing an
    engine and constructing engine_config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentEngineTypeList]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> AgentEngineTypeList | None:
    """ List supported agent engine types

     Returns the production engine_class_id values accepted by agent creation APIs, plus human-readable
    metadata and input schemas. Use this before create_agent or create_agent_version when choosing an
    engine and constructing engine_config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentEngineTypeList
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AgentEngineTypeList]:
    """ List supported agent engine types

     Returns the production engine_class_id values accepted by agent creation APIs, plus human-readable
    metadata and input schemas. Use this before create_agent or create_agent_version when choosing an
    engine and constructing engine_config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentEngineTypeList]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> AgentEngineTypeList | None:
    """ List supported agent engine types

     Returns the production engine_class_id values accepted by agent creation APIs, plus human-readable
    metadata and input schemas. Use this before create_agent or create_agent_version when choosing an
    engine and constructing engine_config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentEngineTypeList
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
