from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_workflow_list import PaginatedWorkflowList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    agent_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_agent_id: str | Unset = UNSET
    if not isinstance(agent_id, Unset):
        json_agent_id = str(agent_id)
    params["agent_id"] = json_agent_id

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows/",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedWorkflowList | None:
    if response.status_code == 200:
        response_200 = PaginatedWorkflowList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedWorkflowList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    agent_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[PaginatedWorkflowList]:
    """ List workflows

     List the organization's workflows, most recently updated first.

    Args:
        agent_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkflowList]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
page=page,
page_size=page_size,
search=search,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    agent_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> PaginatedWorkflowList | None:
    """ List workflows

     List the organization's workflows, most recently updated first.

    Args:
        agent_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkflowList
     """


    return sync_detailed(
        client=client,
agent_id=agent_id,
page=page,
page_size=page_size,
search=search,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    agent_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[PaginatedWorkflowList]:
    """ List workflows

     List the organization's workflows, most recently updated first.

    Args:
        agent_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkflowList]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
page=page,
page_size=page_size,
search=search,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    agent_id: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> PaginatedWorkflowList | None:
    """ List workflows

     List the organization's workflows, most recently updated first.

    Args:
        agent_id (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkflowList
     """


    return (await asyncio_detailed(
        client=client,
agent_id=agent_id,
page=page,
page_size=page_size,
search=search,
organization_id=organization_id,

    )).parsed
