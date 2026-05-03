from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_delete_data_response import AgentJobDeleteDataResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    job_id: UUID,
    *,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/agents/jobs/{job_id}/delete-data/".format(job_id=quote(str(job_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentJobDeleteDataResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AgentJobDeleteDataResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentJobDeleteDataResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobDeleteDataResponse | ErrorResponse]:
    """ Delete agent job data

     Delete uploaded inputs from S3, sanitize stored blob data (outputs, steps, logs, trace), and delete
    workflow artifacts for an agent job without removing DB metadata.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobDeleteDataResponse | ErrorResponse]
     """


    kwargs = _get_kwargs(
        job_id=job_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobDeleteDataResponse | ErrorResponse | None:
    """ Delete agent job data

     Delete uploaded inputs from S3, sanitize stored blob data (outputs, steps, logs, trace), and delete
    workflow artifacts for an agent job without removing DB metadata.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobDeleteDataResponse | ErrorResponse
     """


    return sync_detailed(
        job_id=job_id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobDeleteDataResponse | ErrorResponse]:
    """ Delete agent job data

     Delete uploaded inputs from S3, sanitize stored blob data (outputs, steps, logs, trace), and delete
    workflow artifacts for an agent job without removing DB metadata.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobDeleteDataResponse | ErrorResponse]
     """


    kwargs = _get_kwargs(
        job_id=job_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobDeleteDataResponse | ErrorResponse | None:
    """ Delete agent job data

     Delete uploaded inputs from S3, sanitize stored blob data (outputs, steps, logs, trace), and delete
    workflow artifacts for an agent job without removing DB metadata.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobDeleteDataResponse | ErrorResponse
     """


    return (await asyncio_detailed(
        job_id=job_id,
client=client,
organization_id=organization_id,

    )).parsed
