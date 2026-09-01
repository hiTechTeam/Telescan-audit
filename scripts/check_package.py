#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


PACKAGE_ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = {
    "README.md",
    "SCOPE.md",
    "REPOSITORIES.md",
    "ARCHITECTURE.md",
    "DATA_FLOW.md",
    "THREAT_MODEL.md",
    "API_SURFACE.md",
    "CONTROL_MATRIX.md",
    "SOURCE_MAP.md",
    "PRIVACY_AND_RETENTION.md",
    "SUPPLY_CHAIN.md",
    "BUILD_AND_TEST.md",
    "DEPLOYMENT.md",
    "APP_REVIEW.md",
    "AUDITOR_ACCESS.md",
    "OPEN_RISKS.md",
    "P0_REMEDIATION.md",
    "HANDOFF_CHECKLIST.md",
    "templates/FINDING.md",
    "templates/RETEST.md",
    "evidence/README.md",
    "evidence/BASELINE.md",
    "evidence/CI_RUNS.md",
    "evidence/DEPLOYMENT_STATUS.md",
    "evidence/EXTERNAL_SURFACE.md",
    "evidence/TEST_RESULTS.md",
    "evidence/P0_LOCAL_VERIFICATION.md",
    "scripts/hash_package.py",
}
LINK_PATTERN = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "JWT-like value": re.compile(r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\."),
    "Telegram token": re.compile(r"\b\d{8,12}:[A-Za-z0-9_-]{30,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}


def markdown_files() -> list[Path]:
    return sorted(PACKAGE_ROOT.rglob("*.md"))


def check_required(errors: list[str]) -> None:
    for relative in sorted(REQUIRED_FILES):
        if not (PACKAGE_ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_links(path: Path, text: str, errors: list[str]) -> None:
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = unquote(target.split("#", maxsplit=1)[0])
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        if not resolved.exists():
            errors.append(
                f"broken relative link in {path.relative_to(PACKAGE_ROOT)}: {target}"
            )


def check_secrets(path: Path, text: str, errors: list[str]) -> None:
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            errors.append(
                f"possible {label} in {path.relative_to(PACKAGE_ROOT)}"
            )


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        check_links(path, text, errors)
        check_secrets(path, text, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Audit package check passed: {len(markdown_files())} Markdown files, "
        "required files present, relative links valid, no known secret patterns."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
