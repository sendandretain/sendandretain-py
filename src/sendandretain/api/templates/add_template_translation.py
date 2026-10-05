from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_template_translation_body import AddTemplateTranslationBody
from ...models.add_template_translation_response_201 import AddTemplateTranslationResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    slug: str,
    *,
    body: AddTemplateTranslationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/templates/{slug}/translations".format(
            slug=quote(str(slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddTemplateTranslationResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = AddTemplateTranslationResponse201.from_dict(response.json())

        return response_201

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddTemplateTranslationResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: AddTemplateTranslationBody,
) -> Response[AddTemplateTranslationResponse201 | Error]:
    """Add a translation

     Creates a locale-tagged version. Publish it like any other version; the send path picks it when a
    request passes a matching `locale` and falls back to the base language otherwise.

    Args:
        slug (str):
        body (AddTemplateTranslationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddTemplateTranslationResponse201 | Error]
    """

    kwargs = _get_kwargs(
        slug=slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: AddTemplateTranslationBody,
) -> AddTemplateTranslationResponse201 | Error | None:
    """Add a translation

     Creates a locale-tagged version. Publish it like any other version; the send path picks it when a
    request passes a matching `locale` and falls back to the base language otherwise.

    Args:
        slug (str):
        body (AddTemplateTranslationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddTemplateTranslationResponse201 | Error
    """

    return sync_detailed(
        slug=slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: AddTemplateTranslationBody,
) -> Response[AddTemplateTranslationResponse201 | Error]:
    """Add a translation

     Creates a locale-tagged version. Publish it like any other version; the send path picks it when a
    request passes a matching `locale` and falls back to the base language otherwise.

    Args:
        slug (str):
        body (AddTemplateTranslationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddTemplateTranslationResponse201 | Error]
    """

    kwargs = _get_kwargs(
        slug=slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: AddTemplateTranslationBody,
) -> AddTemplateTranslationResponse201 | Error | None:
    """Add a translation

     Creates a locale-tagged version. Publish it like any other version; the send path picks it when a
    request passes a matching `locale` and falls back to the base language otherwise.

    Args:
        slug (str):
        body (AddTemplateTranslationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddTemplateTranslationResponse201 | Error
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
            body=body,
        )
    ).parsed
