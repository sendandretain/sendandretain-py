from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.render_template_body import RenderTemplateBody
from ...models.render_template_response_200 import RenderTemplateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    slug: str,
    *,
    body: RenderTemplateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/templates/{slug}/render".format(
            slug=quote(str(slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RenderTemplateResponse200 | None:
    if response.status_code == 200:
        response_200 = RenderTemplateResponse200.from_dict(response.json())

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
) -> Response[Error | RenderTemplateResponse200]:
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
    body: RenderTemplateBody | Unset = UNSET,
) -> Response[Error | RenderTemplateResponse200]:
    """Render a template

     Compiles and renders a version and returns the HTML, plain text and subject. No side effects —
    nothing is sent. This is the authoring inner loop: compile and render failures come back as
    `invalid_request` carrying the verbatim diagnostics, so you can fix the source and retry.

    Args:
        slug (str):
        body (RenderTemplateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RenderTemplateResponse200]
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
    client: AuthenticatedClient | Client,
    body: RenderTemplateBody | Unset = UNSET,
) -> Error | RenderTemplateResponse200 | None:
    """Render a template

     Compiles and renders a version and returns the HTML, plain text and subject. No side effects —
    nothing is sent. This is the authoring inner loop: compile and render failures come back as
    `invalid_request` carrying the verbatim diagnostics, so you can fix the source and retry.

    Args:
        slug (str):
        body (RenderTemplateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RenderTemplateResponse200
    """

    return sync_detailed(
        slug=slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenderTemplateBody | Unset = UNSET,
) -> Response[Error | RenderTemplateResponse200]:
    """Render a template

     Compiles and renders a version and returns the HTML, plain text and subject. No side effects —
    nothing is sent. This is the authoring inner loop: compile and render failures come back as
    `invalid_request` carrying the verbatim diagnostics, so you can fix the source and retry.

    Args:
        slug (str):
        body (RenderTemplateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RenderTemplateResponse200]
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
    client: AuthenticatedClient | Client,
    body: RenderTemplateBody | Unset = UNSET,
) -> Error | RenderTemplateResponse200 | None:
    """Render a template

     Compiles and renders a version and returns the HTML, plain text and subject. No side effects —
    nothing is sent. This is the authoring inner loop: compile and render failures come back as
    `invalid_request` carrying the verbatim diagnostics, so you can fix the source and retry.

    Args:
        slug (str):
        body (RenderTemplateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RenderTemplateResponse200
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
            body=body,
        )
    ).parsed
