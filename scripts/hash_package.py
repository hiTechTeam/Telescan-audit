#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_NAMES = {"PACKAGE_HASHES.sha256"}
EXCLUDED_PARTS = {".git", "__pycache__", ".DS_Store"}


def included_files() -> list[Path]:
    return sorted(
        path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and path.name not in EXCLUDED_NAMES
        and not EXCLUDED_PARTS.intersection(path.parts)
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_manifest() -> str:
    lines = []
    for path in included_files():
        relative = path.relative_to(PACKAGE_ROOT)
        lines.append(f"{sha256(path)}  {relative.as_posix()}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate the audit package SHA-256 manifest."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="atomically replace PACKAGE_HASHES.sha256",
    )
    args = parser.parse_args()
    manifest = render_manifest()
    if args.write:
        target = PACKAGE_ROOT / "PACKAGE_HASHES.sha256"
        temporary = PACKAGE_ROOT / ".PACKAGE_HASHES.sha256.tmp"
        try:
            temporary.write_text(manifest, encoding="utf-8")
            temporary.replace(target)
        finally:
            temporary.unlink(missing_ok=True)
    else:
        sys.stdout.write(manifest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
