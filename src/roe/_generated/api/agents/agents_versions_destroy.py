from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.qdrant_cleanup_error_response import QdrantCleanupErrorResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_id: UUID,
    agent_version_id: UUID,
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
        "method": "delete",
        "url": "/v1/agents/{agent_id}/versions/{agent_version_id}/".format(agent_id=quote(str(agent_id), safe=""),agent_version_id=quote(str(agent_version_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorDetailResponse | QdrantCleanupErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = ErrorDetailResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = QdrantCleanupErrorResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorDetailResponse | QdrantCleanupErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | ErrorDetailResponse | QdrantCleanupErrorResponse]:
    """ Delete an agent version.

     Delete a specific agent version.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDetailResponse | QdrantCleanupErrorResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
agent_version_id=agent_version_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Any | ErrorDetailResponse | QdrantCleanupErrorResponse | None:
    """ Delete an agent version.

     Delete a specific agent version.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDetailResponse | QdrantCleanupErrorResponse
     """


    return sync_detailed(
        agent_id=agent_id,
agent_version_id=agent_version_id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | ErrorDetailResponse | QdrantCleanupErrorResponse]:
    """ Delete an agent version.

     Delete a specific agent version.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDetailResponse | QdrantCleanupErrorResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
agent_version_id=agent_version_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: UUID,
    agent_version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Any | ErrorDetailResponse | QdrantCleanupErrorResponse | None:
    """ Delete an agent version.

     Delete a specific agent version.

    Args:
        agent_id (UUID):
        agent_version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDetailResponse | QdrantCleanupErrorResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
agent_version_id=agent_version_id,
client=client,
organization_id=organization_id,

    )).parsed
