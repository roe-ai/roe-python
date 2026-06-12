from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connector_metadata import ConnectorMetadata
from ...models.error_detail_response import ErrorDetailResponse
from typing import cast



def _get_kwargs(
    connector_type: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connectors/{connector_type}/".format(connector_type=quote(str(connector_type), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectorMetadata | ErrorDetailResponse | None:
    if response.status_code == 200:
        response_200 = ConnectorMetadata.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ErrorDetailResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectorMetadata | ErrorDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connector_type: str,
    *,
    client: AuthenticatedClient,

) -> Response[ConnectorMetadata | ErrorDetailResponse]:
    """  Public API: GET /api/v1/connectors/{connector_type}/ - Get connector details.

    Args:
        connector_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorMetadata | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        connector_type=connector_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    connector_type: str,
    *,
    client: AuthenticatedClient,

) -> ConnectorMetadata | ErrorDetailResponse | None:
    """  Public API: GET /api/v1/connectors/{connector_type}/ - Get connector details.

    Args:
        connector_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorMetadata | ErrorDetailResponse
     """


    return sync_detailed(
        connector_type=connector_type,
client=client,

    ).parsed

async def asyncio_detailed(
    connector_type: str,
    *,
    client: AuthenticatedClient,

) -> Response[ConnectorMetadata | ErrorDetailResponse]:
    """  Public API: GET /api/v1/connectors/{connector_type}/ - Get connector details.

    Args:
        connector_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorMetadata | ErrorDetailResponse]
     """


    kwargs = _get_kwargs(
        connector_type=connector_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    connector_type: str,
    *,
    client: AuthenticatedClient,

) -> ConnectorMetadata | ErrorDetailResponse | None:
    """  Public API: GET /api/v1/connectors/{connector_type}/ - Get connector details.

    Args:
        connector_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorMetadata | ErrorDetailResponse
     """


    return (await asyncio_detailed(
        connector_type=connector_type,
client=client,

    )).parsed
