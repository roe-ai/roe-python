from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.finalize_request import FinalizeRequest
from ...models.knowledge_base import KnowledgeBase
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: FinalizeRequest | Unset = UNSET,
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
        "url": "/v1/knowledge-base/{id}/finalize/".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> KnowledgeBase | None:
    if response.status_code == 200:
        response_200 = KnowledgeBase.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[KnowledgeBase]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FinalizeRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[KnowledgeBase]:
    """  Commit the agreed selection into a lens and mark the KB active.
    Operation sync: strict — propagate atlas errors; reconcile in finally.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (FinalizeRequest | Unset): Body for POST /knowledge-base/<id>/finalize/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeBase]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FinalizeRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> KnowledgeBase | None:
    """  Commit the agreed selection into a lens and mark the KB active.
    Operation sync: strict — propagate atlas errors; reconcile in finally.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (FinalizeRequest | Unset): Body for POST /knowledge-base/<id>/finalize/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeBase
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FinalizeRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[KnowledgeBase]:
    """  Commit the agreed selection into a lens and mark the KB active.
    Operation sync: strict — propagate atlas errors; reconcile in finally.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (FinalizeRequest | Unset): Body for POST /knowledge-base/<id>/finalize/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeBase]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FinalizeRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> KnowledgeBase | None:
    """  Commit the agreed selection into a lens and mark the KB active.
    Operation sync: strict — propagate atlas errors; reconcile in finally.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (FinalizeRequest | Unset): Body for POST /knowledge-base/<id>/finalize/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeBase
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
