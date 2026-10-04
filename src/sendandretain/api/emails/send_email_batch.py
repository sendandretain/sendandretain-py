from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.send_email_batch_body import SendEmailBatchBody
from ...models.send_email_batch_response_202 import SendEmailBatchResponse202
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SendEmailBatchBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/emails/batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SendEmailBatchResponse202 | None:
    if response.status_code == 202:
        response_202 = SendEmailBatchResponse202.from_dict(response.json())

        return response_202

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
) -> Response[Error | SendEmailBatchResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBatchBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | SendEmailBatchResponse202]:
    """Send a batch of emails

     Up to 100 DISTINCT emails in one call — each with its own recipient, template and props. One round-
    trip instead of 100.

    This is not a bulk-campaign endpoint: every entry is still a single-recipient message and goes
    through the same idempotency, suppression, cap and sender checks a single send does. Nothing is
    skipped for speed.

    **Entries succeed and fail independently.** The response is always `202` with a per-index result
    array in request order — `data[i]` corresponds to `emails[i]`. A success carries `id` and `status`;
    a failure carries an `error` object with the same codes a single send returns. Check the array, not
    the status code.

    Idempotency: give each entry its own `idempotency_key`, or pass an `Idempotency-Key` header and each
    entry derives `<header>:<index>`. Retrying a partially-succeeded batch then replays the successes
    and retries only the failures.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendEmailBatchResponse202]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBatchBody,
    idempotency_key: str | Unset = UNSET,
) -> Error | SendEmailBatchResponse202 | None:
    """Send a batch of emails

     Up to 100 DISTINCT emails in one call — each with its own recipient, template and props. One round-
    trip instead of 100.

    This is not a bulk-campaign endpoint: every entry is still a single-recipient message and goes
    through the same idempotency, suppression, cap and sender checks a single send does. Nothing is
    skipped for speed.

    **Entries succeed and fail independently.** The response is always `202` with a per-index result
    array in request order — `data[i]` corresponds to `emails[i]`. A success carries `id` and `status`;
    a failure carries an `error` object with the same codes a single send returns. Check the array, not
    the status code.

    Idempotency: give each entry its own `idempotency_key`, or pass an `Idempotency-Key` header and each
    entry derives `<header>:<index>`. Retrying a partially-succeeded batch then replays the successes
    and retries only the failures.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendEmailBatchResponse202
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBatchBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | SendEmailBatchResponse202]:
    """Send a batch of emails

     Up to 100 DISTINCT emails in one call — each with its own recipient, template and props. One round-
    trip instead of 100.

    This is not a bulk-campaign endpoint: every entry is still a single-recipient message and goes
    through the same idempotency, suppression, cap and sender checks a single send does. Nothing is
    skipped for speed.

    **Entries succeed and fail independently.** The response is always `202` with a per-index result
    array in request order — `data[i]` corresponds to `emails[i]`. A success carries `id` and `status`;
    a failure carries an `error` object with the same codes a single send returns. Check the array, not
    the status code.

    Idempotency: give each entry its own `idempotency_key`, or pass an `Idempotency-Key` header and each
    entry derives `<header>:<index>`. Retrying a partially-succeeded batch then replays the successes
    and retries only the failures.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendEmailBatchResponse202]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBatchBody,
    idempotency_key: str | Unset = UNSET,
) -> Error | SendEmailBatchResponse202 | None:
    """Send a batch of emails

     Up to 100 DISTINCT emails in one call — each with its own recipient, template and props. One round-
    trip instead of 100.

    This is not a bulk-campaign endpoint: every entry is still a single-recipient message and goes
    through the same idempotency, suppression, cap and sender checks a single send does. Nothing is
    skipped for speed.

    **Entries succeed and fail independently.** The response is always `202` with a per-index result
    array in request order — `data[i]` corresponds to `emails[i]`. A success carries `id` and `status`;
    a failure carries an `error` object with the same codes a single send returns. Check the array, not
    the status code.

    Idempotency: give each entry its own `idempotency_key`, or pass an `Idempotency-Key` header and each
    entry derives `<header>:<index>`. Retrying a partially-succeeded batch then replays the successes
    and retries only the failures.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendEmailBatchResponse202
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
