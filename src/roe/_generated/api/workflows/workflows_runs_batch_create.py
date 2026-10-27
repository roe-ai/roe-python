from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.workflow_run_batch import WorkflowRunBatch
from ...models.workflow_run_batch_create_request import WorkflowRunBatchCreateRequest
from ...models.workflows_runs_batch_create_response_400_type_1 import WorkflowsRunsBatchCreateResponse400Type1
from ...models.workflows_runs_batch_create_response_400_type_2 import WorkflowsRunsBatchCreateResponse400Type2
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    workflow_id: UUID,
    *,
    body: WorkflowRunBatchCreateRequest,
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
        "url": "/v1/workflows/{workflow_id}/runs/batch/".format(workflow_id=quote(str(workflow_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2 | None:
    if response.status_code == 201:
        response_201 = WorkflowRunBatch.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        def _parse_response_400(data: object) -> list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2:
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
                response_400_type_1 = WorkflowsRunsBatchCreateResponse400Type1.from_dict(data)



                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = WorkflowsRunsBatchCreateResponse400Type2.from_dict(data)



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2]:
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
    body: WorkflowRunBatchCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2]:
    """ Run a workflow in batch

     Start one run per item of inputs.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2]
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
    body: WorkflowRunBatchCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2 | None:
    """ Run a workflow in batch

     Start one run per item of inputs.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2
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
    body: WorkflowRunBatchCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2]:
    """ Run a workflow in batch

     Start one run per item of inputs.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2]
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
    body: WorkflowRunBatchCreateRequest,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2 | None:
    """ Run a workflow in batch

     Start one run per item of inputs.

    Args:
        workflow_id (UUID):
        organization_id (UUID | Unset):
        body (WorkflowRunBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | WorkflowRunBatch | list[str] | WorkflowsRunsBatchCreateResponse400Type1 | WorkflowsRunsBatchCreateResponse400Type2
     """


    return (await asyncio_detailed(
        workflow_id=workflow_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
