# Disclosed Open and Accepted Risks

These items are disclosed before testing so auditors can distinguish a known
design constraint from an undiscovered defect. Auditors should still validate
the stated boundary and may raise a finding if actual impact exceeds it.

Severity and acceptance are provisional until the release owner signs the
baseline.

The table describes the September 2 pre-release baseline. Source and deployment
status are current; acceptance remains provisional until the release owner signs
the baseline.

| ID | Risk | Provisional severity | Current treatment | Decision |
| --- | --- | --- | --- | --- |
| R-001 | Stable BLE Telescan IDs can be observed, correlated, and replayed | Medium | Random non-Telegram identifier; authenticated profile lookup; documented limitation | Accept for MVP; rotating authenticated protocol is future research |
| R-002 | Knowing a valid Telescan ID permits authenticated lookup without cryptographic proof of physical proximity | Medium | UUID entropy, authentication, bidirectional blocks | Accept for MVP; do not present BLE as proof of presence |
| R-003 | Account deletion spans MongoDB collections and object storage rather than one transaction | Medium residual | Deployed durable idempotent deletion journal, sessions-first revocation, retryable cleanup, reconciliation tests | Open operational evidence: production-like interruption/recovery exercise |
| R-004 | Apple-to-Telegram adoption spans multiple database and storage writes | Medium residual | Deployed durable replay-bound merge journal, conflict fencing, session migration/revocation, retryable cleanup | Open operational evidence: production-like interruption/reconciliation exercise |
| R-005 | Python base images are not digest-pinned and the uv installer is fetched without a committed checksum | Medium | Lockfiles, CI, minimal images | Open: pin reviewed image digests and installer artifact/checksum |
| R-006 | Private implementation repositories cannot enforce all desired branch/secret protections on the current GitHub plan | Medium | Procedural PR and green-CI gates | Open: upgrade controls or add independent receiving-side enforcement |
| R-007 | Automated iOS UI coverage does not yet span iOS 18/26 gesture and navigation behavior | Medium | Unit tests plus manual physical/simulator testing; build CI | Open: XCUITest/device matrix and long-running BLE/power tests |
| R-008 | Rate-limit thresholds use fixed windows and require production calibration | Medium | Shared MongoDB counters and endpoint-specific scopes | Open: measure, tune, and test distributed abuse patterns |
| R-009 | Legacy `/v1` compatibility would weaken the Apple-first boundary if re-enabled | High when enabled | Production startup rejects enablement; current deployment/migration workflow succeeded; routes remain hidden | Closed for current release behavior; any bypass is a new High-risk exception |
| R-010 | EU TLS relay adds a plaintext-within-process trust point and availability dependency | Medium | WireGuard origin hop, hardened edge, health monitoring | Accepted topology; protect/monitor relay as sensitive infrastructure |
| R-011 | Moderation is an allow-listed bot without granular roles, assignment, appeals, or formal SLA | Low/Medium | Separate secret and actor audit data | Accept for MVP; expand when case volume requires it |
| R-012 | Compromise of an unlocked device may expose local public Met/Saved snapshots | Low | App container, 24-hour Met retention, session cleanup; no GPS/distance upload | Accepted device threat; reassess encrypted local storage if sensitivity changes |
| R-013 | Monitoring and Telegram alerting are centralized and dependency updates require some manual review | Low/Medium | Cross-host telemetry and missing-signal alerts | Open: tune burn-in, exercise alert failure, enable/replace dependency alerting |
| R-014 | Source-controlled topology does not prove current production DNS, firewall, image, or secret state | Medium verification gap | Operational documentation and CI checks | Close for audit with dated production attestation and external surface evidence |

## P0 deployment disposition

| Risk | Deployed change | Residual acceptance requirement |
| --- | --- | --- |
| R-003 | Durable idempotent deletion journal is deployed and exact-SHA failure tests passed | Production-like object-storage recovery evidence remains open |
| R-004 | Durable replay-bound merge journal is deployed and exact-SHA concurrency/failure tests passed | Sanitized production invariant/reconciliation evidence remains open |
| R-009 | Production rejects legacy authentication and the current workflow completed migration/startup gates | Treat any re-enable request as a new High-risk exception |
| R-013 | Central monitoring is deployed and healthy; source includes restricted ingest, freshness/capacity rules, guarded Grafana key migration, and Telegram drill tooling | Real-host agent migration, firing/resolved observations, burn-in, and dependency governance remain open |
| R-014 | A September 2 smoke check covered public DNS/TLS/routes, core containers, WireGuard origin health, timers, backups, and central monitoring | Full sanitized collector output for firewall/SSH/listeners/mounts/image digests remains open |

R-003 and R-004 are remediated in deployed design but retain operational
recovery-evidence gaps. R-009 is closed for the current production behavior.
All other risks retain their stated disposition.

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
