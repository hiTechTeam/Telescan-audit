# Pre-Release Verification Results

**Date:** September 2, 2026

**Evidence class:** Local verification plus exact-SHA remote CI confirmation

| Component/check | Result |
| --- | --- |
| API Ruff formatting/lint | Passed |
| API Pyright | Passed — 0 errors |
| API pytest | Passed — 157 tests |
| User-bot Ruff formatting/lint | Passed |
| User-bot Pyright | Passed — 0 errors |
| User-bot pytest | Passed — 44 tests |
| Admin-bot Ruff formatting/lint | Passed |
| Admin-bot Pyright | Passed — 0 errors |
| Admin-bot pytest | Passed — 41 tests |
| MongoDB validation | Passed — 10 Python tests, Node contract fixtures, restore-invariant fixtures, deployment fault/recovery fixtures |
| nginx immutable transaction | Passed rollback/success, child termination, durable gate, and outer-session recovery fixtures |
| EU relay immutable transaction | Passed rollback/success, child termination, and outer-session recovery fixtures |
| Monitoring validation | Passed safety gates, negative attestation inventory, immutable transaction, YAML and dashboard JSON checks |
| Canonical legal source | Generated documents current; both public origins matched version and SHA-256 |
| iOS remote XCTest | Passed in GitHub Actions on Xcode 26.3 |
| iOS remote Release build/bundle validation | Passed |
| iOS local unsigned Release simulator build | Passed |
| Release bundle | `hiTeam.TelescaniOS`, version `1.0`, build `2`, production API origin, Bluetooth central/peripheral modes, privacy manifest present |
| All repositories | `git diff --check` passed; no tracked `.env`, private-key, provisioning-profile, or signing-key candidates found |

## Local XCTest runner limitation

The local XCTest invocation compiled the application and tests and reached
`Testing started`, but CoreSimulator stalled while waiting for workers to
materialize. It was interrupted after 270 seconds and is not counted as a local
runtime pass. Exact-SHA GitHub Actions run `33678047504` independently completed
XCTest and the Release build successfully.

## Evidence still required for formal release acceptance

- Publishing-team signed Archive/TestFlight build and final Apple-first login.
- Recorded iOS 17.6/18/26 regression and signed two-device BLE/background matrix.
- Current-schema encrypted production-snapshot restore with observed backup age
  and elapsed restore time.
- Full sanitized production attestation, restricted-ingest/alert-delivery drill,
  immutable image mapping, and dated rollback exercise.
- App Store Connect privacy answers, screenshots/metadata, and release-owner
  sign-off.
