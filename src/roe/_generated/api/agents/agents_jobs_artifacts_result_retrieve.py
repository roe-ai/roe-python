from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_artifact_result import AgentJobArtifactResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_job_id: str,
    *,
    artifact_key: str,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["artifact_key"] = artifact_key

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/jobs/{agent_job_id}/artifacts/result/".format(agent_job_id=quote(str(agent_job_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentJobArtifactResult | Any | None:
    if response.status_code == 200:
        response_200 = AgentJobArtifactResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentJobArtifactResult | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_job_id: str,
    *,
    client: AuthenticatedClient,
    artifact_key: str,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobArtifactResult | Any]:
    """ Get tool result artifact (result only)

     Fetches a tool result artifact for an agent job, returning only the `result` field. Internal fields
    (`metadata`, `input`, and cost/token `usage` data) are stripped. The artifact_key is available in
    the agent job result output (e.g. `evidence_data` values).

    Args:
        agent_job_id (str):
        artifact_key (str):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobArtifactResult | Any]
     """


    kwargs = _get_kwargs(
        agent_job_id=agent_job_id,
artifact_key=artifact_key,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_job_id: str,
    *,
    client: AuthenticatedClient,
    artifact_key: str,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobArtifactResult | Any | None:
    """ Get tool result artifact (result only)

     Fetches a tool result artifact for an agent job, returning only the `result` field. Internal fields
    (`metadata`, `input`, and cost/token `usage` data) are stripped. The artifact_key is available in
    the agent job result output (e.g. `evidence_data` values).

    Args:
        agent_job_id (str):
        artifact_key (str):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobArtifactResult | Any
     """


    return sync_detailed(
        agent_job_id=agent_job_id,
client=client,
artifact_key=artifact_key,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_job_id: str,
    *,
    client: AuthenticatedClient,
    artifact_key: str,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobArtifactResult | Any]:
    """ Get tool result artifact (result only)

     Fetches a tool result artifact for an agent job, returning only the `result` field. Internal fields
    (`metadata`, `input`, and cost/token `usage` data) are stripped. The artifact_key is available in
    the agent job result output (e.g. `evidence_data` values).

    Args:
        agent_job_id (str):
        artifact_key (str):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobArtifactResult | Any]
     """


    kwargs = _get_kwargs(
        agent_job_id=agent_job_id,
artifact_key=artifact_key,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_job_id: str,
    *,
    client: AuthenticatedClient,
    artifact_key: str,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobArtifactResult | Any | None:
    """ Get tool result artifact (result only)

     Fetches a tool result artifact for an agent job, returning only the `result` field. Internal fields
    (`metadata`, `input`, and cost/token `usage` data) are stripped. The artifact_key is available in
    the agent job result output (e.g. `evidence_data` values).

    Args:
        agent_job_id (str):
        artifact_key (str):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobArtifactResult | Any
     """


    return (await asyncio_detailed(
        agent_job_id=agent_job_id,
client=client,
artifact_key=artifact_key,
organization_id=organization_id,

    )).parsed
