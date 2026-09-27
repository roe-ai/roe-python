from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_detail_response import ErrorDetailResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    skill_set_id: UUID,
    run_id: UUID,
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
        "url": "/v1/skills/{skill_set_id}/generation/{run_id}/".format(skill_set_id=quote(str(skill_set_id), safe=""),run_id=quote(str(run_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorDetailResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if response.status_code == 502:
        response_502 = ErrorDetailResponse.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    skill_set_id: UUID,
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | ErrorDetailResponse]:
    """ Stop tracking a generation, cancelling it if it is still running

     Used when the operator cancels, when a finished draft has been loaded into the editor, and when a
    run turns out to be unrecoverable. Cancelling a run that already finished is harmless.

    Args:
        skill_set_id (UUID):
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        skill_set_id=skill_set_id,
run_id=run_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    skill_set_id: UUID,
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Any | ErrorDetailResponse | None:
    """ Stop tracking a generation, cancelling it if it is still running

     Used when the operator cancels, when a finished draft has been loaded into the editor, and when a
    run turns out to be unrecoverable. Cancelling a run that already finished is harmless.

    Args:
        skill_set_id (UUID):
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDetailResponse
     """


    return sync_detailed(
        skill_set_id=skill_set_id,
run_id=run_id,
client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    skill_set_id: UUID,
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any | ErrorDetailResponse]:
    """ Stop tracking a generation, cancelling it if it is still running

     Used when the operator cancels, when a finished draft has been loaded into the editor, and when a
    run turns out to be unrecoverable. Cancelling a run that already finished is harmless.

    Args:
        skill_set_id (UUID):
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        skill_set_id=skill_set_id,
run_id=run_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    skill_set_id: UUID,
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Any | ErrorDetailResponse | None:
    """ Stop tracking a generation, cancelling it if it is still running

     Used when the operator cancels, when a finished draft has been loaded into the editor, and when a
    run turns out to be unrecoverable. Cancelling a run that already finished is harmless.

    Args:
        skill_set_id (UUID):
        run_id (UUID):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDetailResponse
     """


    return (await asyncio_detailed(
        skill_set_id=skill_set_id,
run_id=run_id,
client=client,
organization_id=organization_id,

    )).parsed
