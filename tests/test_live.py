"""Live smoke test against a real deployment. Read-only.

Skipped unless SENDANDRETAIN_E2E_API_KEY is set — a separate variable from the
one the SDK reads, so a key in your shell never turns `pytest` into network traffic.

    SENDANDRETAIN_E2E_API_KEY=aem_… [SENDANDRETAIN_E2E_BASE_URL=…] uv run pytest tests/test_live.py
"""

from __future__ import annotations

import os
import time

import pytest

from sendandretain import NotFoundError, SendAndRetain

KEY = os.environ.get("SENDANDRETAIN_E2E_API_KEY")

pytestmark = pytest.mark.skipif(not KEY, reason="set SENDANDRETAIN_E2E_API_KEY to run against a live API")


def live() -> SendAndRetain:
    return SendAndRetain(KEY, base_url=os.environ.get("SENDANDRETAIN_E2E_BASE_URL"))


def test_authenticates() -> None:
    assert live().setup.onboarding() is not None


def test_unknown_template_is_not_found() -> None:
    with pytest.raises(NotFoundError) as caught:
        live().templates.get(f"does-not-exist-{int(time.time())}")
    assert caught.value.request_id
