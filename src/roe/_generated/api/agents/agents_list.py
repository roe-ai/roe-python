from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_list_response_400 import AgentsListResponse400
from ...models.error_detail_response import ErrorDetailResponse
from ...models.paginated_base_agent_list import PaginatedBaseAgentList
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    creator_id: list[int] | Unset = UNSET,
    engine_class_id: list[str] | Unset = UNSET,
    exclude_engine_class_id: str | Unset = UNSET,
    include_job_stats: bool | Unset = UNSET,
    include_untagged: bool | Unset = UNSET,
    job_count_max: int | Unset = UNSET,
    job_count_min: int | Unset = UNSET,
    most_recent_job_from: datetime.datetime | Unset = UNSET,
    most_recent_job_to: datetime.datetime | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    updated_from: datetime.datetime | Unset = UNSET,
    updated_to: datetime.datetime | Unset = UNSET,

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

    json_creator_id: list[int] | Unset = UNSET
    if not isinstance(creator_id, Unset):
        json_creator_id = creator_id


    params["creator_id"] = json_creator_id

    json_engine_class_id: list[str] | Unset = UNSET
    if not isinstance(engine_class_id, Unset):
        json_engine_class_id = engine_class_id


    params["engine_class_id"] = json_engine_class_id

    params["exclude_engine_class_id"] = exclude_engine_class_id

    params["include_job_stats"] = include_job_stats

    params["include_untagged"] = include_untagged

    params["job_count_max"] = job_count_max

    params["job_count_min"] = job_count_min

    json_most_recent_job_from: str | Unset = UNSET
    if not isinstance(most_recent_job_from, Unset):
        json_most_recent_job_from = most_recent_job_from.isoformat()
    params["most_recent_job_from"] = json_most_recent_job_from

    json_most_recent_job_to: str | Unset = UNSET
    if not isinstance(most_recent_job_to, Unset):
        json_most_recent_job_to = most_recent_job_to.isoformat()
    params["most_recent_job_to"] = json_most_recent_job_to

    params["name"] = name

    params["ordering"] = ordering

    json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags


    params["tags"] = json_tags

    json_updated_from: str | Unset = UNSET
    if not isinstance(updated_from, Unset):
        json_updated_from = updated_from.isoformat()
    params["updated_from"] = json_updated_from

    json_updated_to: str | Unset = UNSET
    if not isinstance(updated_to, Unset):
        json_updated_to = updated_to.isoformat()
    params["updated_to"] = json_updated_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList | None:
    if response.status_code == 200:
        response_200 = PaginatedBaseAgentList.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = AgentsListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorDetailResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    creator_id: list[int] | Unset = UNSET,
    engine_class_id: list[str] | Unset = UNSET,
    exclude_engine_class_id: str | Unset = UNSET,
    include_job_stats: bool | Unset = UNSET,
    include_untagged: bool | Unset = UNSET,
    job_count_max: int | Unset = UNSET,
    job_count_min: int | Unset = UNSET,
    most_recent_job_from: datetime.datetime | Unset = UNSET,
    most_recent_job_to: datetime.datetime | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    updated_from: datetime.datetime | Unset = UNSET,
    updated_to: datetime.datetime | Unset = UNSET,

) -> Response[AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList]:
    """ List agents or create a new agent.

     Retrieve a list of agents or create a new agent.

    Args:
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        creator_id (list[int] | Unset):
        engine_class_id (list[str] | Unset):
        exclude_engine_class_id (str | Unset):
        include_job_stats (bool | Unset):
        include_untagged (bool | Unset):
        job_count_max (int | Unset):
        job_count_min (int | Unset):
        most_recent_job_from (datetime.datetime | Unset):
        most_recent_job_to (datetime.datetime | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        tags (list[str] | Unset):
        updated_from (datetime.datetime | Unset):
        updated_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList]
     """


    kwargs = _get_kwargs(
        created_from=created_from,
created_to=created_to,
creator_id=creator_id,
engine_class_id=engine_class_id,
exclude_engine_class_id=exclude_engine_class_id,
include_job_stats=include_job_stats,
include_untagged=include_untagged,
job_count_max=job_count_max,
job_count_min=job_count_min,
most_recent_job_from=most_recent_job_from,
most_recent_job_to=most_recent_job_to,
name=name,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,
tags=tags,
updated_from=updated_from,
updated_to=updated_to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    creator_id: list[int] | Unset = UNSET,
    engine_class_id: list[str] | Unset = UNSET,
    exclude_engine_class_id: str | Unset = UNSET,
    include_job_stats: bool | Unset = UNSET,
    include_untagged: bool | Unset = UNSET,
    job_count_max: int | Unset = UNSET,
    job_count_min: int | Unset = UNSET,
    most_recent_job_from: datetime.datetime | Unset = UNSET,
    most_recent_job_to: datetime.datetime | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    updated_from: datetime.datetime | Unset = UNSET,
    updated_to: datetime.datetime | Unset = UNSET,

) -> AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList | None:
    """ List agents or create a new agent.

     Retrieve a list of agents or create a new agent.

    Args:
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        creator_id (list[int] | Unset):
        engine_class_id (list[str] | Unset):
        exclude_engine_class_id (str | Unset):
        include_job_stats (bool | Unset):
        include_untagged (bool | Unset):
        job_count_max (int | Unset):
        job_count_min (int | Unset):
        most_recent_job_from (datetime.datetime | Unset):
        most_recent_job_to (datetime.datetime | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        tags (list[str] | Unset):
        updated_from (datetime.datetime | Unset):
        updated_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList
     """


    return sync_detailed(
        client=client,
created_from=created_from,
created_to=created_to,
creator_id=creator_id,
engine_class_id=engine_class_id,
exclude_engine_class_id=exclude_engine_class_id,
include_job_stats=include_job_stats,
include_untagged=include_untagged,
job_count_max=job_count_max,
job_count_min=job_count_min,
most_recent_job_from=most_recent_job_from,
most_recent_job_to=most_recent_job_to,
name=name,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,
tags=tags,
updated_from=updated_from,
updated_to=updated_to,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    creator_id: list[int] | Unset = UNSET,
    engine_class_id: list[str] | Unset = UNSET,
    exclude_engine_class_id: str | Unset = UNSET,
    include_job_stats: bool | Unset = UNSET,
    include_untagged: bool | Unset = UNSET,
    job_count_max: int | Unset = UNSET,
    job_count_min: int | Unset = UNSET,
    most_recent_job_from: datetime.datetime | Unset = UNSET,
    most_recent_job_to: datetime.datetime | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    updated_from: datetime.datetime | Unset = UNSET,
    updated_to: datetime.datetime | Unset = UNSET,

) -> Response[AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList]:
    """ List agents or create a new agent.

     Retrieve a list of agents or create a new agent.

    Args:
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        creator_id (list[int] | Unset):
        engine_class_id (list[str] | Unset):
        exclude_engine_class_id (str | Unset):
        include_job_stats (bool | Unset):
        include_untagged (bool | Unset):
        job_count_max (int | Unset):
        job_count_min (int | Unset):
        most_recent_job_from (datetime.datetime | Unset):
        most_recent_job_to (datetime.datetime | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        tags (list[str] | Unset):
        updated_from (datetime.datetime | Unset):
        updated_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList]
     """


    kwargs = _get_kwargs(
        created_from=created_from,
created_to=created_to,
creator_id=creator_id,
engine_class_id=engine_class_id,
exclude_engine_class_id=exclude_engine_class_id,
include_job_stats=include_job_stats,
include_untagged=include_untagged,
job_count_max=job_count_max,
job_count_min=job_count_min,
most_recent_job_from=most_recent_job_from,
most_recent_job_to=most_recent_job_to,
name=name,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,
tags=tags,
updated_from=updated_from,
updated_to=updated_to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    creator_id: list[int] | Unset = UNSET,
    engine_class_id: list[str] | Unset = UNSET,
    exclude_engine_class_id: str | Unset = UNSET,
    include_job_stats: bool | Unset = UNSET,
    include_untagged: bool | Unset = UNSET,
    job_count_max: int | Unset = UNSET,
    job_count_min: int | Unset = UNSET,
    most_recent_job_from: datetime.datetime | Unset = UNSET,
    most_recent_job_to: datetime.datetime | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_id: UUID,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    updated_from: datetime.datetime | Unset = UNSET,
    updated_to: datetime.datetime | Unset = UNSET,

) -> AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList | None:
    """ List agents or create a new agent.

     Retrieve a list of agents or create a new agent.

    Args:
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        creator_id (list[int] | Unset):
        engine_class_id (list[str] | Unset):
        exclude_engine_class_id (str | Unset):
        include_job_stats (bool | Unset):
        include_untagged (bool | Unset):
        job_count_max (int | Unset):
        job_count_min (int | Unset):
        most_recent_job_from (datetime.datetime | Unset):
        most_recent_job_to (datetime.datetime | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        tags (list[str] | Unset):
        updated_from (datetime.datetime | Unset):
        updated_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsListResponse400 | ErrorDetailResponse | PaginatedBaseAgentList
     """


    return (await asyncio_detailed(
        client=client,
created_from=created_from,
created_to=created_to,
creator_id=creator_id,
engine_class_id=engine_class_id,
exclude_engine_class_id=exclude_engine_class_id,
include_job_stats=include_job_stats,
include_untagged=include_untagged,
job_count_max=job_count_max,
job_count_min=job_count_min,
most_recent_job_from=most_recent_job_from,
most_recent_job_to=most_recent_job_to,
name=name,
ordering=ordering,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,
tags=tags,
updated_from=updated_from,
updated_to=updated_to,

    )).parsed
