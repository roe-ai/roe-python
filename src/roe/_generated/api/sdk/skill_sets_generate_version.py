from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...models.generate_skill_set_version_request import GenerateSkillSetVersionRequest
from ...models.generate_skill_set_version_response import GenerateSkillSetVersionResponse
from ...models.skill_sets_generate_version_response_400 import SkillSetsGenerateVersionResponse400
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    skill_set_id: UUID,
    *,
    body: GenerateSkillSetVersionRequest,
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
        "url": "/v1/skills/{skill_set_id}/generate-version/".format(skill_set_id=quote(str(skill_set_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400 | None:
    if response.status_code == 200:
        response_200 = GenerateSkillSetVersionResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SkillSetsGenerateVersionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400]:
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
    body: GenerateSkillSetVersionRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400]:
    """  Author the next version of a skill set with an agent.

    Starts the generation workflow and returns where to stream it. The agent
    reads the customer's use case, profiles the linked tables, reads the
    attached CSVs and documents, and rewrites the customer layer of the skill.

    Nothing is written here: the generated file set comes back for review and is
    saved through the normal version-create path, so a generated skill only ever
    becomes live because a person accepted it.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):
        body (GenerateSkillSetVersionRequest): Request to author the next version of a skill set
            with an agent.

            ``base_version_id`` is the version the draft is derived from; omit it to
            start from the set's current version. By default nothing here writes a
            version — the generated file set comes back for review and is saved
            through the normal version-create path. With ``auto_commit`` the workflow
            saves it itself on success, through that same path. At least one table name
            or attachment is required; a use case or policy alone is not a data source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400]
     """


    kwargs = _get_kwargs(
        skill_set_id=skill_set_id,
body=body,
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
    body: GenerateSkillSetVersionRequest,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400 | None:
    """  Author the next version of a skill set with an agent.

    Starts the generation workflow and returns where to stream it. The agent
    reads the customer's use case, profiles the linked tables, reads the
    attached CSVs and documents, and rewrites the customer layer of the skill.

    Nothing is written here: the generated file set comes back for review and is
    saved through the normal version-create path, so a generated skill only ever
    becomes live because a person accepted it.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):
        body (GenerateSkillSetVersionRequest): Request to author the next version of a skill set
            with an agent.

            ``base_version_id`` is the version the draft is derived from; omit it to
            start from the set's current version. By default nothing here writes a
            version — the generated file set comes back for review and is saved
            through the normal version-create path. With ``auto_commit`` the workflow
            saves it itself on success, through that same path. At least one table name
            or attachment is required; a use case or policy alone is not a data source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400
     """


    return sync_detailed(
        skill_set_id=skill_set_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    skill_set_id: UUID,
    *,
    client: AuthenticatedClient,
    body: GenerateSkillSetVersionRequest,
    organization_id: UUID | Unset = UNSET,

) -> Response[ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400]:
    """  Author the next version of a skill set with an agent.

    Starts the generation workflow and returns where to stream it. The agent
    reads the customer's use case, profiles the linked tables, reads the
    attached CSVs and documents, and rewrites the customer layer of the skill.

    Nothing is written here: the generated file set comes back for review and is
    saved through the normal version-create path, so a generated skill only ever
    becomes live because a person accepted it.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):
        body (GenerateSkillSetVersionRequest): Request to author the next version of a skill set
            with an agent.

            ``base_version_id`` is the version the draft is derived from; omit it to
            start from the set's current version. By default nothing here writes a
            version — the generated file set comes back for review and is saved
            through the normal version-create path. With ``auto_commit`` the workflow
            saves it itself on success, through that same path. At least one table name
            or attachment is required; a use case or policy alone is not a data source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400]
     """


    kwargs = _get_kwargs(
        skill_set_id=skill_set_id,
body=body,
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
    body: GenerateSkillSetVersionRequest,
    organization_id: UUID | Unset = UNSET,

) -> ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400 | None:
    """  Author the next version of a skill set with an agent.

    Starts the generation workflow and returns where to stream it. The agent
    reads the customer's use case, profiles the linked tables, reads the
    attached CSVs and documents, and rewrites the customer layer of the skill.

    Nothing is written here: the generated file set comes back for review and is
    saved through the normal version-create path, so a generated skill only ever
    becomes live because a person accepted it.

    Args:
        skill_set_id (UUID):
        organization_id (UUID | Unset):
        body (GenerateSkillSetVersionRequest): Request to author the next version of a skill set
            with an agent.

            ``base_version_id`` is the version the draft is derived from; omit it to
            start from the set's current version. By default nothing here writes a
            version — the generated file set comes back for review and is saved
            through the normal version-create path. With ``auto_commit`` the workflow
            saves it itself on success, through that same path. At least one table name
            or attachment is required; a use case or policy alone is not a data source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetailResponse | GenerateSkillSetVersionResponse | SkillSetsGenerateVersionResponse400
     """


    return (await asyncio_detailed(
        skill_set_id=skill_set_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
