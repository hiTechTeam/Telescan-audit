# Disclosed Open and Accepted Risks

These items are disclosed before testing so auditors can distinguish a known
design constraint from an undiscovered defect. Auditors should still validate
the stated boundary and may raise a finding if actual impact exceeds it.

Severity and acceptance are provisional until the release owner signs the
baseline.

The table is the historical frozen-baseline disclosure. The local P0 candidate
does not silently rewrite it; candidate disposition follows the table and is
not effective until a new baseline is frozen and accepted.

| ID | Risk | Provisional severity | Current treatment | Decision |
| --- | --- | --- | --- | --- |
| R-001 | Stable BLE Telescan IDs can be observed, correlated, and replayed | Medium | Random non-Telegram identifier; authenticated profile lookup; documented limitation | Accept for MVP; rotating authenticated protocol is future research |
| R-002 | Knowing a valid Telescan ID permits authenticated lookup without cryptographic proof of physical proximity | Medium | UUID entropy, authentication, bidirectional blocks | Accept for MVP; do not present BLE as proof of presence |
| R-003 | Account deletion spans MongoDB collections and object storage without a durable transaction/job | High | Sessions revoked first; repeated deletion/storage-prefix cleanup is designed to be safe where possible | Open: add durable idempotent deletion orchestration and reconciliation |
| R-004 | Apple-to-Telegram account adoption moves identity/session and deletes a placeholder user across multiple writes | Medium | Conflict checks and session revocation | Open: add transaction/saga or durable reconciliation |
| R-005 | Python base images are not digest-pinned and the uv installer is fetched without a committed checksum | Medium | Lockfiles, CI, minimal images | Open: pin reviewed image digests and installer artifact/checksum |
| R-006 | Private implementation repositories cannot enforce all desired branch/secret protections on the current GitHub plan | Medium | Procedural PR and green-CI gates | Open: upgrade controls or add independent receiving-side enforcement |
| R-007 | Automated iOS UI coverage does not yet span iOS 18/26 gesture and navigation behavior | Medium | Unit tests plus manual physical/simulator testing; build CI | Open: XCUITest/device matrix and long-running BLE/power tests |
| R-008 | Rate-limit thresholds use fixed windows and require production calibration | Medium | Shared MongoDB counters and endpoint-specific scopes | Open: measure, tune, and test distributed abuse patterns |
| R-009 | Legacy `/v1` compatibility weakens the current Apple-first boundary if re-enabled | High when enabled | Historical baseline allowed a bounded production window; P0 candidate prohibits production enablement and removes legacy code material | Close only after production config/migration attestation; any bypass is a new High-risk exception |
| R-010 | EU TLS relay adds a plaintext-within-process trust point and availability dependency | Medium | WireGuard origin hop, hardened edge, health monitoring | Accepted topology; protect/monitor relay as sensitive infrastructure |
| R-011 | Moderation is an allow-listed bot without granular roles, assignment, appeals, or formal SLA | Low/Medium | Separate secret and actor audit data | Accept for MVP; expand when case volume requires it |
| R-012 | Compromise of an unlocked device may expose local public Met/Saved snapshots | Low | App container, 24-hour Met retention, session cleanup; no GPS/distance upload | Accepted device threat; reassess encrypted local storage if sensitivity changes |
| R-013 | Monitoring and Telegram alerting are centralized and dependency updates require some manual review | Low/Medium | Cross-host telemetry and missing-signal alerts | Open: tune burn-in, exercise alert failure, enable/replace dependency alerting |
| R-014 | Source-controlled topology does not prove current production DNS, firewall, image, or secret state | Medium verification gap | Operational documentation and CI checks | Close for audit with dated production attestation and external surface evidence |

## P0 candidate disposition

| Risk | Candidate change | Residual acceptance requirement |
| --- | --- | --- |
| R-003 | Durable idempotent deletion journal revokes sessions first, anonymizes retained reports, retries database/object cleanup, and retains incomplete work for reconciliation | Injected-failure tests must be repeated at frozen commits; migration/invariant output and production-like object-storage recovery must be attached |
| R-004 | Durable merge journal binds the exact consumed-code proof, preserves the canonical Telegram profile, migrates/deduplicates references, and retries obsolete-photo cleanup | Frozen concurrency/failure evidence plus production dry-run invariants and post-migration reconciliation are required |
| R-009 | Production settings reject legacy authentication, and migration removes legacy user-code material and revokes legacy sessions | Production configuration and migration attestation are required; any requested bypass is a new High-risk exception |
| R-013 | Restricted write-only ingest, state freshness, backup/disk/inode/Loki alerts, guarded Grafana key migration, and an interactive Telegram drill are implemented in source | Real-host staged migration, both firing/resolved observations, burn-in, and dependency governance remain open |
| R-014 | A read-only, fail-closed three-role attestation collector now covers DNS, TLS, listeners, firewall, WireGuard, SSH policy, mounts, timers, ports, and image digests | Dated sanitized production output is still absent; the verification gap remains open |

R-003, R-004, and R-009 are therefore remediated in design and local source,
not yet closed operationally. All other risks retain their prior disposition.

## Risk acceptance record

For every accepted item, record:

```text
Risk ID:
Decision owner:
Decision date:
Release/build:
Reason accepted:
Compensating controls:
Review/expiry date:
Trigger for re-evaluation:
```

No entry is considered formally accepted merely because it appears in this
document.
