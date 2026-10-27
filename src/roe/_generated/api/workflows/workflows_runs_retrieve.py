from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.workflow_run_detail import WorkflowRunDetail
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    run_id: UUID,
    *,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows/runs/{run_id}/".format(run_id=quote(str(run_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorDetailResponse | WorkflowRunDetail | None:
    if response.status_code == 200:
        response_200 = WorkflowRunDetail.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorDetailResponse | WorkflowRunDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | WorkflowRunDetail]:
    """ Get a workflow run

     Get a run with its outputs once it has finished, and what each step received and returned.

    Args:
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | WorkflowRunDetail]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | WorkflowRunDetail | None:
    """ Get a workflow run

     Get a run with its outputs once it has finished, and what each step received and returned.

    Args:
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | WorkflowRunDetail
     """


    return sync_detailed(
        run_id=run_id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | WorkflowRunDetail]:
    """ Get a workflow run

     Get a run with its outputs once it has finished, and what each step received and returned.

    Args:
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | WorkflowRunDetail]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | WorkflowRunDetail | None:
    """ Get a workflow run

     Get a run with its outputs once it has finished, and what each step received and returned.

    Args:
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | WorkflowRunDetail
     """


    return (await asyncio_detailed(
        run_id=run_id,
client=client,
organization_id=organization_id,

    )).parsed
