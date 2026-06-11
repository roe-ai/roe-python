from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connections_test_credentials_create_response_400_type_0 import ConnectionsTestCredentialsCreateResponse400Type0
from ...models.connections_test_credentials_create_response_400_type_1 import ConnectionsTestCredentialsCreateResponse400Type1
from ...models.test_connection import TestConnection
from ...models.test_connection_credentials_request import TestConnectionCredentialsRequest
from typing import cast



def _get_kwargs(
    *,
    body: TestConnectionCredentialsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connections/test-credentials/",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection | None:
    if response.status_code == 200:
        response_200 = TestConnection.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        def _parse_response_400(data: object) -> ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = ConnectionsTestCredentialsCreateResponse400Type0.from_dict(data)



                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_1 = ConnectionsTestCredentialsCreateResponse400Type1.from_dict(data)



            return response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TestConnectionCredentialsRequest,

) -> Response[ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection]:
    """  Test credentials without storing them.

    Args:
        body (TestConnectionCredentialsRequest): Serializer for testing connector credentials
            without saving a connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: TestConnectionCredentialsRequest,

) -> ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection | None:
    """  Test credentials without storing them.

    Args:
        body (TestConnectionCredentialsRequest): Serializer for testing connector credentials
            without saving a connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TestConnectionCredentialsRequest,

) -> Response[ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection]:
    """  Test credentials without storing them.

    Args:
        body (TestConnectionCredentialsRequest): Serializer for testing connector credentials
            without saving a connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TestConnectionCredentialsRequest,

) -> ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection | None:
    """  Test credentials without storing them.

    Args:
        body (TestConnectionCredentialsRequest): Serializer for testing connector credentials
            without saving a connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionsTestCredentialsCreateResponse400Type0 | ConnectionsTestCredentialsCreateResponse400Type1 | TestConnection
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
