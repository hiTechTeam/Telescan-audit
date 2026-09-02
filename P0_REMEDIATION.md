# P0 Remediation Status

**Reviewed:** September 2, 2026

**State:** coordinated source frozen on `main`; configured server workflows
deployed successfully; formal operational acceptance remains incomplete

The normative behavior is defined in the private
`Telescan-internal-docs/product/P0_CONTRACTS.md` file. Current pre-release SHAs
and exact CI/CD runs are recorded in [REPOSITORIES.md](REPOSITORIES.md) and
[evidence/CI_RUNS.md](evidence/CI_RUNS.md).

## Control status

| ID | P0 outcome | Current evidence | Remaining acceptance gate |
| --- | --- | --- | --- |
| P0-01 | One active Telegram code; replay-bound Apple-to-Telegram adoption; legacy auth prohibited in production | API and bot suites passed; current workflows deployed; public legacy/docs surface denied | Retain sanitized production migration/invariant output |
| P0-02 | Durable idempotent deletion with sessions revoked first and retryable cleanup | API failure/retry suites and current API deployment passed | Repeat interruption/reconciliation exercise against production-like storage |
| P0-03 | Account-scoped iOS reset and generation-bound async work | Exact-SHA XCTest and Release bundle CI passed; local Release build passed | Publishing-team signed TestFlight account-switch/reset matrix |
| P0-04 | Resolved-only BLE presentation/notification and complete block purge | Unit/regression CI passed; owner has repeatedly exercised physical BLE | Record the final signed two-device foreground/background matrix |
| P0-05 | Idempotent universal reports, retained evidence, revision-safe moderation | API/admin-bot suites and deployments passed | Retention/storage lifecycle and moderator operational drill |
| P0-06 | Canonical localized legal source and two-origin digest verification | Exact source equality passed; both public origins served version `2026-09-01` and the approved digest | Recheck immediately before submission if legal source changes |
| P0-07 | Fail-closed application/database configuration and storage routing | Negative configuration/Compose tests and production startup gates passed | Full sanitized configuration/host attestation |
| P0-08 | Encrypted backups and isolated restore validation | Backup timer active; latest job succeeded; prior-schema restore drill and current-schema tooling exist | Restore a current-schema encrypted production snapshot and record age/time |
| P0-09 | Main-only, serialized, crash-recoverable deployments with rollback | Exact-SHA workflows and fault-injected transaction fixtures passed across server repositories | Freeze image digests and retain a dated rollback exercise |
| P0-10 | Restricted monitoring, freshness/capacity alerts, guarded key migration and attestations | Central stack deployed and healthy; safety/negative attestation fixtures passed | Complete agent restricted-ingest, firing/resolved delivery, key migration, and three-host attestation evidence |

## App Store boundary

The iOS repository intentionally performs validation only; it does not upload to
TestFlight or App Store Connect. Final distribution requires the publishing
company's paid Apple Developer team, a registered `hiTeam.TelescaniOS` identifier
with Sign in with Apple, a new build number if build `2` was already uploaded,
and a signed Archive/TestFlight pass.

## Acceptance rule

Green source tests and successful deployment are necessary but not sufficient
to state that every P0 control is accepted in production. The unchecked items in
[HANDOFF_CHECKLIST.md](HANDOFF_CHECKLIST.md) must either be completed or receive
an explicit, dated owner risk decision.
