from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_policy_version import CreatePolicyVersion
from ...models.create_policy_version_request import CreatePolicyVersionRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    policy_id: UUID,
    *,
    body:    CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  | Unset = UNSET,
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
        "url": "/v1/policies/{policy_id}/versions/".format(policy_id=quote(str(policy_id), safe=""),),
        "params": params,
    }

    if isinstance(body, CreatePolicyVersionRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePolicyVersionRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CreatePolicyVersionRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreatePolicyVersion | None:
    if response.status_code == 201:
        response_201 = CreatePolicyVersion.from_dict(response.json())



        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreatePolicyVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[CreatePolicyVersion]:
    """  Create a new policy version or list all versions of a specific policy

    Args:
        policy_id (UUID):
        organization_id (UUID | Unset):
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePolicyVersion]
     """


    kwargs = _get_kwargs(
        policy_id=policy_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> CreatePolicyVersion | None:
    """  Create a new policy version or list all versions of a specific policy

    Args:
        policy_id (UUID):
        organization_id (UUID | Unset):
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePolicyVersion
     """


    return sync_detailed(
        policy_id=policy_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[CreatePolicyVersion]:
    """  Create a new policy version or list all versions of a specific policy

    Args:
        policy_id (UUID):
        organization_id (UUID | Unset):
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePolicyVersion]
     """


    kwargs = _get_kwargs(
        policy_id=policy_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  |     CreatePolicyVersionRequest  | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> CreatePolicyVersion | None:
    """  Create a new policy version or list all versions of a specific policy

    Args:
        policy_id (UUID):
        organization_id (UUID | Unset):
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version
        body (CreatePolicyVersionRequest): Serializer for creating a new policy version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePolicyVersion
     """


    return (await asyncio_detailed(
        policy_id=policy_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
