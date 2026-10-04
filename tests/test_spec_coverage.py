"""Guards that the generated client really covers the vendored spec.

`verify_schema_sync.py` proves the tree matches the spec byte-for-byte. This
proves the spec is the one we think it is, and that no operation was silently
dropped — openapi-python-client warns and skips rather than failing, so a
regression here would otherwise be invisible.
"""

from __future__ import annotations

import json
import pathlib

import sendandretain

REPO = pathlib.Path(__file__).resolve().parent.parent
SPEC = json.loads((REPO / "openapi.json").read_text())
GENERATED = REPO / "src" / "sendandretain"
METHODS = {"get", "put", "post", "delete", "patch", "head", "options", "trace"}


def spec_operation_count() -> int:
    return sum(1 for operations in SPEC["paths"].values() for method in operations if method in METHODS)


def generated_operation_modules() -> list[pathlib.Path]:
    return [path for path in (GENERATED / "api").rglob("*.py") if path.name != "__init__.py"]


def test_every_operation_in_the_spec_was_generated() -> None:
    assert len(generated_operation_modules()) == spec_operation_count()


def test_every_generated_operation_exposes_sync_and_async() -> None:
    entrypoints = ("def sync_detailed(", "def asyncio_detailed(")
    missing = [
        f"{path.relative_to(GENERATED)}: {entrypoint}"
        for path in generated_operation_modules()
        for entrypoint in entrypoints
        if entrypoint not in path.read_text()
    ]
    assert not missing


def test_spec_targets_production() -> None:
    assert SPEC["servers"][0]["url"] == sendandretain.DEFAULT_BASE_URL == "https://sendandretain.com"


def test_bearer_is_the_documented_scheme() -> None:
    scheme = SPEC["components"]["securitySchemes"]["bearerAuth"]
    assert scheme["type"] == "http"
    assert scheme["scheme"] == "bearer"


def test_public_surface_is_importable() -> None:
    for name in sendandretain.__all__:
        assert hasattr(sendandretain, name), name
