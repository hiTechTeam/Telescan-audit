# Dependency and Supply-Chain Review

## Dependency sources

| Component | Lock/inventory source | Runtime installation |
| --- | --- | --- |
| iOS | SwiftPM `Package.resolved` | Xcode/SwiftPM resolved revisions |
| API | `pyproject.toml` plus `uv.lock` | `uv sync --frozen --no-dev` in container |
| User bot | `pyproject.toml` plus `uv.lock` | `uv sync --frozen --no-dev` in container |
| Admin bot | `pyproject.toml` plus lockfile | Repository Docker/CI process |
| nginx/relay/database/monitoring | Compose image references and Dockerfiles | Docker/Compose |

Development test dependencies are separated from API and user-bot runtime
installations.

## iOS frozen packages at preparation time

These values are informational until the final audit SHA is frozen:

| Package | Version | Revision |
| --- | --- | --- |
| Kingfisher | `8.6.2` | `d30a5fad881137e2267f96a8e3fc35c58999bb94` |
| swift-log | `1.8.0` | `bc386b95f2a16ccd0150a8235e7c69eab2b866ca` |
| swift-syntax | `602.0.0` | `4799286537280063c85a32f09884cfbca301b1a1` |
| swift-testing | `6.2.3` | `48a471ab313e858258ab0b9b0bf2cea55a50cefb` |

## Current image-pin posture

- Relay nginx/certbot and monitoring Grafana/Prometheus/Loki/Alloy images use
  version plus immutable digest in source.
- Database MongoDB and Restic references are version-tagged but not all are
  digest-pinned.
- API and user-bot Dockerfiles start from `python:3.13.0-slim` without an
  immutable digest.
- API and user-bot builds download the uv installer script without a committed
  checksum.

The last two points are disclosed as risk `R-005` and must not be described as
fully reproducible supply-chain builds.

## Required baseline artifacts

- Exact `Package.resolved`, all Python lockfiles, and Compose/Dockerfiles at the
  frozen SHAs.
- Resolved immutable digest for every built and pulled production image.
- Per-component CycloneDX or SPDX SBOM produced from the frozen source and final
  image, using a recorded scanner name/version.
- Vulnerability scan results with database timestamp and explicit disposition
  for every non-negligible finding.
- CI workflow identity, build timestamp, source SHA, image digest, and deployment
  environment record.
- App archive/build provenance, dependency revisions, entitlements, privacy
  manifests, and bundle-content inventory.

## Auditor checks

- Attempt a frozen/offline dependency resolution from approved caches.
- Compare source lockfiles with packages present in final artifacts/images.
- Inspect Docker layers for `.env`, keys, Git metadata, tests, caches, and build
  credentials.
- Review package install hooks, transitive native extensions, and compiler/build
  tools retained in runtime images.
- Confirm CI uses reviewed action revisions and least-privilege token scopes.
- Verify PR/build artifacts cannot overwrite the production release outside the
  protected environment gate.
- Confirm image rollback selects the recorded prior digest rather than an
  attacker-controlled mutable tag.
- Review Dependabot/provider alerts and document repositories where automated
  alerts are unavailable or disabled.

## Remediation target

Before claiming deterministic production builds, pin Python base images by
reviewed digest, replace the network-fetched uv installer with a verified pinned
artifact/checksum, and digest-pin remaining database/backup images. Regenerate
SBOM and provenance evidence after every pin update.

