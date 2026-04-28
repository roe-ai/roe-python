from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_import_export_request import AgentImportExportRequest
from ...models.agent_version import AgentVersion
from ...models.error_response import ErrorResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body:    AgentImportExportRequest  |     AgentImportExportRequest  |     AgentImportExportRequest  | Unset = UNSET,
    organization_id: UUID,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/agents/import/",
        "params": params,
    }

    if isinstance(body, AgentImportExportRequest):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentImportExportRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AgentImportExportRequest):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentVersion | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = AgentVersion.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentVersion | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    AgentImportExportRequest  |     AgentImportExportRequest  |     AgentImportExportRequest  | Unset = UNSET,
    organization_id: UUID,

) -> Response[AgentVersion | ErrorResponse]:
    """ Import an agent configuration.

     Import an agent configuration from exported JSON, creating a new agent in the specified
    organization.

    Args:
        organization_id (UUID):
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVersion | ErrorResponse]
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
    client: AuthenticatedClient | Client,
    body:    AgentImportExportRequest  |     AgentImportExportRequest  |     AgentImportExportRequest  | Unset = UNSET,
    organization_id: UUID,

) -> AgentVersion | ErrorResponse | None:
    """ Import an agent configuration.

     Import an agent configuration from exported JSON, creating a new agent in the specified
    organization.

    Args:
        organization_id (UUID):
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVersion | ErrorResponse
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body:    AgentImportExportRequest  |     AgentImportExportRequest  |     AgentImportExportRequest  | Unset = UNSET,
    organization_id: UUID,

) -> Response[AgentVersion | ErrorResponse]:
    """ Import an agent configuration.

     Import an agent configuration from exported JSON, creating a new agent in the specified
    organization.

    Args:
        organization_id (UUID):
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentVersion | ErrorResponse]
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
    client: AuthenticatedClient | Client,
    body:    AgentImportExportRequest  |     AgentImportExportRequest  |     AgentImportExportRequest  | Unset = UNSET,
    organization_id: UUID,

) -> AgentVersion | ErrorResponse | None:
    """ Import an agent configuration.

     Import an agent configuration from exported JSON, creating a new agent in the specified
    organization.

    Args:
        organization_id (UUID):
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export
        body (AgentImportExportRequest): Serializer for agent data shared by import and export

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentVersion | ErrorResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
