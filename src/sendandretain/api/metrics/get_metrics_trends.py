from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_metrics_trends_response_200 import GetMetricsTrendsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/metrics/trends",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetMetricsTrendsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetMetricsTrendsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetMetricsTrendsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
) -> Response[Error | GetMetricsTrendsResponse200]:
    """Daily series

     Day-by-day counts from the pre-aggregated rollup — fast and coarse, for charting. Use `GET
    /api/v1/metrics` when you need exact, windowed, per-template numbers. Days with no activity are
    absent rather than zero-filled.

    Args:
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetMetricsTrendsResponse200]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
) -> Error | GetMetricsTrendsResponse200 | None:
    """Daily series

     Day-by-day counts from the pre-aggregated rollup — fast and coarse, for charting. Use `GET
    /api/v1/metrics` when you need exact, windowed, per-template numbers. Days with no activity are
    absent rather than zero-filled.

    Args:
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetMetricsTrendsResponse200
    """

    return sync_detailed(
        client=client,
        days=days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
) -> Response[Error | GetMetricsTrendsResponse200]:
    """Daily series

     Day-by-day counts from the pre-aggregated rollup — fast and coarse, for charting. Use `GET
    /api/v1/metrics` when you need exact, windowed, per-template numbers. Days with no activity are
    absent rather than zero-filled.

    Args:
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetMetricsTrendsResponse200]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
) -> Error | GetMetricsTrendsResponse200 | None:
    """Daily series

     Day-by-day counts from the pre-aggregated rollup — fast and coarse, for charting. Use `GET
    /api/v1/metrics` when you need exact, windowed, per-template numbers. Days with no activity are
    absent rather than zero-filled.

    Args:
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetMetricsTrendsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
        )
    ).parsed
