from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.workflow_run_create_request import WorkflowRunCreateRequest
from ...models.workflow_run_detail import WorkflowRunDetail
from ...models.workflows_runs_create_response_400_type_1 import WorkflowsRunsCreateResponse400Type1
from ...models.workflows_runs_create_response_400_type_2 import WorkflowsRunsCreateResponse400Type2
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    workflow_id: UUID,
    *,
    body: WorkflowRunCreateRequest | Unset = UNSET,
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
        "url": "/v1/workflows/{workflow_id}/runs/".format(workflow_id=quote(str(workflow_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2 | None:
    if response.status_code == 201:
        response_201 = WorkflowRunDetail.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        def _parse_response_400(data: object) -> list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_400_type_0 = cast(list[str], data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_1 = WorkflowsRunsCreateResponse400Type1.from_dict(data)



                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = WorkflowsRunsCreateResponse400Type2.from_dict(data)



            return response_400_type_2

        response_400 = _parse_response_400(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2]:
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
    body: WorkflowRunCreateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2]:
    """ Run a workflow

     Start a run of the current version, or of version_id. With wait, the response comes when the run
    finishes or after 60 seconds, whichever is first.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2]
     """


    kwargs = _get_kwargs(
        workflow_id=workflow_id,
body=body,
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
    body: WorkflowRunCreateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2 | None:
    """ Run a workflow

     Start a run of the current version, or of version_id. With wait, the response comes when the run
    finishes or after 60 seconds, whichever is first.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2
     """


    return sync_detailed(
        workflow_id=workflow_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    workflow_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkflowRunCreateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2]:
    """ Run a workflow

     Start a run of the current version, or of version_id. With wait, the response comes when the run
    finishes or after 60 seconds, whichever is first.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2]
     """


    kwargs = _get_kwargs(
        workflow_id=workflow_id,
body=body,
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
    body: WorkflowRunCreateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2 | None:
    """ Run a workflow

     Start a run of the current version, or of version_id. With wait, the response comes when the run
    finishes or after 60 seconds, whichever is first.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | WorkflowRunDetail | list[str] | WorkflowsRunsCreateResponse400Type1 | WorkflowsRunsCreateResponse400Type2
     """


    return (await asyncio_detailed(
        workflow_id=workflow_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
