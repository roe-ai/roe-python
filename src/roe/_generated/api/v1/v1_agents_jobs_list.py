from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.paginated_list_agent_job_list import PaginatedListAgentJobList
from ...models.v1_agents_jobs_list_ordering_item import V1AgentsJobsListOrderingItem
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    agent_id: UUID,
    *,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    exclude_metadata: str | Unset = UNSET,
    job_id: str | Unset = UNSET,
    job_inputs: str | Unset = UNSET,
    metadata: str | Unset = UNSET,
    ordering: list[V1AgentsJobsListOrderingItem] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    semantic_string: str | Unset = UNSET,
    status_code: str | Unset = UNSET,
    version_name: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_created_from: str | Unset = UNSET
    if not isinstance(created_from, Unset):
        json_created_from = created_from.isoformat()
    params["created_from"] = json_created_from

    json_created_to: str | Unset = UNSET
    if not isinstance(created_to, Unset):
        json_created_to = created_to.isoformat()
    params["created_to"] = json_created_to

    params["exclude_metadata"] = exclude_metadata

    params["job_id"] = job_id

    params["job_inputs"] = job_inputs

    params["metadata"] = metadata

    json_ordering: list[str] | Unset = UNSET
    if not isinstance(ordering, Unset):
        json_ordering = []
        for ordering_item_data in ordering:
            ordering_item = ordering_item_data.value
            json_ordering.append(ordering_item)


    params["ordering"] = json_ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params["semantic_string"] = semantic_string

    params["status_code"] = status_code

    params["version_name"] = version_name

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{agent_id}/jobs/".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | PaginatedListAgentJobList | None:
    if response.status_code == 200:
        response_200 = PaginatedListAgentJobList.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | PaginatedListAgentJobList]:
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
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    exclude_metadata: str | Unset = UNSET,
    job_id: str | Unset = UNSET,
    job_inputs: str | Unset = UNSET,
    metadata: str | Unset = UNSET,
    ordering: list[V1AgentsJobsListOrderingItem] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    semantic_string: str | Unset = UNSET,
    status_code: str | Unset = UNSET,
    version_name: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | PaginatedListAgentJobList]:
    """ List agent jobs or create a new agent job.

     Retrieve a list of jobs for a specific agent or create a new job

    Args:
        agent_id (UUID):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        exclude_metadata (str | Unset):
        job_id (str | Unset):
        job_inputs (str | Unset):
        metadata (str | Unset):
        ordering (list[V1AgentsJobsListOrderingItem] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        semantic_string (str | Unset):
        status_code (str | Unset):
        version_name (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedListAgentJobList]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
created_from=created_from,
created_to=created_to,
exclude_metadata=exclude_metadata,
job_id=job_id,
job_inputs=job_inputs,
metadata=metadata,
ordering=ordering,
page=page,
page_size=page_size,
search=search,
semantic_string=semantic_string,
status_code=status_code,
version_name=version_name,
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
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    exclude_metadata: str | Unset = UNSET,
    job_id: str | Unset = UNSET,
    job_inputs: str | Unset = UNSET,
    metadata: str | Unset = UNSET,
    ordering: list[V1AgentsJobsListOrderingItem] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    semantic_string: str | Unset = UNSET,
    status_code: str | Unset = UNSET,
    version_name: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | PaginatedListAgentJobList | None:
    """ List agent jobs or create a new agent job.

     Retrieve a list of jobs for a specific agent or create a new job

    Args:
        agent_id (UUID):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        exclude_metadata (str | Unset):
        job_id (str | Unset):
        job_inputs (str | Unset):
        metadata (str | Unset):
        ordering (list[V1AgentsJobsListOrderingItem] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        semantic_string (str | Unset):
        status_code (str | Unset):
        version_name (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedListAgentJobList
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
created_from=created_from,
created_to=created_to,
exclude_metadata=exclude_metadata,
job_id=job_id,
job_inputs=job_inputs,
metadata=metadata,
ordering=ordering,
page=page,
page_size=page_size,
search=search,
semantic_string=semantic_string,
status_code=status_code,
version_name=version_name,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    exclude_metadata: str | Unset = UNSET,
    job_id: str | Unset = UNSET,
    job_inputs: str | Unset = UNSET,
    metadata: str | Unset = UNSET,
    ordering: list[V1AgentsJobsListOrderingItem] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    semantic_string: str | Unset = UNSET,
    status_code: str | Unset = UNSET,
    version_name: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorResponse | PaginatedListAgentJobList]:
    """ List agent jobs or create a new agent job.

     Retrieve a list of jobs for a specific agent or create a new job

    Args:
        agent_id (UUID):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        exclude_metadata (str | Unset):
        job_id (str | Unset):
        job_inputs (str | Unset):
        metadata (str | Unset):
        ordering (list[V1AgentsJobsListOrderingItem] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        semantic_string (str | Unset):
        status_code (str | Unset):
        version_name (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedListAgentJobList]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
created_from=created_from,
created_to=created_to,
exclude_metadata=exclude_metadata,
job_id=job_id,
job_inputs=job_inputs,
metadata=metadata,
ordering=ordering,
page=page,
page_size=page_size,
search=search,
semantic_string=semantic_string,
status_code=status_code,
version_name=version_name,
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
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    exclude_metadata: str | Unset = UNSET,
    job_id: str | Unset = UNSET,
    job_inputs: str | Unset = UNSET,
    metadata: str | Unset = UNSET,
    ordering: list[V1AgentsJobsListOrderingItem] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    semantic_string: str | Unset = UNSET,
    status_code: str | Unset = UNSET,
    version_name: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorResponse | PaginatedListAgentJobList | None:
    """ List agent jobs or create a new agent job.

     Retrieve a list of jobs for a specific agent or create a new job

    Args:
        agent_id (UUID):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        exclude_metadata (str | Unset):
        job_id (str | Unset):
        job_inputs (str | Unset):
        metadata (str | Unset):
        ordering (list[V1AgentsJobsListOrderingItem] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        semantic_string (str | Unset):
        status_code (str | Unset):
        version_name (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedListAgentJobList
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
created_from=created_from,
created_to=created_to,
exclude_metadata=exclude_metadata,
job_id=job_id,
job_inputs=job_inputs,
metadata=metadata,
ordering=ordering,
page=page,
page_size=page_size,
search=search,
semantic_string=semantic_string,
status_code=status_code,
version_name=version_name,
organization_id=organization_id,

    )).parsed
