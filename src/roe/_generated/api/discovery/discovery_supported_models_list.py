from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET, Unset
from ... import errors

from ...models.supported_llm_model_list import SupportedLLMModelList



def _get_kwargs(
    *,
    capability: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["capability"] = capability


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/models/",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SupportedLLMModelList | None:
    if response.status_code == 200:
        response_200 = SupportedLLMModelList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SupportedLLMModelList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    capability: str | Unset = UNSET,

) -> Response[SupportedLLMModelList]:
    """ List supported model IDs

     Returns non-deprecated text-capable model IDs accepted in engine_config.model, with capability and
    context metadata. Use this before create_agent or create_agent_version when choosing a model. The
    list is tenant-agnostic and excludes customer-specific or deployment-specific providers.

    Args:
        capability (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportedLLMModelList]
     """


    kwargs = _get_kwargs(
        capability=capability,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    capability: str | Unset = UNSET,

) -> SupportedLLMModelList | None:
    """ List supported model IDs

     Returns non-deprecated text-capable model IDs accepted in engine_config.model, with capability and
    context metadata. Use this before create_agent or create_agent_version when choosing a model. The
    list is tenant-agnostic and excludes customer-specific or deployment-specific providers.

    Args:
        capability (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportedLLMModelList
     """


    return sync_detailed(
        client=client,
capability=capability,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    capability: str | Unset = UNSET,

) -> Response[SupportedLLMModelList]:
    """ List supported model IDs

     Returns non-deprecated text-capable model IDs accepted in engine_config.model, with capability and
    context metadata. Use this before create_agent or create_agent_version when choosing a model. The
    list is tenant-agnostic and excludes customer-specific or deployment-specific providers.

    Args:
        capability (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportedLLMModelList]
     """


    kwargs = _get_kwargs(
        capability=capability,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    capability: str | Unset = UNSET,

) -> SupportedLLMModelList | None:
    """ List supported model IDs

     Returns non-deprecated text-capable model IDs accepted in engine_config.model, with capability and
    context metadata. Use this before create_agent or create_agent_version when choosing a model. The
    list is tenant-agnostic and excludes customer-specific or deployment-specific providers.

    Args:
        capability (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportedLLMModelList
     """


    return (await asyncio_detailed(
        client=client,
capability=capability,

    )).parsed
