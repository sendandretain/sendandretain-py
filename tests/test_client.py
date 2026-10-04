"""The hand-written layer is small, so it is tested exhaustively.

No network: every assertion reads the httpx client the factory built.
"""

from __future__ import annotations

import httpx
import pytest

from sendandretain import API_KEY_ENV_VAR, API_KEY_PREFIX, DEFAULT_BASE_URL, Client
from sendandretain.client import AuthenticatedClient

VALID_KEY = "aem_test0123456789"


def test_returns_the_generated_authenticated_client() -> None:
    assert isinstance(Client(api_key=VALID_KEY), AuthenticatedClient)


def test_sets_the_production_base_url_by_default() -> None:
    assert Client(api_key=VALID_KEY).get_httpx_client().base_url == httpx.URL("https://sendandretain.com")
    assert DEFAULT_BASE_URL == "https://sendandretain.com"


def test_sends_the_key_as_a_bearer_token() -> None:
    headers = Client(api_key=VALID_KEY).get_httpx_client().headers
    assert headers["Authorization"] == f"Bearer {VALID_KEY}"


def test_base_url_can_be_overridden() -> None:
    client = Client(api_key=VALID_KEY, base_url="https://staging.example.com")
    assert client.get_httpx_client().base_url == httpx.URL("https://staging.example.com")


def test_reads_the_key_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(API_KEY_ENV_VAR, VALID_KEY)
    assert Client().get_httpx_client().headers["Authorization"] == f"Bearer {VALID_KEY}"


def test_explicit_key_beats_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(API_KEY_ENV_VAR, "aem_from_env")
    client = Client(api_key=VALID_KEY)
    assert client.get_httpx_client().headers["Authorization"] == f"Bearer {VALID_KEY}"


def test_missing_key_names_both_ways_to_supply_one(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(API_KEY_ENV_VAR, raising=False)
    with pytest.raises(ValueError, match=API_KEY_ENV_VAR):
        Client()


def test_wrong_prefix_is_rejected_before_any_request(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(API_KEY_ENV_VAR, raising=False)
    with pytest.raises(ValueError, match=API_KEY_PREFIX):
        Client(api_key="sk_live_not_ours")


def test_empty_environment_variable_is_treated_as_absent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(API_KEY_ENV_VAR, "")
    with pytest.raises(ValueError):
        Client()


def test_numeric_timeout_is_accepted() -> None:
    client = Client(api_key=VALID_KEY, timeout=12.5)
    assert client.get_httpx_client().timeout == httpx.Timeout(12.5)


def test_extra_headers_are_forwarded() -> None:
    client = Client(api_key=VALID_KEY, headers={"X-Trace": "abc"})
    assert client.get_httpx_client().headers["X-Trace"] == "abc"


def test_key_prefix_matches_the_documented_one() -> None:
    assert API_KEY_PREFIX == "aem_"
