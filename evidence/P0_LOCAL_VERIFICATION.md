# P0 Pre-Release Verification

**Date:** September 2, 2026

**Evidence class:** Frozen-source local checks, exact-SHA CI/CD, and read-only
production smoke observations

The P0 source is no longer an unpublished working-tree candidate. Every listed
repository is on synchronized `main`, the configured exact-SHA workflows are
green, and the server workflows completed their current production deployments.
The authoritative SHAs are in [BASELINE.md](BASELINE.md); test and production
observations are in [TEST_RESULTS.md](TEST_RESULTS.md) and
[DEPLOYMENT_STATUS.md](DEPLOYMENT_STATUS.md).

## Verified outcomes

- Apple-first sessions, scoped Telegram linking, 90-day App Review batches,
  durable account merge/deletion journals, block-aware profile access, and
  universal report moderation passed API/bot tests and production deployment.
- iOS exact-SHA CI completed XCTest, a Release simulator build, and bundle
  validation. A second unsigned Release build passed locally.
- MongoDB configuration, index, application-role, restore-invariant, backup-lock,
  and deployment recovery fixtures passed; the production database and latest
  backup job were healthy.
- nginx, EU relay, and monitoring transaction/recovery fixtures passed locally,
  their exact-SHA workflows succeeded, and their current production services
  were healthy in the read-only smoke check.
- Both public legal origins served the canonical version and source hash; public
  Swagger and OpenAPI paths returned `404`.
- All repository trees were clean and synchronized after fetching remotes; no
  tracked runtime environment, private-key, or signing credential files were
  found.

## Operational evidence not implied

The checks above do not constitute a signed App Store build, full production
attestation, current-schema isolated restore, physical-device TestFlight matrix,
restricted-ingest migration proof, observed firing/resolved alert drill,
container SBOM/provenance set, or release-owner risk acceptance. Those remain
explicit handoff gates rather than hidden source failures.
