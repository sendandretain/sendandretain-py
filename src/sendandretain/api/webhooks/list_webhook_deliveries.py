import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_webhook_deliveries_response_200 import ListWebhookDeliveriesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    status: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["status"] = status

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/webhooks/{id}/deliveries".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ListWebhookDeliveriesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListWebhookDeliveriesResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Error | ListWebhookDeliveriesResponse200]:
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
    status: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Error | ListWebhookDeliveriesResponse200]:
    """List deliveries

     What we attempted, when, and what your server said. `response_snippet` carries the first 2 KB of
    your endpoint's response body, which is usually the whole answer. Newest first; page with `limit` +
    `before`.

    Args:
        id (str):
        status (str | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListWebhookDeliveriesResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        before=before,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Error | ListWebhookDeliveriesResponse200 | None:
    """List deliveries

     What we attempted, when, and what your server said. `response_snippet` carries the first 2 KB of
    your endpoint's response body, which is usually the whole answer. Newest first; page with `limit` +
    `before`.

    Args:
        id (str):
        status (str | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListWebhookDeliveriesResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        status=status,
        before=before,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Error | ListWebhookDeliveriesResponse200]:
    """List deliveries

     What we attempted, when, and what your server said. `response_snippet` carries the first 2 KB of
    your endpoint's response body, which is usually the whole answer. Newest first; page with `limit` +
    `before`.

    Args:
        id (str):
        status (str | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListWebhookDeliveriesResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        before=before,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Error | ListWebhookDeliveriesResponse200 | None:
    """List deliveries

     What we attempted, when, and what your server said. `response_snippet` carries the first 2 KB of
    your endpoint's response body, which is usually the whole answer. Newest first; page with `limit` +
    `before`.

    Args:
        id (str):
        status (str | Unset):
        before (datetime.datetime | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListWebhookDeliveriesResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            status=status,
            before=before,
            limit=limit,
        )
    ).parsed
