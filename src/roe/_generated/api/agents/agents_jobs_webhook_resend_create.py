from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_webhook_resend_response import AgentJobWebhookResendResponse
from ...models.api_error_response import ApiErrorResponse
from ...models.error_detail_response import ErrorDetailResponse
from ...models.resend_agent_job_webhook_request import ResendAgentJobWebhookRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    job_id: UUID,
    *,
    body: ResendAgentJobWebhookRequest | Unset = UNSET,
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
        "url": "/v1/agents/jobs/{job_id}/webhook/resend/".format(job_id=quote(str(job_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse | None:
    if response.status_code == 200:
        response_200 = AgentJobWebhookResendResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResendAgentJobWebhookRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse]:
    """ Resend agent job webhook

     Re-send the completion webhook for a job. Useful for replaying a callback during integration work.
    Sends to every active webhook on the agent, or to one of them when `webhook_id` is given. The job is
    not re-run and its status is unchanged.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (ResendAgentJobWebhookRequest | Unset): Serializer for re-sending a job's completion
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse]
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
    client: AuthenticatedClient,
    body: ResendAgentJobWebhookRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse | None:
    """ Resend agent job webhook

     Re-send the completion webhook for a job. Useful for replaying a callback during integration work.
    Sends to every active webhook on the agent, or to one of them when `webhook_id` is given. The job is
    not re-run and its status is unchanged.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (ResendAgentJobWebhookRequest | Unset): Serializer for re-sending a job's completion
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse
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
    client: AuthenticatedClient,
    body: ResendAgentJobWebhookRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse]:
    """ Resend agent job webhook

     Re-send the completion webhook for a job. Useful for replaying a callback during integration work.
    Sends to every active webhook on the agent, or to one of them when `webhook_id` is given. The job is
    not re-run and its status is unchanged.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (ResendAgentJobWebhookRequest | Unset): Serializer for re-sending a job's completion
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse]
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
    client: AuthenticatedClient,
    body: ResendAgentJobWebhookRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse | None:
    """ Resend agent job webhook

     Re-send the completion webhook for a job. Useful for replaying a callback during integration work.
    Sends to every active webhook on the agent, or to one of them when `webhook_id` is given. The job is
    not re-run and its status is unchanged.

    Args:
        job_id (UUID):
        organization_id (UUID | Unset):
        body (ResendAgentJobWebhookRequest | Unset): Serializer for re-sending a job's completion
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentJobWebhookResendResponse | ApiErrorResponse | ErrorDetailResponse
     """


    return (await asyncio_detailed(
        job_id=job_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
