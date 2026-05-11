from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_result_many_request_request import AgentJobResultManyRequestRequest
from ...models.error_response import ErrorResponse
from ...models.paginated_agent_job_result_item_list import PaginatedAgentJobResultItemList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body: AgentJobResultManyRequestRequest,
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
        "url": "/v1/agents/jobs/results/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | PaginatedAgentJobResultItemList | None:
    if response.status_code == 200:
        response_200 = PaginatedAgentJobResultItemList.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | PaginatedAgentJobResultItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentJobResultManyRequestRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | PaginatedAgentJobResultItemList]:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequestRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedAgentJobResultItemList]
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
    body: AgentJobResultManyRequestRequest,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | PaginatedAgentJobResultItemList | None:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequestRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedAgentJobResultItemList
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentJobResultManyRequestRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | PaginatedAgentJobResultItemList]:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequestRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedAgentJobResultItemList]
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
    body: AgentJobResultManyRequestRequest,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | PaginatedAgentJobResultItemList | None:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequestRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedAgentJobResultItemList
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
