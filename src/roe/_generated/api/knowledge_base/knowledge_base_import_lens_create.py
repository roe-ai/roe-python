from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.knowledge_base import KnowledgeBase
from ...models.knowledge_base_import_lens_create_body import KnowledgeBaseImportLensCreateBody
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body: KnowledgeBaseImportLensCreateBody | Unset = UNSET,
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
        "url": "/v1/knowledge-base/import-lens/",
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

    if response.status_code == 201:
        response_201 = KnowledgeBase.from_dict(response.json())



        return response_201

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
    *,
    client: AuthenticatedClient,
    body: KnowledgeBaseImportLensCreateBody | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[KnowledgeBase]:
    """  Import a finalized Atlas lens into roe-main by its atlas_lens_id.
    Creates a KnowledgeBase row in active state with the lens snapshot —
    no draft involved.

    POST /knowledge-base/import-lens/   body: { atlas_lens_id }

    Idempotent: if a row for this org already points to the same
    atlas_lens_id the existing record is synced and returned (200).

    Args:
        organization_id (UUID | Unset):
        body (KnowledgeBaseImportLensCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeBase]
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
    body: KnowledgeBaseImportLensCreateBody | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> KnowledgeBase | None:
    """  Import a finalized Atlas lens into roe-main by its atlas_lens_id.
    Creates a KnowledgeBase row in active state with the lens snapshot —
    no draft involved.

    POST /knowledge-base/import-lens/   body: { atlas_lens_id }

    Idempotent: if a row for this org already points to the same
    atlas_lens_id the existing record is synced and returned (200).

    Args:
        organization_id (UUID | Unset):
        body (KnowledgeBaseImportLensCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeBase
     """


    return sync_detailed(
        client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: KnowledgeBaseImportLensCreateBody | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[KnowledgeBase]:
    """  Import a finalized Atlas lens into roe-main by its atlas_lens_id.
    Creates a KnowledgeBase row in active state with the lens snapshot —
    no draft involved.

    POST /knowledge-base/import-lens/   body: { atlas_lens_id }

    Idempotent: if a row for this org already points to the same
    atlas_lens_id the existing record is synced and returned (200).

    Args:
        organization_id (UUID | Unset):
        body (KnowledgeBaseImportLensCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeBase]
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
    body: KnowledgeBaseImportLensCreateBody | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> KnowledgeBase | None:
    """  Import a finalized Atlas lens into roe-main by its atlas_lens_id.
    Creates a KnowledgeBase row in active state with the lens snapshot —
    no draft involved.

    POST /knowledge-base/import-lens/   body: { atlas_lens_id }

    Idempotent: if a row for this org already points to the same
    atlas_lens_id the existing record is synced and returned (200).

    Args:
        organization_id (UUID | Unset):
        body (KnowledgeBaseImportLensCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeBase
     """


    return (await asyncio_detailed(
        client=client,
body=body,
organization_id=organization_id,

    )).parsed
