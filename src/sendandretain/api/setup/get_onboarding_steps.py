from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_onboarding_steps_response_200 import GetOnboardingStepsResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/setup/onboarding",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetOnboardingStepsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetOnboardingStepsResponse200.from_dict(response.json())

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
) -> Response[Error | GetOnboardingStepsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetOnboardingStepsResponse200]:
    """How far through setup is this company?

     The ten steps of getting a company live, with the same addresses (`1.1`–`3.5`) and titles the
    operator sees in the dashboard. Every `done` is derived from real rows — there is no stored
    checklist — so work done through this API, over MCP or by hand all move the same list.

    Distinct from `GET /api/v1/connection`, which answers the narrower deploy-time question 'can this
    project send right now'. This one also covers the discovery answers, the approved programme and
    whether the company has sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetOnboardingStepsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetOnboardingStepsResponse200 | None:
    """How far through setup is this company?

     The ten steps of getting a company live, with the same addresses (`1.1`–`3.5`) and titles the
    operator sees in the dashboard. Every `done` is derived from real rows — there is no stored
    checklist — so work done through this API, over MCP or by hand all move the same list.

    Distinct from `GET /api/v1/connection`, which answers the narrower deploy-time question 'can this
    project send right now'. This one also covers the discovery answers, the approved programme and
    whether the company has sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetOnboardingStepsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetOnboardingStepsResponse200]:
    """How far through setup is this company?

     The ten steps of getting a company live, with the same addresses (`1.1`–`3.5`) and titles the
    operator sees in the dashboard. Every `done` is derived from real rows — there is no stored
    checklist — so work done through this API, over MCP or by hand all move the same list.

    Distinct from `GET /api/v1/connection`, which answers the narrower deploy-time question 'can this
    project send right now'. This one also covers the discovery answers, the approved programme and
    whether the company has sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetOnboardingStepsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetOnboardingStepsResponse200 | None:
    """How far through setup is this company?

     The ten steps of getting a company live, with the same addresses (`1.1`–`3.5`) and titles the
    operator sees in the dashboard. Every `done` is derived from real rows — there is no stored
    checklist — so work done through this API, over MCP or by hand all move the same list.

    Distinct from `GET /api/v1/connection`, which answers the narrower deploy-time question 'can this
    project send right now'. This one also covers the discovery answers, the approved programme and
    whether the company has sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetOnboardingStepsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
