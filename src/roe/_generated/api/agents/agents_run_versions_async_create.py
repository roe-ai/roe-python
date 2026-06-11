from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_execution_request import AgentExecutionRequest
from ...models.agents_run_versions_async_create_response_400_type_1 import AgentsRunVersionsAsyncCreateResponse400Type1
from ...models.agents_run_versions_async_create_response_400_type_2 import AgentsRunVersionsAsyncCreateResponse400Type2
from ...models.error_detail_response import ErrorDetailResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    body: AgentExecutionRequest | Unset = UNSET,
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
        "url": "/v1/agents/run/{agent_id}/versions/{agent_version_id}/async/".format(agent_id=quote(str(agent_id), safe=""),agent_version_id=quote(str(agent_version_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        def _parse_response_400(data: object) -> AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str]:
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
                response_400_type_1 = AgentsRunVersionsAsyncCreateResponse400Type1.from_dict(data)



                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = AgentsRunVersionsAsyncCreateResponse400Type2.from_dict(data)



            return response_400_type_2

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorDetailResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = ErrorDetailResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AgentExecutionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str]:
    """  Run agent version asynchronously. Returns agent job id which can be used to check status and get
    results.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequest | Unset): Agent execution request. In addition to `metadata`,
            every key of the agent's input definitions is accepted as a property (text value or file
            upload).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
agent_version_id=agent_version_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AgentExecutionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str | None:
    """  Run agent version asynchronously. Returns agent job id which can be used to check status and get
    results.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequest | Unset): Agent execution request. In addition to `metadata`,
            every key of the agent's input definitions is accepted as a property (text value or file
            upload).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str
     """


    return sync_detailed(
        agent_id=agent_id,
agent_version_id=agent_version_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AgentExecutionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str]:
    """  Run agent version asynchronously. Returns agent job id which can be used to check status and get
    results.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequest | Unset): Agent execution request. In addition to `metadata`,
            every key of the agent's input definitions is accepted as a property (text value or file
            upload).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
agent_version_id=agent_version_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AgentExecutionRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str | None:
    """  Run agent version asynchronously. Returns agent job id which can be used to check status and get
    results.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequest | Unset): Agent execution request. In addition to `metadata`,
            every key of the agent's input definitions is accepted as a property (text value or file
            upload).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsRunVersionsAsyncCreateResponse400Type1 | AgentsRunVersionsAsyncCreateResponse400Type2 | list[str] | ErrorDetailResponse | str
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
agent_version_id=agent_version_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
