from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.policy_version import PolicyVersion
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    policy_id: UUID,
    version_id: UUID,
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
        "url": "/v1/policies/{policy_id}/versions/{version_id}/".format(policy_id=quote(str(policy_id), safe=""),version_id=quote(str(version_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorDetailResponse | PolicyVersion | None:
    if response.status_code == 200:
        response_200 = PolicyVersion.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorDetailResponse | PolicyVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | PolicyVersion]:
    """  Get a specific policy version by policy_id and version_id.
    Used for nested URL pattern: /policies/{policy_id}/versions/{version_id}/

    Args:
        policy_id (UUID):
        version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | PolicyVersion]
     """


    kwargs = _get_kwargs(
        policy_id=policy_id,
version_id=version_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    policy_id: UUID,
    version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | PolicyVersion | None:
    """  Get a specific policy version by policy_id and version_id.
    Used for nested URL pattern: /policies/{policy_id}/versions/{version_id}/

    Args:
        policy_id (UUID):
        version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | PolicyVersion
     """


    return sync_detailed(
        policy_id=policy_id,
version_id=version_id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    policy_id: UUID,
    version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | PolicyVersion]:
    """  Get a specific policy version by policy_id and version_id.
    Used for nested URL pattern: /policies/{policy_id}/versions/{version_id}/

    Args:
        policy_id (UUID):
        version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | PolicyVersion]
     """


    kwargs = _get_kwargs(
        policy_id=policy_id,
version_id=version_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    policy_id: UUID,
    version_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | PolicyVersion | None:
    """  Get a specific policy version by policy_id and version_id.
    Used for nested URL pattern: /policies/{policy_id}/versions/{version_id}/

    Args:
        policy_id (UUID):
        version_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | PolicyVersion
     """


    return (await asyncio_detailed(
        policy_id=policy_id,
version_id=version_id,
client=client,
organization_id=organization_id,

    )).parsed
