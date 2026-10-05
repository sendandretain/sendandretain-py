from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.update_template_meta_body import UpdateTemplateMetaBody
from ...models.update_template_meta_response_200 import UpdateTemplateMetaResponse200
from ...types import Response


def _get_kwargs(
    slug: str,
    *,
    body: UpdateTemplateMetaBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/templates/{slug}/meta".format(
            slug=quote(str(slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | UpdateTemplateMetaResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateTemplateMetaResponse200.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | UpdateTemplateMetaResponse200]:
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
    body: UpdateTemplateMetaBody,
) -> Response[Error | UpdateTemplateMetaResponse200]:
    r"""Edit subject, preview text, or sender

     The \"just fix the email meta\" path — no new TSX. Subject and preview-text edits are copy-on-write
    (a new draft version) and are **auto-published when the template is already published**, so the
    change actually sends instead of stranding a draft. The sender updates in place.

    Args:
        slug (str):
        body (UpdateTemplateMetaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateTemplateMetaResponse200]
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
    body: UpdateTemplateMetaBody,
) -> Error | UpdateTemplateMetaResponse200 | None:
    r"""Edit subject, preview text, or sender

     The \"just fix the email meta\" path — no new TSX. Subject and preview-text edits are copy-on-write
    (a new draft version) and are **auto-published when the template is already published**, so the
    change actually sends instead of stranding a draft. The sender updates in place.

    Args:
        slug (str):
        body (UpdateTemplateMetaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateTemplateMetaResponse200
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
    body: UpdateTemplateMetaBody,
) -> Response[Error | UpdateTemplateMetaResponse200]:
    r"""Edit subject, preview text, or sender

     The \"just fix the email meta\" path — no new TSX. Subject and preview-text edits are copy-on-write
    (a new draft version) and are **auto-published when the template is already published**, so the
    change actually sends instead of stranding a draft. The sender updates in place.

    Args:
        slug (str):
        body (UpdateTemplateMetaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateTemplateMetaResponse200]
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
    body: UpdateTemplateMetaBody,
) -> Error | UpdateTemplateMetaResponse200 | None:
    r"""Edit subject, preview text, or sender

     The \"just fix the email meta\" path — no new TSX. Subject and preview-text edits are copy-on-write
    (a new draft version) and are **auto-published when the template is already published**, so the
    change actually sends instead of stranding a draft. The sender updates in place.

    Args:
        slug (str):
        body (UpdateTemplateMetaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateTemplateMetaResponse200
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
            body=body,
        )
    ).parsed
