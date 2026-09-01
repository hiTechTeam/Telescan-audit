# Security Control and Evidence Matrix

The matrix is an audit index, not proof that a control is effective. Evidence
must be regenerated at the frozen commits.

| ID | Intended control | Primary implementation | Required evidence/test |
| --- | --- | --- | --- |
| AUTH-01 | Apple token signature, issuer, audience, expiry, and nonce verification | API Apple verifier and auth use case | Unit/negative tests with wrong key, audience, issuer, nonce, expiry, and unavailable Apple keys |
| AUTH-02 | Telegram code cannot create a primary session | Authenticated Telegram-link endpoint and legacy flag | Route/contract test; legacy disabled production attestation |
| CODE-01 | Normal link codes are random, short-lived, HMAC-stored, and single-use | `link_codes`, `LinkCodeService`, atomic repository consume | Concurrent consumption and database-index evidence |
| CODE-03 | At most one normal link code is active for a Telegram target, and consumed proof can resume only its prepared merge | Partial unique index, link-code repository, merge journal authorization | Concurrent issue/consume, mismatched-device/proof, completed-replay, migration invariant tests |
| CODE-02 | Review codes are separated, scoped, revocable, and retained for audit | `review_codes`, dedicated HMAC secret, `scripts/review_codes.py` | Cross-secret negative test, batch issue/status/revoke dry run, concurrent consume |
| SESS-01 | Refresh tokens are digested, rotated, and reuse-revoked | Device-session repository/service | Two-device and concurrent refresh/reuse tests |
| SESS-02 | JWT alone is insufficient after logout/deletion | Auth dependency checks active session and Apple identity | Protected-route matrix using revoked/deleted/expired sessions |
| AUTHZ-01 | Profile lookup is authenticated and block-aware in both directions | Profile use case and block repository | IDOR and bidirectional-block tests |
| ABUSE-01 | Sensitive endpoints use shared server-side rate limits | MongoDB fixed-window rate limiter/router scopes | Distributed/IP/device/user/token scope tests and TTL evidence |
| MOD-01 | Reports are idempotent and retain limited review context | Client UUID unique index, report snapshot, universal report use case | Duplicate/race tests and payload/rendering review |
| MOD-02 | Moderator and user-bot authority are separated | Distinct dependencies and production secrets | Credential-substitution tests; allow-list tests |
| MOD-03 | Moderation is revision-CAS protected, terminal, event-audited, and preserves report evidence for the closed retention window | Report/evidence service and repository, moderation events, admin-bot revision payload | Stale/missing revision, transition matrix, tri-state note, evidence copy/retry/cleanup tests |
| PHOTO-01 | Photo replacement avoids deleting the live object before DB commit | Upload → DB commit → obsolete cleanup with compensation | Injected storage/DB failures and orphan reconciliation |
| DELETE-01 | Account deletion removes owned data and revokes sessions first | DeleteAccount use case plus iOS local cleanup | Synthetic full-collection deletion and interruption/retry matrix |
| BLE-01 | BLE advertises only a random Telescan ID, not Telegram identity/token | BLE manager UUID characteristics | Packet/GATT inspection on physical devices |
| BLE-02 | RSSI/distance/Met/Saved remain local | iOS stores and network client | Traffic capture plus local storage inspection |
| LOCAL-01 | Local account transition clears account-specific Met/Saved/cache state | App coordinator and local stores | Same-process account-switch regression test |
| LOCAL-02 | Late asynchronous work cannot repopulate another account, and raw BLE cannot notify before authenticated complete resolution | Account generation, session-aware API client, People VM notification boundary | A-to-B stale refresh/profile/photo callback and unresolved/raw BLE notification tests |
| EDGE-01 | Internal/schema routes are denied publicly | EU/Moscow nginx route policy | External path/method/encoding matrix through every public host |
| EDGE-02 | API/MongoDB are not publicly bound | Compose/host firewall/WireGuard configuration | Dated listener scan from outside and on each host |
| CONF-01 | Production rejects development/duplicate secrets and unsafe CORS | API settings validator | Startup negative tests with each unsafe configuration |
| CONT-01 | Runtime containers are least-privilege and exclude secret/build debris | Dockerfiles, Compose, `.dockerignore` | Image-layer and runtime capability/mount inspection |
| DEPLOY-01 | Failed rollout restores prior application image | Serialized deployment workflow and health gate | Non-production migration/startup/health failure exercise |
| DEPLOY-02 | Only `main` may mutate production and all repositories sharing a host use the same OS lock | Workflows plus `/tmp/telescan-production-deploy.lock` | YAML/policy check and cross-repository contention exercise |
| BACKUP-01 | Backups are encrypted, off-host, verified, and restorable | Database backup/restore tooling | Dated checksum validation and isolated restore evidence |
| BACKUP-02 | Backup is consistent and current-schema restore proves domain/index integrity and least-privilege application access | fsync/quiesced backup and isolated restore validators | Real encrypted snapshot drill with backup age, elapsed restore time, index/reference results, and privilege-negative tests |
| MON-01 | Availability/security failures are observable | Prometheus/Loki/Alloy/Grafana/Telegram alerts | Alert rule tests, missing-telemetry test, alert-channel failure test |
| MON-02 | Monitoring ingest is write-only and runtime state claims are fresh; Grafana key changes and Telegram delivery are explicit drills | Restricted ingest proxy, state collectors/rules, guarded key migration, drill scripts | Promtool/config tests plus staged ingest, firing/resolved messages, and real-host evidence |
| PRIV-01 | Shipped behavior matches public collection/retention claims | iOS/API code, privacy manifest, public policy | Data inventory reconciliation and network/local storage test |
| LEGAL-01 | Public Markdown and API legal pages derive exactly from one localized, versioned, hashed source | `Telescan-info` legal generator/manifest and API vendored source/checker | Generator/sync check and both-origin TLS/version/digest smoke evidence |
| ATTEST-01 | Source topology is reconciled against live DNS, TLS, listeners, firewall, WireGuard, SSH, filesystems, timers, ports, and images | Fail-closed read-only production attestation collector | Dated sanitized three-role output at the frozen release |
| SUP-01 | Dependencies are frozen and artifacts trace to reviewed source | SwiftPM/uv locks, image digests, CI | SBOM, provenance, final-image inventory, vulnerability disposition |

## Control disposition fields

For the final audit, add a result for every row:

```text
Control ID:
Frozen repository/SHA:
Evidence reference:
Auditor result: Effective / Partially effective / Ineffective / Not tested
Related finding IDs:
Owner response:
```
