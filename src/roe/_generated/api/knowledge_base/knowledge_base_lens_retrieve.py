from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from uuid import UUID



def _get_kwargs(
    atlas_lens_id: str,
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
        "url": "/v1/knowledge-base/lens/{atlas_lens_id}/".format(atlas_lens_id=quote(str(atlas_lens_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    atlas_lens_id: str,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any]:
    r"""  Fetch a lens directly from Atlas by its atlas_lens_id and return the
    names-only projection. Does NOT require a KnowledgeBase row to exist.

    If a KnowledgeBase row for this org already points to the given
    atlas_lens_id, it is also synced (best-effort) and returned under
    the \"knowledge_base\" key.

    GET  /knowledge-base/lens/<atlas_lens_id>/

    Args:
        atlas_lens_id (str):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        atlas_lens_id=atlas_lens_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    atlas_lens_id: str,
    *,
    client: AuthenticatedClient,
    organization_id: UUID | Unset = UNSET,

) -> Response[Any]:
    r"""  Fetch a lens directly from Atlas by its atlas_lens_id and return the
    names-only projection. Does NOT require a KnowledgeBase row to exist.

    If a KnowledgeBase row for this org already points to the given
    atlas_lens_id, it is also synced (best-effort) and returned under
    the \"knowledge_base\" key.

    GET  /knowledge-base/lens/<atlas_lens_id>/

    Args:
        atlas_lens_id (str):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        atlas_lens_id=atlas_lens_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

