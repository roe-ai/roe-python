from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_jobs_references_retrieve_response_400_type_1 import AgentsJobsReferencesRetrieveResponse400Type1
from ...models.agents_jobs_references_retrieve_response_400_type_2 import AgentsJobsReferencesRetrieveResponse400Type2
from ...models.api_error_response import ApiErrorResponse
from ...models.error_detail_response import ErrorDetailResponse
from ...types import File, FileTypes
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast
from uuid import UUID



def _get_kwargs(
    agent_job_id: UUID,
    resource_id: str,
    *,
    download: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["download"] = download

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/jobs/{agent_job_id}/references/{resource_id}/".format(agent_job_id=quote(str(agent_job_id), safe=""),resource_id=quote(str(resource_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File | None:
    if response.status_code == 200:
        response_200 = File(
             payload = BytesIO(response.content)
        )



        return response_200

    if response.status_code == 206:
        response_206 = File(
             payload = BytesIO(response.content)
        )



        return response_206

    if response.status_code == 400:
        def _parse_response_400(data: object) -> AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str]:
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
                response_400_type_1 = AgentsJobsReferencesRetrieveResponse400Type1.from_dict(data)



                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = AgentsJobsReferencesRetrieveResponse400Type2.from_dict(data)



            return response_400_type_2

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorDetailResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if response.status_code == 416:
        response_416 = ApiErrorResponse.from_dict(response.json())



        return response_416

    if response.status_code == 500:
        response_500 = ApiErrorResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_job_id: UUID,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    download: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File]:
    """  Serve a reference file associated with an agent job.

    Args:
        agent_job_id (UUID):
        resource_id (str):
        download (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File]
     """


    kwargs = _get_kwargs(
        agent_job_id=agent_job_id,
resource_id=resource_id,
download=download,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_job_id: UUID,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    download: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File | None:
    """  Serve a reference file associated with an agent job.

    Args:
        agent_job_id (UUID):
        resource_id (str):
        download (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File
     """


    return sync_detailed(
        agent_job_id=agent_job_id,
resource_id=resource_id,
client=client,
download=download,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    agent_job_id: UUID,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    download: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File]:
    """  Serve a reference file associated with an agent job.

    Args:
        agent_job_id (UUID):
        resource_id (str):
        download (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File]
     """


    kwargs = _get_kwargs(
        agent_job_id=agent_job_id,
resource_id=resource_id,
download=download,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_job_id: UUID,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    download: bool | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File | None:
    """  Serve a reference file associated with an agent job.

    Args:
        agent_job_id (UUID):
        resource_id (str):
        download (bool | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsJobsReferencesRetrieveResponse400Type1 | AgentsJobsReferencesRetrieveResponse400Type2 | list[str] | ApiErrorResponse | ErrorDetailResponse | File
     """


    return (await asyncio_detailed(
        agent_job_id=agent_job_id,
resource_id=resource_id,
client=client,
download=download,
organization_id=organization_id,

    )).parsed
