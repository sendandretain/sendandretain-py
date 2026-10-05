from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_connection_status_response_200 import GetConnectionStatusResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/connection",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetConnectionStatusResponse200 | None:
    if response.status_code == 200:
        response_200 = GetConnectionStatusResponse200.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetConnectionStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | GetConnectionStatusResponse200]:
    """Can this project send?

     One call for the whole readiness question: provider connected, domains verified, default sender
    present, webhooks registered, kill switch off. Meant as a deploy-time preflight.

    Note there is no way to SET a provider API key over this API — credentials only ever enter through
    the dashboard (`settings_url`), so a leaked `aem_` key can't repoint your sending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetConnectionStatusResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | GetConnectionStatusResponse200 | None:
    """Can this project send?

     One call for the whole readiness question: provider connected, domains verified, default sender
    present, webhooks registered, kill switch off. Meant as a deploy-time preflight.

    Note there is no way to SET a provider API key over this API — credentials only ever enter through
    the dashboard (`settings_url`), so a leaked `aem_` key can't repoint your sending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetConnectionStatusResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | GetConnectionStatusResponse200]:
    """Can this project send?

     One call for the whole readiness question: provider connected, domains verified, default sender
    present, webhooks registered, kill switch off. Meant as a deploy-time preflight.

    Note there is no way to SET a provider API key over this API — credentials only ever enter through
    the dashboard (`settings_url`), so a leaked `aem_` key can't repoint your sending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetConnectionStatusResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | GetConnectionStatusResponse200 | None:
    """Can this project send?

     One call for the whole readiness question: provider connected, domains verified, default sender
    present, webhooks registered, kill switch off. Meant as a deploy-time preflight.

    Note there is no way to SET a provider API key over this API — credentials only ever enter through
    the dashboard (`settings_url`), so a leaked `aem_` key can't repoint your sending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetConnectionStatusResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
