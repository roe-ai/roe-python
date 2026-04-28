from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.paginated_file_list import PaginatedFileList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    dataset_id: UUID,
    *,
    organization_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["organization_id"] = organization_id

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/datasets/{dataset_id}/files/".format(dataset_id=quote(str(dataset_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | PaginatedFileList | None:
    if response.status_code == 200:
        response_200 = PaginatedFileList.from_dict(response.json())



        return response_200

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | PaginatedFileList]:
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
    organization_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[ErrorResponse | PaginatedFileList]:
    """ List files in a dataset.

     Retrieve a paginated list of files in a dataset with optional search filtering.

    Args:
        dataset_id (UUID):
        organization_id (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedFileList]
     """


    kwargs = _get_kwargs(
        dataset_id=dataset_id,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> ErrorResponse | PaginatedFileList | None:
    """ List files in a dataset.

     Retrieve a paginated list of files in a dataset with optional search filtering.

    Args:
        dataset_id (UUID):
        organization_id (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedFileList
     """


    return sync_detailed(
        dataset_id=dataset_id,
client=client,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    ).parsed

async def asyncio_detailed(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[ErrorResponse | PaginatedFileList]:
    """ List files in a dataset.

     Retrieve a paginated list of files in a dataset with optional search filtering.

    Args:
        dataset_id (UUID):
        organization_id (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaginatedFileList]
     """


    kwargs = _get_kwargs(
        dataset_id=dataset_id,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dataset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    organization_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,

) -> ErrorResponse | PaginatedFileList | None:
    """ List files in a dataset.

     Retrieve a paginated list of files in a dataset with optional search filtering.

    Args:
        dataset_id (UUID):
        organization_id (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaginatedFileList
     """


    return (await asyncio_detailed(
        dataset_id=dataset_id,
client=client,
organization_id=organization_id,
page=page,
page_size=page_size,
search=search,

    )).parsed
