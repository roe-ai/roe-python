from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_datum import AgentDatum
from ...models.agent_execution_request_request import AgentExecutionRequestRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    *,
    body: AgentExecutionRequestRequest | Unset = UNSET,
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
        "url": "/v1/agents/run/{agent_id}/".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | list[AgentDatum] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = AgentDatum.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())



        return response_402

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | list[AgentDatum]]:
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
    body: AgentExecutionRequestRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | list[AgentDatum]]:
    """ Run agent synchronously

     Execute an agent with provided inputs and return results immediately.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequestRequest | Unset): Serializer for agent execution requests with
            dynamic input fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[AgentDatum]]
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
    body: AgentExecutionRequestRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | list[AgentDatum] | None:
    """ Run agent synchronously

     Execute an agent with provided inputs and return results immediately.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequestRequest | Unset): Serializer for agent execution requests with
            dynamic input fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[AgentDatum]
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
    body: AgentExecutionRequestRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | list[AgentDatum]]:
    """ Run agent synchronously

     Execute an agent with provided inputs and return results immediately.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequestRequest | Unset): Serializer for agent execution requests with
            dynamic input fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[AgentDatum]]
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
    body: AgentExecutionRequestRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | list[AgentDatum] | None:
    """ Run agent synchronously

     Execute an agent with provided inputs and return results immediately.

    Args:
        agent_id (UUID):
        organization_id (UUID | Unset):
        body (AgentExecutionRequestRequest | Unset): Serializer for agent execution requests with
            dynamic input fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[AgentDatum]
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
