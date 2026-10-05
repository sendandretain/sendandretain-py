from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_suppressions_reason import ListSuppressionsReason
from ...models.list_suppressions_response_200 import ListSuppressionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    reason: ListSuppressionsReason | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_reason: str | Unset = UNSET
    if not isinstance(reason, Unset):
        json_reason = reason.value

    params["reason"] = json_reason

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/suppressions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ListSuppressionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListSuppressionsResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Error | ListSuppressionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    reason: ListSuppressionsReason | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Error | ListSuppressionsResponse200]:
    """List suppressions

     Lists suppressed addresses (the do-not-send list). Filter by `reason`. Requires a `write`-scope key.

    Args:
        reason (ListSuppressionsReason | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListSuppressionsResponse200]
    """

    kwargs = _get_kwargs(
        reason=reason,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    reason: ListSuppressionsReason | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Error | ListSuppressionsResponse200 | None:
    """List suppressions

     Lists suppressed addresses (the do-not-send list). Filter by `reason`. Requires a `write`-scope key.

    Args:
        reason (ListSuppressionsReason | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListSuppressionsResponse200
    """

    return sync_detailed(
        client=client,
        reason=reason,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    reason: ListSuppressionsReason | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Error | ListSuppressionsResponse200]:
    """List suppressions

     Lists suppressed addresses (the do-not-send list). Filter by `reason`. Requires a `write`-scope key.

    Args:
        reason (ListSuppressionsReason | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListSuppressionsResponse200]
    """

    kwargs = _get_kwargs(
        reason=reason,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    reason: ListSuppressionsReason | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Error | ListSuppressionsResponse200 | None:
    """List suppressions

     Lists suppressed addresses (the do-not-send list). Filter by `reason`. Requires a `write`-scope key.

    Args:
        reason (ListSuppressionsReason | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListSuppressionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            reason=reason,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
