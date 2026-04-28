from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_status import AgentJobStatus
from ...models.agent_job_status_many_request_request import AgentJobStatusManyRequestRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body:    AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  | Unset = UNSET,
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
        "url": "/v1/agents/jobs/statuses/",
        "params": params,
    }

    if isinstance(body, AgentJobStatusManyRequestRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentJobStatusManyRequestRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AgentJobStatusManyRequestRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | list[AgentJobStatus] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = AgentJobStatus.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | list[AgentJobStatus]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | list[AgentJobStatus]]:
    """ Get status for multiple agent jobs

     Retrieve the current status for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[AgentJobStatus]]
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
    body:    AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | list[AgentJobStatus] | None:
    """ Get status for multiple agent jobs

     Retrieve the current status for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[AgentJobStatus]
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | list[AgentJobStatus]]:
    """ Get status for multiple agent jobs

     Retrieve the current status for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[AgentJobStatus]]
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
    body:    AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  |     AgentJobStatusManyRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | list[AgentJobStatus] | None:
    """ Get status for multiple agent jobs

     Retrieve the current status for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.
        body (AgentJobStatusManyRequestRequest): Serializer for bulk agent job status request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[AgentJobStatus]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
