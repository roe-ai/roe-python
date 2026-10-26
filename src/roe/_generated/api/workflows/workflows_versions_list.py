from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_workflow_version_list import PaginatedWorkflowVersionList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    workflow_id: UUID,
    *,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows/{workflow_id}/versions/".format(workflow_id=quote(str(workflow_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedWorkflowVersionList | None:
    if response.status_code == 200:
        response_200 = PaginatedWorkflowVersionList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedWorkflowVersionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[PaginatedWorkflowVersionList]:
    """ List workflow versions

     List a workflow's versions, newest first.

    Args:
        workflow_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkflowVersionList]
     """


    kwargs = _get_kwargs(
        workflow_id=workflow_id,
page=page,
page_size=page_size,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    workflow_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> PaginatedWorkflowVersionList | None:
    """ List workflow versions

     List a workflow's versions, newest first.

    Args:
        workflow_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkflowVersionList
     """


    return sync_detailed(
        workflow_id=workflow_id,
client=client,
page=page,
page_size=page_size,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    workflow_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[PaginatedWorkflowVersionList]:
    """ List workflow versions

     List a workflow's versions, newest first.

    Args:
        workflow_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkflowVersionList]
     """


    kwargs = _get_kwargs(
        workflow_id=workflow_id,
page=page,
page_size=page_size,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    workflow_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> PaginatedWorkflowVersionList | None:
    """ List workflow versions

     List a workflow's versions, newest first.

    Args:
        workflow_id (UUID):
        page (int | Unset):
        page_size (int | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkflowVersionList
     """


    return (await asyncio_detailed(
        workflow_id=workflow_id,
client=client,
page=page,
page_size=page_size,
organization_id=organization_id,

    )).parsed
