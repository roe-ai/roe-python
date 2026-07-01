from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.draft import Draft
from ...models.regenerate_request import RegenerateRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: RegenerateRequest | Unset = UNSET,
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
        "url": "/v1/knowledge-base/{id}/regenerate/".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Draft | None:
    if response.status_code == 202:
        response_202 = Draft.from_dict(response.json())



        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Draft]:
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
    body: RegenerateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[Draft]:
    """  Kick off another async generation round with feedback.
    Operation sync: propagate atlas errors; finally reconcile.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (RegenerateRequest | Unset): Body for POST /knowledge-base/<id>/regenerate/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Draft]
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
    body: RegenerateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Draft | None:
    """  Kick off another async generation round with feedback.
    Operation sync: propagate atlas errors; finally reconcile.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (RegenerateRequest | Unset): Body for POST /knowledge-base/<id>/regenerate/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Draft
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
    body: RegenerateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Response[Draft]:
    """  Kick off another async generation round with feedback.
    Operation sync: propagate atlas errors; finally reconcile.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (RegenerateRequest | Unset): Body for POST /knowledge-base/<id>/regenerate/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Draft]
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
    body: RegenerateRequest | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,

) -> Draft | None:
    """  Kick off another async generation round with feedback.
    Operation sync: propagate atlas errors; finally reconcile.

    Args:
        id (UUID):
        organization_id (UUID | Unset):
        body (RegenerateRequest | Unset): Body for POST /knowledge-base/<id>/regenerate/.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Draft
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
