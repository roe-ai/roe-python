from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.public_skill_set_generation import PublicSkillSetGeneration
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    skill_set_id: UUID,
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
        "url": "/v1/skills/{skill_set_id}/generation/".format(skill_set_id=quote(str(skill_set_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PublicSkillSetGeneration | None:
    if response.status_code == 200:
        response_200 = PublicSkillSetGeneration.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PublicSkillSetGeneration]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    skill_set_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[PublicSkillSetGeneration]:
    """  Returns the last generation and its status, or generation: null when no run exists.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublicSkillSetGeneration]
     """


    kwargs = _get_kwargs(
        skill_set_id=skill_set_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    skill_set_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> PublicSkillSetGeneration | None:
    """  Returns the last generation and its status, or generation: null when no run exists.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublicSkillSetGeneration
     """


    return sync_detailed(
        skill_set_id=skill_set_id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    skill_set_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[PublicSkillSetGeneration]:
    """  Returns the last generation and its status, or generation: null when no run exists.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublicSkillSetGeneration]
     """


    kwargs = _get_kwargs(
        skill_set_id=skill_set_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    skill_set_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> PublicSkillSetGeneration | None:
    """  Returns the last generation and its status, or generation: null when no run exists.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublicSkillSetGeneration
     """


    return (await asyncio_detailed(
        skill_set_id=skill_set_id,
client=client,
organization_id=organization_id,

    )).parsed
