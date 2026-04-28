from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.batch_create_agent_webhook import BatchCreateAgentWebhook
from ...models.batch_create_agent_webhook_request import BatchCreateAgentWebhookRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    webhook_id: UUID,
    *,
    body:    BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  | Unset = UNSET,
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
        "url": "/v1/webhooks/{webhook_id}/agents/".format(webhook_id=quote(str(webhook_id), safe=""),),
        "params": params,
    }

    if isinstance(body, BatchCreateAgentWebhookRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, BatchCreateAgentWebhookRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, BatchCreateAgentWebhookRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BatchCreateAgentWebhook | None:
    if response.status_code == 201:
        response_201 = BatchCreateAgentWebhook.from_dict(response.json())



        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BatchCreateAgentWebhook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[BatchCreateAgentWebhook]:
    """  List agents linked to a webhook, or link new agents.

    GET: List all agents linked to this webhook
    POST: Link one or more agents to this webhook

    Args:
        webhook_id (UUID):
        organization_id (UUID | Unset):
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchCreateAgentWebhook]
     """


    kwargs = _get_kwargs(
        webhook_id=webhook_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> BatchCreateAgentWebhook | None:
    """  List agents linked to a webhook, or link new agents.

    GET: List all agents linked to this webhook
    POST: Link one or more agents to this webhook

    Args:
        webhook_id (UUID):
        organization_id (UUID | Unset):
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchCreateAgentWebhook
     """


    return sync_detailed(
        webhook_id=webhook_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[BatchCreateAgentWebhook]:
    """  List agents linked to a webhook, or link new agents.

    GET: List all agents linked to this webhook
    POST: Link one or more agents to this webhook

    Args:
        webhook_id (UUID):
        organization_id (UUID | Unset):
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchCreateAgentWebhook]
     """


    kwargs = _get_kwargs(
        webhook_id=webhook_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  |     BatchCreateAgentWebhookRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> BatchCreateAgentWebhook | None:
    """  List agents linked to a webhook, or link new agents.

    GET: List all agents linked to this webhook
    POST: Link one or more agents to this webhook

    Args:
        webhook_id (UUID):
        organization_id (UUID | Unset):
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.
        body (BatchCreateAgentWebhookRequest): Serializer for batch linking multiple agents to a
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchCreateAgentWebhook
     """


    return (await asyncio_detailed(
        webhook_id=webhook_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
