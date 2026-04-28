from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.webhook import Webhook
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
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
        "url": "/v1/webhooks/",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Webhook] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Webhook.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Webhook]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[list[Webhook]]:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Webhook]]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> list[Webhook] | None:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Webhook]
     """


    return sync_detailed(
        client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> Response[list[Webhook]]:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Webhook]]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,

) -> list[Webhook] | None:
    r"""  Mixin for organization access validation.

    Automatically resolves and validates organization access on every request,
    making the organization available as self.organization.

    For API key auth:  organization is derived from the key (no org_id param needed).
    For user auth:     organization_id must be provided in the request
                       (kwargs / headers / body / query params).

    Usage:
        class MyView(BaseOrganizationAccessMixin, APIView):
            def get(self, request):
                # self.organization is automatically available
                return Response({\"org\": self.organization.name})

    Args:
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Webhook]
     """


    return (await asyncio_detailed(
        client=client,
organization_id=organization_id,

    )).parsed
