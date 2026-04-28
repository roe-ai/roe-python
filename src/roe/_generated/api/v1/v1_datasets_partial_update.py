from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dataset import Dataset
from ...models.patched_dataset_request import PatchedDatasetRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    dataset_id: UUID,
    *,
    body:    PatchedDatasetRequest  |     PatchedDatasetRequest  |     PatchedDatasetRequest  | Unset = UNSET,
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
        "method": "patch",
        "url": "/v1/datasets/{dataset_id}/".format(dataset_id=quote(str(dataset_id), safe=""),),
        "params": params,
    }

    if isinstance(body, PatchedDatasetRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedDatasetRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedDatasetRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dataset | None:
    if response.status_code == 200:
        response_200 = Dataset.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Dataset]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedDatasetRequest  |     PatchedDatasetRequest  |     PatchedDatasetRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[Dataset]:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dataset]
     """


    kwargs = _get_kwargs(
        dataset_id=dataset_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedDatasetRequest  |     PatchedDatasetRequest  |     PatchedDatasetRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Dataset | None:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dataset
     """


    return sync_detailed(
        dataset_id=dataset_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedDatasetRequest  |     PatchedDatasetRequest  |     PatchedDatasetRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[Dataset]:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dataset]
     """


    kwargs = _get_kwargs(
        dataset_id=dataset_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    PatchedDatasetRequest  |     PatchedDatasetRequest  |     PatchedDatasetRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Dataset | None:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        dataset_id (UUID):
        organization_id (UUID | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):
        body (PatchedDatasetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dataset
     """


    return (await asyncio_detailed(
        dataset_id=dataset_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
