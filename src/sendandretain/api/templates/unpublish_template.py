from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.unpublish_template_response_200 import UnpublishTemplateResponse200
from ...types import Response


def _get_kwargs(
    slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/templates/{slug}/versions".format(
            slug=quote(str(slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | UnpublishTemplateResponse200 | None:
    if response.status_code == 200:
        response_200 = UnpublishTemplateResponse200.from_dict(response.json())

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
) -> Response[Error | UnpublishTemplateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | UnpublishTemplateResponse200]:
    """Unpublish a template

     Takes a published template back out of service: clears its live version and flips that version back
    to draft. Every send then refuses with `template_not_published` until you publish again — use this
    when a template went live before it was ready. Republishing restores it; nothing is archived and no
    content is lost. Refused while an ACTIVE automation still sends this template — pause those
    automations first.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnpublishTemplateResponse200]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | UnpublishTemplateResponse200 | None:
    """Unpublish a template

     Takes a published template back out of service: clears its live version and flips that version back
    to draft. Every send then refuses with `template_not_published` until you publish again — use this
    when a template went live before it was ready. Republishing restores it; nothing is archived and no
    content is lost. Refused while an ACTIVE automation still sends this template — pause those
    automations first.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnpublishTemplateResponse200
    """

    return sync_detailed(
        slug=slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | UnpublishTemplateResponse200]:
    """Unpublish a template

     Takes a published template back out of service: clears its live version and flips that version back
    to draft. Every send then refuses with `template_not_published` until you publish again — use this
    when a template went live before it was ready. Republishing restores it; nothing is archived and no
    content is lost. Refused while an ACTIVE automation still sends this template — pause those
    automations first.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnpublishTemplateResponse200]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | UnpublishTemplateResponse200 | None:
    """Unpublish a template

     Takes a published template back out of service: clears its live version and flips that version back
    to draft. Every send then refuses with `template_not_published` until you publish again — use this
    when a template went live before it was ready. Republishing restores it; nothing is archived and no
    content is lost. Refused while an ACTIVE automation still sends this template — pause those
    automations first.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnpublishTemplateResponse200
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
        )
    ).parsed
