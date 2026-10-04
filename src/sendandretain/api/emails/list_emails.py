from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_emails_response_200 import ListEmailsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    before: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["status"] = status

    params["to"] = to

    params["limit"] = limit

    params["before"] = before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/emails",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ListEmailsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListEmailsResponse200.from_dict(response.json())

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
) -> Response[Error | ListEmailsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    before: str | Unset = UNSET,
) -> Response[Error | ListEmailsResponse200]:
    """List sent emails

     Lists messages newest-first. Filter by `status` or recipient `to`; page with `limit` + `before` (an
    ISO `created_at`). Requires a `write`-scope key.

    Args:
        status (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListEmailsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        to=to,
        limit=limit,
        before=before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    before: str | Unset = UNSET,
) -> Error | ListEmailsResponse200 | None:
    """List sent emails

     Lists messages newest-first. Filter by `status` or recipient `to`; page with `limit` + `before` (an
    ISO `created_at`). Requires a `write`-scope key.

    Args:
        status (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListEmailsResponse200
    """

    return sync_detailed(
        client=client,
        status=status,
        to=to,
        limit=limit,
        before=before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    before: str | Unset = UNSET,
) -> Response[Error | ListEmailsResponse200]:
    """List sent emails

     Lists messages newest-first. Filter by `status` or recipient `to`; page with `limit` + `before` (an
    ISO `created_at`). Requires a `write`-scope key.

    Args:
        status (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListEmailsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        to=to,
        limit=limit,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    before: str | Unset = UNSET,
) -> Error | ListEmailsResponse200 | None:
    """List sent emails

     Lists messages newest-first. Filter by `status` or recipient `to`; page with `limit` + `before` (an
    ISO `created_at`). Requires a `write`-scope key.

    Args:
        status (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        before (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListEmailsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            to=to,
            limit=limit,
            before=before,
        )
    ).parsed
