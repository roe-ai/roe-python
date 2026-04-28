from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_rerun_response import AgentJobRerunResponse
from ...models.agent_job_rerun_v2_request_request import AgentJobRerunV2RequestRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    job_id: UUID,
    *,
    body:    AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  | Unset = UNSET,
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
        "url": "/v2/agents/{agent_id}/jobs/{job_id}:rerun".format(agent_id=quote(str(agent_id), safe=""),job_id=quote(str(job_id), safe=""),),
        "params": params,
    }

    if isinstance(body, AgentJobRerunV2RequestRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentJobRerunV2RequestRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AgentJobRerunV2RequestRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentJobRerunResponse | Any | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AgentJobRerunResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentJobRerunResponse | Any | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobRerunResponse | Any | ErrorResponse]:
    """ Re-run agent job (:rerun)

     Re-run a completed agent job.

    Args:
        agent_id (UUID):
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobRerunResponse | Any | ErrorResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
job_id=job_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobRerunResponse | Any | ErrorResponse | None:
    """ Re-run agent job (:rerun)

     Re-run a completed agent job.

    Args:
        agent_id (UUID):
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobRerunResponse | Any | ErrorResponse
     """


    return sync_detailed(
        agent_id=agent_id,
job_id=job_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobRerunResponse | Any | ErrorResponse]:
    """ Re-run agent job (:rerun)

     Re-run a completed agent job.

    Args:
        agent_id (UUID):
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobRerunResponse | Any | ErrorResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
job_id=job_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  |     AgentJobRerunV2RequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobRerunResponse | Any | ErrorResponse | None:
    """ Re-run agent job (:rerun)

     Re-run a completed agent job.

    Args:
        agent_id (UUID):
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):
        body (AgentJobRerunV2RequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobRerunResponse | Any | ErrorResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
job_id=job_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
