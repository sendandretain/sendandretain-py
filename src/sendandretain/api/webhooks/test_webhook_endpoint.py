from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.test_webhook_endpoint_response_202 import TestWebhookEndpointResponse202
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/webhooks/{id}/test".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | TestWebhookEndpointResponse202 | None:
    if response.status_code == 202:
        response_202 = TestWebhookEndpointResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TestWebhookEndpointResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | TestWebhookEndpointResponse202]:
    """Send a test delivery

     Queues a synthetic `webhook.test` event. It travels the full path — same signing, same retry curve,
    same delivery log — so a passing test proves real events will arrive too. Requires the endpoint to
    be subscribed to `webhook.test`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TestWebhookEndpointResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | TestWebhookEndpointResponse202 | None:
    """Send a test delivery

     Queues a synthetic `webhook.test` event. It travels the full path — same signing, same retry curve,
    same delivery log — so a passing test proves real events will arrive too. Requires the endpoint to
    be subscribed to `webhook.test`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TestWebhookEndpointResponse202
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | TestWebhookEndpointResponse202]:
    """Send a test delivery

     Queues a synthetic `webhook.test` event. It travels the full path — same signing, same retry curve,
    same delivery log — so a passing test proves real events will arrive too. Requires the endpoint to
    be subscribed to `webhook.test`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TestWebhookEndpointResponse202]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | TestWebhookEndpointResponse202 | None:
    """Send a test delivery

     Queues a synthetic `webhook.test` event. It travels the full path — same signing, same retry curve,
    same delivery log — so a passing test proves real events will arrive too. Requires the endpoint to
    be subscribed to `webhook.test`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TestWebhookEndpointResponse202
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
