from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backfill_missed_enrollments_body import BackfillMissedEnrollmentsBody
from ...models.backfill_missed_enrollments_response_200 import BackfillMissedEnrollmentsResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: BackfillMissedEnrollmentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/automations/{id}/backfill".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackfillMissedEnrollmentsResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = BackfillMissedEnrollmentsResponse200.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BackfillMissedEnrollmentsResponse200 | Error]:
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
    body: BackfillMissedEnrollmentsBody,
) -> Response[BackfillMissedEnrollmentsResponse200 | Error]:
    """Catch up enrollments missed while paused

     Events keep being recorded while an automation is paused — only enrollment is skipped — so the
    contacts it missed are recoverable. **Defaults to a dry run**: the point is to see who would be
    enrolled before committing. Contacts whose EXIT event arrived after their trigger are skipped,
    because they resolved during the pause and enrolling them would chase a customer who already
    converted; the automation's own re-enrollment, cooldown and suppression guards still apply. `since`
    is required and **capped at six hours** — a window reaching further back is pulled forward and
    `window_clamped` says so, because replaying a one-hour chase days late is noise, not recovery.
    Resume the automation before running for real.

    Args:
        id (str):
        body (BackfillMissedEnrollmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackfillMissedEnrollmentsResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BackfillMissedEnrollmentsBody,
) -> BackfillMissedEnrollmentsResponse200 | Error | None:
    """Catch up enrollments missed while paused

     Events keep being recorded while an automation is paused — only enrollment is skipped — so the
    contacts it missed are recoverable. **Defaults to a dry run**: the point is to see who would be
    enrolled before committing. Contacts whose EXIT event arrived after their trigger are skipped,
    because they resolved during the pause and enrolling them would chase a customer who already
    converted; the automation's own re-enrollment, cooldown and suppression guards still apply. `since`
    is required and **capped at six hours** — a window reaching further back is pulled forward and
    `window_clamped` says so, because replaying a one-hour chase days late is noise, not recovery.
    Resume the automation before running for real.

    Args:
        id (str):
        body (BackfillMissedEnrollmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackfillMissedEnrollmentsResponse200 | Error
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BackfillMissedEnrollmentsBody,
) -> Response[BackfillMissedEnrollmentsResponse200 | Error]:
    """Catch up enrollments missed while paused

     Events keep being recorded while an automation is paused — only enrollment is skipped — so the
    contacts it missed are recoverable. **Defaults to a dry run**: the point is to see who would be
    enrolled before committing. Contacts whose EXIT event arrived after their trigger are skipped,
    because they resolved during the pause and enrolling them would chase a customer who already
    converted; the automation's own re-enrollment, cooldown and suppression guards still apply. `since`
    is required and **capped at six hours** — a window reaching further back is pulled forward and
    `window_clamped` says so, because replaying a one-hour chase days late is noise, not recovery.
    Resume the automation before running for real.

    Args:
        id (str):
        body (BackfillMissedEnrollmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackfillMissedEnrollmentsResponse200 | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BackfillMissedEnrollmentsBody,
) -> BackfillMissedEnrollmentsResponse200 | Error | None:
    """Catch up enrollments missed while paused

     Events keep being recorded while an automation is paused — only enrollment is skipped — so the
    contacts it missed are recoverable. **Defaults to a dry run**: the point is to see who would be
    enrolled before committing. Contacts whose EXIT event arrived after their trigger are skipped,
    because they resolved during the pause and enrolling them would chase a customer who already
    converted; the automation's own re-enrollment, cooldown and suppression guards still apply. `since`
    is required and **capped at six hours** — a window reaching further back is pulled forward and
    `window_clamped` says so, because replaying a one-hour chase days late is noise, not recovery.
    Resume the automation before running for real.

    Args:
        id (str):
        body (BackfillMissedEnrollmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackfillMissedEnrollmentsResponse200 | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
