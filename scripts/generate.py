#!/usr/bin/env python3
"""Regenerate the client in `src/sendandretain` from the vendored `openapi.json`.

The generated tree is committed, so this only runs when the spec or the
generator version changes. `scripts/verify_schema_sync.py` runs it into a
throwaway directory and fails if the result differs from what is committed.

The generator owns every path in `GENERATED_PATHS`; everything else in the
package is left alone — the hand-written modules in `HAND_WRITTEN`, the synced
`_runtime.py`, and `_resources.py`, which `generate_facade.py` rebuilds from the
same spec at the end of this script. That is
what lets the public import paths be real -- `sendandretain.api.emails` rather than
`sendandretain._generated.api.emails` -- while regeneration stays a clean replace.

The generator version is pinned here; regeneration is reproducible only because
it is.
"""

from __future__ import annotations

import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from normalize_spec import normalize  # noqa: E402, I001

GENERATOR = "openapi-python-client"
GENERATOR_VERSION = "0.29.0"
REPO = pathlib.Path(__file__).resolve().parent.parent
SPEC = REPO / "openapi.json"
PACKAGE = REPO / "src" / "sendandretain"

# Everything the generator emits, and therefore everything regeneration is free
# to delete. `__init__.py` is deliberately absent: the generator writes one, but
# ours supersedes it and is never overwritten.
GENERATED_PATHS = ("api", "models", "client.py", "errors.py", "types.py")

# `py.typed` is ours, not the generator's: with `--meta none` it emits no
# packaging files at all, and the PEP 561 marker is what tells a type checker
# that this *distribution* ships types. Without it every annotation in the
# generated tree is invisible to anyone who pip-installs the package.
HAND_WRITTEN = (
    "__init__.py",
    "_base.py",
    "_client.py",
    "_convenience.py",
    "_exceptions.py",
    "_version.py",
    "_webhooks.py",
    "py.typed",
)


def generator_command() -> list[str]:
    """Prefer `uvx` so the pinned version is used regardless of what is installed."""
    if shutil.which("uv"):
        return ["uvx", "--from", f"{GENERATOR}=={GENERATOR_VERSION}", GENERATOR]
    if shutil.which(GENERATOR):
        out = subprocess.run([GENERATOR, "--version"], capture_output=True, text=True, check=True).stdout
        if GENERATOR_VERSION not in out:
            sys.exit(
                f"{GENERATOR} {GENERATOR_VERSION} is required, found: {out.strip()}.\n"
                f"Install it with: pip install {GENERATOR}=={GENERATOR_VERSION}"
            )
        return [GENERATOR]
    sys.exit(f"Neither `uv` nor `{GENERATOR}` is on PATH. Install uv, or pip install {GENERATOR}=={GENERATOR_VERSION}")


def generate_into(destination: pathlib.Path) -> None:
    """Normalise the vendored spec and generate a complete client tree."""
    document, hoisted, widened = normalize(json.loads(SPEC.read_text()))
    print(f"normalised spec: hoisted {hoisted} union member(s), widened {widened} untyped array(s)")

    # The spec is written inside the repo, and so is `destination`, because
    # openapi-python-client runs `ruff format` over its output and ruff finds
    # configuration by walking up from the file. Anywhere outside the repo would
    # miss this project's `line-length` and rewrap every long line.
    with tempfile.NamedTemporaryFile("w", dir=REPO, prefix=".openapi-", suffix=".json", delete=True) as handle:
        json.dump(document, handle, indent=2)
        handle.flush()

        destination.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            [
                *generator_command(),
                "generate",
                "--path",
                handle.name,
                "--output-path",
                str(destination),
                "--overwrite",
                "--meta",
                "none",
                # A spec change that reintroduces a construct the generator
                # cannot model must fail here, not silently drop an endpoint.
                "--fail-on-warning",
            ],
            capture_output=True,
            text=True,
        )
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        if result.returncode != 0:
            sys.exit(f"{GENERATOR} failed with exit code {result.returncode}")

    # The generator leaves its own ruff cache behind; it is not part of the client.
    shutil.rmtree(destination / ".ruff_cache", ignore_errors=True)


def install(fresh: pathlib.Path, package: pathlib.Path = PACKAGE) -> None:
    """Replace the generated paths in `package`, preserving hand-written files."""
    package.mkdir(parents=True, exist_ok=True)
    for name in GENERATED_PATHS:
        target = package / name
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()

        source = fresh / name
        if source.is_dir():
            shutil.copytree(source, target)
        elif source.exists():
            shutil.copyfile(source, target)


def main() -> None:
    with tempfile.TemporaryDirectory(dir=REPO, prefix=".generate-") as tmp:
        fresh = pathlib.Path(tmp) / "client"
        generate_into(fresh)
        install(fresh)
    print(f"generated {PACKAGE.relative_to(REPO)} ({', '.join(GENERATED_PATHS)})")
    # The facade is projected from the same spec, so it moves in the same step.
    subprocess.run([sys.executable, str(REPO / "scripts" / "generate_facade.py")], check=True)


if __name__ == "__main__":
    main()
