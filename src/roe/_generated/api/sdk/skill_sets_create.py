from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_skill_set import CreateSkillSet
from ...models.create_skill_set_request import CreateSkillSetRequest
from ...models.skill_sets_create_response_400 import SkillSetsCreateResponse400
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body: CreateSkillSetRequest,
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
        "url": "/v1/skills/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateSkillSet | SkillSetsCreateResponse400 | None:
    if response.status_code == 201:
        response_201 = CreateSkillSet.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = SkillSetsCreateResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateSkillSet | SkillSetsCreateResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSkillSetRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[CreateSkillSet | SkillSetsCreateResponse400]:
    """  List the org's skill sets and create a new one.

    Args:
        organization_id (UUID | Unset):
        body (CreateSkillSetRequest): Create a new skill set. Its version 0 is always the base
            skill.

            Every set starts from the same built-in base content; customization happens
            by creating a new version on top of it (``POST .../versions/``), which is
            also what makes the edit downloadable and rollback-able.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSkillSet | SkillSetsCreateResponse400]
     """


    kwargs = _get_kwargs(
        body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CreateSkillSetRequest,
    organization_id: UUID | Unset = UNSET,

) -> CreateSkillSet | SkillSetsCreateResponse400 | None:
    """  List the org's skill sets and create a new one.

    Args:
        organization_id (UUID | Unset):
        body (CreateSkillSetRequest): Create a new skill set. Its version 0 is always the base
            skill.

            Every set starts from the same built-in base content; customization happens
            by creating a new version on top of it (``POST .../versions/``), which is
            also what makes the edit downloadable and rollback-able.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSkillSet | SkillSetsCreateResponse400
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSkillSetRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[CreateSkillSet | SkillSetsCreateResponse400]:
    """  List the org's skill sets and create a new one.

    Args:
        organization_id (UUID | Unset):
        body (CreateSkillSetRequest): Create a new skill set. Its version 0 is always the base
            skill.

            Every set starts from the same built-in base content; customization happens
            by creating a new version on top of it (``POST .../versions/``), which is
            also what makes the edit downloadable and rollback-able.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSkillSet | SkillSetsCreateResponse400]
     """


    kwargs = _get_kwargs(
        body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateSkillSetRequest,
    organization_id: UUID | Unset = UNSET,

) -> CreateSkillSet | SkillSetsCreateResponse400 | None:
    """  List the org's skill sets and create a new one.

    Args:
        organization_id (UUID | Unset):
        body (CreateSkillSetRequest): Create a new skill set. Its version 0 is always the base
            skill.

            Every set starts from the same built-in base content; customization happens
            by creating a new version on top of it (``POST .../versions/``), which is
            also what makes the edit downloadable and rollback-able.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSkillSet | SkillSetsCreateResponse400
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
