# Local Baseline Verification Results

**Date:** September 1, 2026  
**Evidence class:** Local verification plus remote CI confirmation

| Component/check | Result |
| --- | --- |
| API Ruff formatting/lint | Passed |
| API Pyright | Passed — 0 errors |
| API pytest | Passed — 62 tests |
| API uv lock | Passed — 49 packages resolved |
| User-bot Ruff formatting/lint | Passed |
| User-bot Pyright | Passed — 0 errors |
| User-bot pytest | Passed — 14 tests |
| User-bot uv lock | Passed — 30 packages resolved |
| Admin-bot Ruff formatting/lint | Passed |
| Admin-bot Pyright | Passed — 0 errors |
| Admin-bot pytest | Passed — 9 tests |
| iOS unsigned Release simulator build | Passed |
| iOS `build-for-testing` | Passed |
| iOS entitlement and Info plist validation | Passed |
| iOS English/Russian localization parity | Passed — 193 keys each |
| Changed-repository `git diff --check` | Passed before commit |

## XCTest runner limitation

A full local XCTest invocation built the application/test targets and reached
`Testing started`, but the Xcode runner stalled at `waiting for workers to
materialize`. The run was interrupted after 136 seconds and is not counted as a
passing local execution. GitHub Actions run `33492223348` subsequently completed
XCTest, the Release build, and final bundle validation successfully on Xcode
26.3. The workflow does not upload the `.xcresult`, so retain a result bundle in
an audit-specific rerun if required by the auditor.

## Evidence still required

- Completed XCTest result bundle if required beyond the retained CI logs.
- iOS 18/26 manual/device matrix and two-device BLE evidence.
- Deployment rollback, external surface, production attestation, SBOM/image
  digest, and latest backup/restore evidence.
