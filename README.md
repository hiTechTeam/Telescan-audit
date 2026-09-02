# Telescan Audit Package

**Classification:** Confidential — authorized auditors and Telescan operators only  

**Prepared:** September 2, 2026

**Status:** Pre-release source baseline frozen; configured CI/CD green; server
production and public legal/health smoke evidence captured; signed App Store
build, current-schema restore, full attestation, and owner sign-off remain

## Purpose

This package gives an authorized security auditor a self-contained starting
point for reviewing the Telescan iOS application and its supporting services.
It defines the audit boundary, explains the security-critical data flows,
records the known residual risks, and provides reproducible build and test
instructions.

The package deliberately contains no production credentials, clear App Review
codes, user data, database snapshots, private keys, or `.env` files.

## Handoff gate

Every in-scope repository has a clean local working tree and a pre-release
commit SHA recorded in [REPOSITORIES.md](REPOSITORIES.md) and
[evidence/BASELINE.md](evidence/BASELINE.md). Those commits are published on
their authorized remotes. Configured CI/CD workflows are green, the current
server components completed their production workflows, and dated evidence is
linked
from [evidence/CI_RUNS.md](evidence/CI_RUNS.md) and
[evidence/DEPLOYMENT_STATUS.md](evidence/DEPLOYMENT_STATUS.md). Remaining
handoff gates are explicitly tracked in [HANDOFF_CHECKLIST.md](HANDOFF_CHECKLIST.md).
Use `scripts/hash_package.py` after every package update.

## Package map

| Document | Purpose |
| --- | --- |
| [SCOPE.md](SCOPE.md) | In-scope systems, exclusions, rules of engagement, and audit objectives |
| [REPOSITORIES.md](REPOSITORIES.md) | Repository inventory and baseline-freeze procedure |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Components, trust boundaries, and deployed request path |
| [DATA_FLOW.md](DATA_FLOW.md) | Authentication, BLE, profile, moderation, photo, and deletion flows |
| [THREAT_MODEL.md](THREAT_MODEL.md) | Assets, adversaries, threats, controls, and test hypotheses |
| [API_SURFACE.md](API_SURFACE.md) | Endpoint inventory, authority, and rate-limit review map |
| [CONTROL_MATRIX.md](CONTROL_MATRIX.md) | Security controls mapped to implementation and audit evidence |
| [SOURCE_MAP.md](SOURCE_MAP.md) | High-value code and configuration entry points by repository |
| [PRIVACY_AND_RETENTION.md](PRIVACY_AND_RETENTION.md) | Data inventory, ownership, storage, and retention |
| [SUPPLY_CHAIN.md](SUPPLY_CHAIN.md) | Dependency locks, images, build provenance, and SBOM expectations |
| [BUILD_AND_TEST.md](BUILD_AND_TEST.md) | Reproducible verification commands and current evidence |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Production topology, release flow, rollback, and operational boundaries |
| [APP_REVIEW.md](APP_REVIEW.md) | Safe Apple App Review code workflow |
| [AUDITOR_ACCESS.md](AUDITOR_ACCESS.md) | Least-privilege access and staging-data requirements |
| [OPEN_RISKS.md](OPEN_RISKS.md) | Accepted or unresolved risks disclosed before testing |
| [P0_REMEDIATION.md](P0_REMEDIATION.md) | Deployed P0 status, evidence, and remaining acceptance gates |
| [HANDOFF_CHECKLIST.md](HANDOFF_CHECKLIST.md) | Final operator checklist before granting access |
| [templates/FINDING.md](templates/FINDING.md) | Standard finding format |
| [templates/RETEST.md](templates/RETEST.md) | Remediation/retest record |
| [evidence/README.md](evidence/README.md) | Evidence policy and expected artifacts |
| [evidence/CI_RUNS.md](evidence/CI_RUNS.md) | Remote CI/CD results for the frozen SHAs |
| [evidence/DEPLOYMENT_STATUS.md](evidence/DEPLOYMENT_STATUS.md) | Production rollout and health evidence |
| [evidence/EXTERNAL_SURFACE.md](evidence/EXTERNAL_SURFACE.md) | Dated public endpoint smoke observations |
| [evidence/P0_LOCAL_VERIFICATION.md](evidence/P0_LOCAL_VERIFICATION.md) | Sanitized local and remote verification for the pre-release baseline |
| [PACKAGE_HASHES.sha256](PACKAGE_HASHES.sha256) | Integrity manifest for the current package contents |

## Auditor starting sequence

1. Confirm the signed scope and frozen repository manifest.
2. Read `ARCHITECTURE.md`, `DATA_FLOW.md`, and `THREAT_MODEL.md`.
3. Reproduce the builds and automated checks in `BUILD_AND_TEST.md`.
4. Review `OPEN_RISKS.md` before classifying duplicate or already accepted
   findings.
5. Request only the staging access required by `AUDITOR_ACCESS.md`.
6. Record findings using `templates/FINDING.md`, including the affected commit
   SHA and a minimally destructive proof of concept.

## Authoritative sources

This package summarizes, but does not replace, the implementation and the
private engineering documentation. Where a statement conflicts with code, the
frozen implementation is the security source of truth and the documentation
drift must be reported as a finding.

Public privacy and terms documents are product commitments. A conflict between
those commitments and the shipped behavior must be treated as a release blocker.
