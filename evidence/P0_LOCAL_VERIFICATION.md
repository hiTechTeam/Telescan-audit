# P0 Local Candidate Verification

**Date:** September 1, 2026

**Evidence class:** Committed release-candidate verification with partial remote
publication

**Production evidence:** No

This file records sanitized checks run before the candidate commits below were
created. The results do not establish immutable image digests or production
acceptance and do not supersede `BASELINE.md`, `CI_RUNS.md`,
`DEPLOYMENT_STATUS.md`, or `TEST_RESULTS.md`.

## Candidate scope

All 11 repositories were on `main` when the candidate was prepared. The audit
package records its own commit in repository history rather than embedding a
self-referential SHA.

| Repository | Candidate SHA | Remote state on September 2, 2026 |
| --- | --- | --- |
| `Telescan-api` | `3a2fb7dec54471267945ae06fbb0ffd729160c70` | Local commit; push-triggered deployment held |
| `Telescan-bot-app` | `be8d30e1df4f4ba17a5a54135eb26fe1b5de0808` | Local commit; push-triggered deployment held |
| `Telescan-admin-bot` | `8ffbc7dbe685b6f13e2c56e0b622a945f1b48d39` | Local commit; push-triggered deployment held |
| `Telescan-db` | `8003cca1e7a05b4bcdd3b474c1a0db6410057a83` | Local commit; push-triggered deployment held |
| `Telescan-nginx` | `06727db3acd57d218c07bb5a635f2b519053eeb3` | Pushed to `main`; validation passed; production preflight stopped before mutation |
| `Telescan-relay` | `6958d17fe3dafaae9fe4e7a936b45893d0abd85b` | Local commit; push-triggered deployment held |
| `Telescan-monitoring` | `f190db9c4e4ca10bc04f079d62ee746f8ff6a581` | Local commit; push-triggered deployment held |
| `Telescan-info` | `59176141e495f26d47d86144af225d0026c71cda` | Green pull request 13 rebased and merged to `main` |
| `Telescan-iOS` | `01dbdc0d3534c36b43aee0ebec50f67a0a1ab88d` | Pushed to `main`; CI run 36 in progress at evidence capture |
| `Telescan-internal-docs` | `a249ca7bc0ed385563e4d97796bc8702fa3c233f` | Pushed to `main` |

## Results

| Area | Sanitized local result |
| --- | --- |
| API | Ruff and format clean; Pyright reported zero errors; `pytest` passed 152 tests; account-saga, evidence-retention, S3 partial-delete, deployment fault and recovery fixtures passed. |
| User bot | Ruff and format clean; Pyright reported zero errors; 44 tests passed; immutable deployment and power-loss recovery fixtures passed. |
| Admin bot | Ruff and format clean; Pyright reported zero errors; 41 tests passed; immutable deployment and power-loss recovery fixtures passed. |
| Database | 10 Python tests passed; exact index, restore reference/type/fence, Compose routing, backup-lock and deployment rollback/recovery fixtures passed. The index gate rejects missing, reordered, malformed and extra non-primary indexes. |
| iOS | The full pre-final simulator suite passed 82 of 82 tests and the Release arm64 simulator build succeeded. After the last two race fixes, `build-for-testing` compiled the app and all tests successfully and six deterministic regression tests were added for local-first logout/A-to-B isolation and stale block synchronization. Two focused runtime attempts were cancelled because local CoreSimulator workers did not materialize, so a post-fix runtime pass is not claimed. |
| Legal | Generator/checks and Ruff passed. Canonical and API-vendored JSON were byte-identical with SHA-256 `f3bddc01a0013a89086044509ba85e1e63edc6bde7e45732a7e0c9803257045e`. |
| Nginx and relay | Exact Docker candidate preflights passed. Each immutable release transaction passed success, rollback, child/outer termination, online/boot recovery and fail-closed lock fixtures; the owner-scoped API maintenance gate passed five scenarios. |
| Monitoring | Immutable transaction/recovery fixtures passed. Pinned Prometheus `v3.14.0` passed 10 groups, 12 expressions and 13 expected samples; pinned Alloy `v1.18.1` passed central and agent checks; restricted-ingest nginx passed. Exact attestation accepted three role inventories and rejected ten negative fixtures. |
| Cross-repository source hygiene | Workflow YAML, changed shell syntax and repository-specific Compose/JSON checks passed. `git diff --check` passed in every repository. The audit package checker and regenerated SHA-256 manifest passed after this evidence update. |

## Limited remote rollout evidence

- Nginx workflow run 26 validated the Docker/transaction candidate successfully.
  Its production job exited during the silent fail-closed host prerequisite
  comparisons, before the release transaction command. This is consistent with
  the documented first-install recovery/maintenance bootstrap still being
  required; it is not production deployment evidence.
- iOS and internal documentation commits reached `main` without initiating a
  backend production release.
- Legal source reached `main` through protected-branch pull request 13 after its
  validation check passed.

The deployment fixtures exercise source-controlled failure behavior with local
mocks or local Docker. They are not evidence that recovery units, firewalls,
secrets, images, mounts, timers or maintenance gates are installed correctly on
the production hosts.

`scripts/check_package.py` is a structural check: it verifies required files,
relative links and a small set of known secret patterns. It is not a semantic
security review or a general secret scanner.

## Evidence not produced locally

- No successful P0 production deployment occurred. The nginx production job was
  triggered but stopped before release mutation; the other push-triggered
  backend/database/infrastructure workflows were deliberately held.
- No production database, object storage, secret, DNS, firewall, or host state
  was read or changed.
- No encrypted production snapshot was restored and no current RPO/RTO was
  measured.
- No signed TestFlight build or physical two-device BLE test was performed.
- No post-fix iOS runtime result is claimed because CoreSimulator did not
  materialize a test worker; CI/device rerun remains required at the frozen SHA.
- No production Telegram alert, restricted-ingest migration, Grafana key
  migration, or three-host attestation was performed.
- Candidate source commits exist, but no new accepted baseline, container
  digests, SBOMs, or provenance artifacts were frozen.
- Release/security-owner sign-off was not provided.
