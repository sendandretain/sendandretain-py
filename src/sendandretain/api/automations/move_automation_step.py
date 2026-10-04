from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.move_automation_step_body import MoveAutomationStepBody
from ...models.move_automation_step_response_200 import MoveAutomationStepResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: MoveAutomationStepBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/automations/steps/move",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MoveAutomationStepResponse200 | None:
    if response.status_code == 200:
        response_200 = MoveAutomationStepResponse200.from_dict(response.json())

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
) -> Response[Error | MoveAutomationStepResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MoveAutomationStepBody,
) -> Response[Error | MoveAutomationStepResponse200]:
    """Reorder a step

     Moves a step among its lane siblings — never across into another branch arm. Requires a paused
    automation.

    Args:
        body (MoveAutomationStepBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MoveAutomationStepResponse200]
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
    body: MoveAutomationStepBody,
) -> Error | MoveAutomationStepResponse200 | None:
    """Reorder a step

     Moves a step among its lane siblings — never across into another branch arm. Requires a paused
    automation.

    Args:
        body (MoveAutomationStepBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MoveAutomationStepResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MoveAutomationStepBody,
) -> Response[Error | MoveAutomationStepResponse200]:
    """Reorder a step

     Moves a step among its lane siblings — never across into another branch arm. Requires a paused
    automation.

    Args:
        body (MoveAutomationStepBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MoveAutomationStepResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MoveAutomationStepBody,
) -> Error | MoveAutomationStepResponse200 | None:
    """Reorder a step

     Moves a step among its lane siblings — never across into another branch arm. Requires a paused
    automation.

    Args:
        body (MoveAutomationStepBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MoveAutomationStepResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
