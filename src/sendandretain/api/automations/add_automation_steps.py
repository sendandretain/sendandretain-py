from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_automation_steps_body import AddAutomationStepsBody
from ...models.add_automation_steps_response_200 import AddAutomationStepsResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: AddAutomationStepsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/automations/steps",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddAutomationStepsResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = AddAutomationStepsResponse200.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddAutomationStepsResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddAutomationStepsBody,
) -> Response[AddAutomationStepsResponse200 | Error]:
    """Append automation steps

     Appends steps to a sequence or a branch lane. Appending to a live automation is safe — in-flight
    contacts advance by stable step id, so they are never disturbed. Use `after_position` to insert, or
    `parent_step_id` + `lane_key` to target a branch lane.

    Args:
        body (AddAutomationStepsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAutomationStepsResponse200 | Error]
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
    client: AuthenticatedClient | Client,
    body: AddAutomationStepsBody,
) -> AddAutomationStepsResponse200 | Error | None:
    """Append automation steps

     Appends steps to a sequence or a branch lane. Appending to a live automation is safe — in-flight
    contacts advance by stable step id, so they are never disturbed. Use `after_position` to insert, or
    `parent_step_id` + `lane_key` to target a branch lane.

    Args:
        body (AddAutomationStepsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAutomationStepsResponse200 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddAutomationStepsBody,
) -> Response[AddAutomationStepsResponse200 | Error]:
    """Append automation steps

     Appends steps to a sequence or a branch lane. Appending to a live automation is safe — in-flight
    contacts advance by stable step id, so they are never disturbed. Use `after_position` to insert, or
    `parent_step_id` + `lane_key` to target a branch lane.

    Args:
        body (AddAutomationStepsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAutomationStepsResponse200 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AddAutomationStepsBody,
) -> AddAutomationStepsResponse200 | Error | None:
    """Append automation steps

     Appends steps to a sequence or a branch lane. Appending to a live automation is safe — in-flight
    contacts advance by stable step id, so they are never disturbed. Use `after_position` to insert, or
    `parent_step_id` + `lane_key` to target a branch lane.

    Args:
        body (AddAutomationStepsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAutomationStepsResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
