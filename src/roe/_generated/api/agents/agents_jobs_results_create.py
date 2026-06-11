from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_job_result_item import AgentJobResultItem
from ...models.agent_job_result_many_request import AgentJobResultManyRequest
from ...models.agents_jobs_results_create_response_400 import AgentsJobsResultsCreateResponse400
from ...models.error_detail_response import ErrorDetailResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body: AgentJobResultManyRequest,
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = AgentJobResultItem.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = AgentsJobsResultsCreateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorDetailResponse.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentJobResultManyRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem]]:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem]]
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
    client: AuthenticatedClient,
    body: AgentJobResultManyRequest,
    organization_id: UUID | Unset = UNSET,

) -> AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem] | None:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem]
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentJobResultManyRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem]]:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem]]
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
    client: AuthenticatedClient,
    body: AgentJobResultManyRequest,
    organization_id: UUID | Unset = UNSET,

) -> AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem] | None:
    """ Get results for multiple agent jobs

     Retrieve the detailed results for multiple agent jobs by providing a list of job IDs

    Args:
        organization_id (UUID | Unset):
        body (AgentJobResultManyRequest): Serializer for bulk agent job results request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsJobsResultsCreateResponse400 | ErrorDetailResponse | list[AgentJobResultItem]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
