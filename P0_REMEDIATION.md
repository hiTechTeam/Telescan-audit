# P0 Remediation Delta

**Prepared:** September 1, 2026
**Candidate state:** Source commits created; partial remote publication only;
not frozen, deployed, or accepted

This is a delta over the historical baseline in [REPOSITORIES.md](REPOSITORIES.md)
and [evidence/BASELINE.md](evidence/BASELINE.md). It does not modify or supersede
that evidence. A release owner must freeze new commits and image digests before
any row can become final audit evidence.

The normative cross-repository behavior is defined in the private
`Telescan-internal-docs/product/P0_CONTRACTS.md` file. The table below maps that
contract to the implementation candidate.

## Publication and rollout status

On September 2, 2026, candidate commits were created in all ten affected source
repositories. `Telescan-iOS` and `Telescan-internal-docs` were pushed to `main`;
the protected `Telescan-info` repository was merged to `main` through green pull
request 13. Backend, database, relay, and monitoring candidates remain local
commits so their push-triggered production workflows cannot overtake the
required ingress bootstrap.

Nginx commit `06727db3acd57d218c07bb5a635f2b519053eeb3` was pushed to
`main`. Workflow run 26 passed candidate validation, then its production job
stopped during the fail-closed host prerequisite checks with exit code 2,
before `run-release-transaction.sh` was invoked. No successful P0 production
deployment is claimed. The Moscow host must first receive the reviewed
maintenance-marker runtime and nginx recovery units through the documented
provider-console bootstrap window.

## Candidate control map

| ID | P0 outcome | Owning repositories and primary source | Local verification | Acceptance state |
| --- | --- | --- | --- | --- |
| P0-01 | One active Telegram link code; durable, fenced and replay-bound Apple-to-Telegram adoption; canonical Telegram profile preserved; legacy auth prohibited in production | `Telescan-api`: `src/use_cases/auth.py`, `src/services/account_merges.py`, `src/repositories/account_merges.py`, `src/repositories/link_codes.py`, migration/invariant scripts; `Telescan-bot-app`: link-code client/config | API saga, conflict, replay, late-write fencing, configuration, migration, and bot contract tests | Code candidate implemented; production migration and invariant output pending |
| P0-02 | Durable, fenced and idempotent account deletion with sessions revoked first, final reference sweep, anonymization, and retryable photo cleanup | `Telescan-api`: `src/services/account_deletions.py`, `src/repositories/account_deletions.py`, `src/use_cases/profiles.py`; `Telescan-iOS`: coordinator reset | Injected interruption/retry, late-write/session rejection, and deletion integration tests | Code candidate implemented; production reconciliation pending |
| P0-03 | Complete account-scoped iOS reset and generation-bound asynchronous work | `Telescan-iOS`: `AccountSessionGeneration.swift`, `AuthSessionStore.swift`, `APIClient.swift`, `AppCoordinator.swift`, `PeopleVM.swift`, `PhotoVM.swift`, local stores/views | Same-process A-to-B, local-first offline/lost-response logout, no-primary startup, stale callback/refresh, injected Keychain deletion/read faults across restart, cache/list reset tests; simulator builds | Local compile and pre-final simulator evidence only; post-fix CI runtime, signed TestFlight and device matrix pending |
| P0-04 | Raw BLE remains untrusted; only a complete current authenticated profile can notify; block purges every encounter surface while Saved stays hidden | `Telescan-iOS`: `BLEManager.swift`, `PeopleVM.swift`, people/profile views, coordinator and quick-action store; `Telescan-api`: block-aware profile use case | Raw/failed/stale resolution, queue-ordered source epochs, delayed advertising/service/GATT callbacks across reset and scan re-enable, per-peripheral single-flight, stale/overlapping block-sync guards, process-interruption recovery, notification, persistence and Met/Saved tests | Local compile and pre-final simulator evidence only; post-fix CI runtime and physical two-device BLE/background evidence pending |
| P0-05 | Stable report idempotency, optional 0–500 comment, separately retained photo evidence, 180-day closed retention, revision-CAS moderation and immutable events | `Telescan-iOS`: request model, fetch service, people/profile report UI; `Telescan-api`: moderation use case/router/repository, evidence service, documents/migrations; `Telescan-admin-bot`: models/client/handlers/presentation | Duplicate/retry, evidence failure/recovery, transition, stale revision, tri-state note, config and bot rendering/client tests | Code candidate implemented; storage lifecycle and moderator drill pending |
| P0-06 | One canonical localized legal source with generated public documents, exact API vendoring, version/digest headers and two-origin deployment check | `Telescan-info`: `legal/legal_documents.json`, generator/workflow; `Telescan-api`: vendored JSON, legal renderer/router and sync/deployment scripts | Generator equality/date/URL checks, API legal tests, exact source sync | Local digest matched; publication and both-origin production check pending |
| P0-07 | Fail-closed production application/database configuration and exact storage routing | `Telescan-api`: `src/core/config.py`, S3 adapter/tests; `Telescan-db`: compose validator and application-role validator | Negative configuration matrix, exact host/bucket/public URL checks, compose-validator tests | Local validation implemented; sanitized production config attestation pending |
| P0-08 | Consistent encrypted backups and current-schema isolated restore validation | `Telescan-db`: backup supervisor, restore drill, exact index allowlist, strict domain/reference/type and application-role validators, timer-aware deployment | Static/unit/config checks; missing, malformed, reordered and extra-index negatives; restore-invariant and interrupted-lock fixtures | Tooling candidate implemented; real current-schema snapshot, timer state, RPO/RTO pending |
| P0-09 | `main`-only, host-serialized and crash-recoverable deploys with semantic preflight, immutable releases, prior-image preservation and automatic rollback | API, both bots, DB, nginx, relay, and monitoring workflows plus durable deploy controllers/recovery units | Workflow YAML and shell checks; fault-injected rollback, child/outer termination, power-loss boundary, recovery-lock and health-gate fixtures | Local source checks implemented; guarded first installation, dated non-production rollback and production image mapping pending |
| P0-10 | Restricted monitoring ingestion, missing/stale/capacity/backup alerts, guarded Grafana key migration, Telegram delivery drill, and fail-closed production attestation | `Telescan-monitoring`: Compose/config, rules, collectors, safety checks and runbooks; nginx/relay host checks | Promtool positive/negative fixtures, Alloy/nginx/Compose checks, self-signed TLS and missing-state negative tests | Local tooling implemented; staged host migration, firing/resolved delivery and three-host attestation pending |

## Compatibility and release order

The candidate is coordinated and must not be split into arbitrary independent
deploys:

1. freeze all repository commits and immutable images, then regenerate this
   package's repository and hash manifests;
2. take and validate a consistent backup;
3. deploy additive database indexes/journal/evidence fields and run dry-run
   invariant audits;
4. deploy the API with old/new bot-payload compatibility;
5. deploy user and admin bots, then require moderation revisions;
6. deploy iOS through a signed TestFlight candidate and run the physical matrix;
7. publish legal pages only with the matching API behavior and digest;
8. stage restricted telemetry ingestion and Grafana-key migration according to
   their rollback runbooks;
9. collect rollback, restore, telemetry, Telegram, public-origin and three-host
   attestation evidence; and
10. create a new accepted audit baseline only after owner sign-off.

## Release blockers outside source control

The following cannot be completed by a local source edit and remain P0
acceptance gates:

- production credentials/configuration review and legacy-data migration;
- a current-schema restore from an encrypted production snapshot with observed
  backup age and restore time;
- signed Apple/TestFlight authentication and two-device physical BLE/background
  behavior;
- production rollout and rollback exercises against frozen image digests;
- restricted-ingest and Grafana secret-key migrations on the real monitoring
  host;
- observed Telegram firing and resolved messages;
- read-only DNS, TLS, listener, firewall, WireGuard, SSH, filesystem, timer,
  published-port, and running-image attestations; and
- release-owner risk decisions and audit-baseline sign-off.

Absence of those artifacts is not a code-test failure, but it prevents the
statement “all P0 is accepted in production.”
