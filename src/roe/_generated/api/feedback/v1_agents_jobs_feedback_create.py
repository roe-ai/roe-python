from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_feedback_request_request import AgentJobFeedbackRequestRequest
from ...models.agent_job_feedback_response import AgentJobFeedbackResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    job_id: UUID,
    *,
    body:    AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  | Unset = UNSET,
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
        "url": "/v1/agents/jobs/{job_id}/feedback/".format(job_id=quote(str(job_id), safe=""),),
        "params": params,
    }

    if isinstance(body, AgentJobFeedbackRequestRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentJobFeedbackRequestRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AgentJobFeedbackRequestRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentJobFeedbackResponse | Any | None:
    if response.status_code == 200:
        response_200 = AgentJobFeedbackResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentJobFeedbackResponse | Any]:
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
    body:    AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobFeedbackResponse | Any]:
    """ Submit agent job feedback

     Submit feedback for an agent job.

    Storage conditions:
    - YES only (no feedback): Saved to DB, no memory storage
    - YES + feedback: Saved to DB, triggers memory storage
    - NO (corrected_verdict required): Saved to DB, triggers memory storage

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobFeedbackResponse | Any]
     """


    kwargs = _get_kwargs(
        job_id=job_id,
body=body,
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
    body:    AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobFeedbackResponse | Any | None:
    """ Submit agent job feedback

     Submit feedback for an agent job.

    Storage conditions:
    - YES only (no feedback): Saved to DB, no memory storage
    - YES + feedback: Saved to DB, triggers memory storage
    - NO (corrected_verdict required): Saved to DB, triggers memory storage

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobFeedbackResponse | Any
     """


    return sync_detailed(
        job_id=job_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobFeedbackResponse | Any]:
    """ Submit agent job feedback

     Submit feedback for an agent job.

    Storage conditions:
    - YES only (no feedback): Saved to DB, no memory storage
    - YES + feedback: Saved to DB, triggers memory storage
    - NO (corrected_verdict required): Saved to DB, triggers memory storage

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobFeedbackResponse | Any]
     """


    kwargs = _get_kwargs(
        job_id=job_id,
body=body,
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
    body:    AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  |     AgentJobFeedbackRequestRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobFeedbackResponse | Any | None:
    """ Submit agent job feedback

     Submit feedback for an agent job.

    Storage conditions:
    - YES only (no feedback): Saved to DB, no memory storage
    - YES + feedback: Saved to DB, triggers memory storage
    - NO (corrected_verdict required): Saved to DB, triggers memory storage

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.
        body (AgentJobFeedbackRequestRequest): Serializer for submitting agent job feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobFeedbackResponse | Any
     """


    return (await asyncio_detailed(
        job_id=job_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
