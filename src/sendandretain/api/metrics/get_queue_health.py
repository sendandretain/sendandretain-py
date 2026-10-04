from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_queue_health_response_200 import GetQueueHealthResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/queue/health",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetQueueHealthResponse200 | None:
    if response.status_code == 200:
        response_200 = GetQueueHealthResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetQueueHealthResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetQueueHealthResponse200]:
    """Worker queue health

     Scheduling is ours, not the provider's: delayed sends, automation steps and throttle-deferred
    messages all wait in our queue. A growing `pending_due_now` or a large `oldest_pending_age_seconds`
    means mail is late; `dead_letter` means some gave up entirely. Worth alerting on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetQueueHealthResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetQueueHealthResponse200 | None:
    """Worker queue health

     Scheduling is ours, not the provider's: delayed sends, automation steps and throttle-deferred
    messages all wait in our queue. A growing `pending_due_now` or a large `oldest_pending_age_seconds`
    means mail is late; `dead_letter` means some gave up entirely. Worth alerting on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetQueueHealthResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetQueueHealthResponse200]:
    """Worker queue health

     Scheduling is ours, not the provider's: delayed sends, automation steps and throttle-deferred
    messages all wait in our queue. A growing `pending_due_now` or a large `oldest_pending_age_seconds`
    means mail is late; `dead_letter` means some gave up entirely. Worth alerting on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetQueueHealthResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetQueueHealthResponse200 | None:
    """Worker queue health

     Scheduling is ours, not the provider's: delayed sends, automation steps and throttle-deferred
    messages all wait in our queue. A growing `pending_due_now` or a large `oldest_pending_age_seconds`
    means mail is late; `dead_letter` means some gave up entirely. Worth alerting on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetQueueHealthResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
