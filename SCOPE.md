# Audit Scope and Rules of Engagement

**Proposed review type:** source-assisted application, API, infrastructure, and
privacy/security design audit.

## Objectives

The audit should determine whether Telescan:

1. authenticates Apple identities and device sessions safely;
2. links Telegram profiles without allowing code replay, profile takeover, or
   cross-account confusion;
3. enforces authorization and blocking server-side rather than trusting iOS;
4. protects service credentials, signing secrets, MongoDB, photo storage, and
   internal endpoints;
5. minimizes BLE and local-device data consistently with the public privacy
   policy;
6. handles reports, moderator access, deletion, retention, and idempotency as
   documented;
7. can be built, deployed, rolled back, monitored, backed up, and restored
   without silently weakening the trust boundary;
8. exposes known residual risks clearly enough for a release decision.

## In-scope repositories

- `Telescan-iOS`
- `Telescan-api`
- `Telescan-bot-app`
- `Telescan-admin-bot`
- `Telescan-nginx`
- `Telescan-relay`
- `Telescan-db`
- `Telescan-monitoring`
- `Telescan-info`
- `Telescan-internal-docs`

Exact commit SHAs must be frozen in [REPOSITORIES.md](REPOSITORIES.md) before
testing begins.

## In-scope security surfaces

- Sign in with Apple verification, nonce handling, identity adoption, and
  conflict behavior.
- Normal Telegram link codes and separate App Review codes.
- Access JWTs, refresh-token rotation/reuse detection, active session checks,
  logout, and account deletion.
- Profile lookup, BIO/photo changes, Saved/Met local state, reports, blocks, and
  moderator operations.
- BLE advertisement, GATT identity exchange, background restoration, replay and
  correlation exposure, and local persistence.
- Public, authenticated, bot-service, moderation-service, and legacy API routes.
- MongoDB indexes and TTLs, S3-compatible photo ownership, backups, migration
  scripts, and failure compensation.
- EU relay, Moscow origin, WireGuard boundaries, nginx route denial, TLS,
  container hardening, CI/CD, monitoring, and secret handling.
- Privacy manifest, Privacy Policy, Terms, retention claims, and deletion
  behavior.

## Out of scope unless separately authorized

- Apple, Telegram, GitHub, cloud-provider, or S3-provider internals.
- Social engineering of users, moderators, operators, or provider support.
- Denial-of-service, destructive production testing, credential stuffing, RF
  jamming, or testing unrelated public infrastructure.
- Physical-device extraction beyond the supplied test devices.
- Legal advice or certification of regulatory compliance.
- Source review of third-party dependencies beyond their integration,
  configuration, provenance, and known-vulnerability posture.

## Rules of engagement

- Use staging and synthetic accounts by default.
- Do not access or copy real user data.
- Do not test production without written authorization specifying source IPs,
  time window, rate limits, endpoints, and emergency contacts.
- Never place secrets or clear Review codes in findings, screenshots, chat,
  issue trackers, or source control.
- Stop immediately if a test risks cross-user access, persistent data loss,
  provider abuse controls, or service availability.
- Report critical findings through the agreed private emergency channel before
  continuing related exploitation.
- Proofs of concept must use the minimum data and requests needed to establish
  impact.

## Finding severity

| Severity | Meaning |
| --- | --- |
| Critical | Practical account/service compromise, broad sensitive-data exposure, production secret compromise, or destructive control of core infrastructure |
| High | Cross-account access, durable authorization bypass, exploitable internal-service exposure, or material deletion/privacy failure |
| Medium | Meaningful defense failure requiring preconditions, limited information exposure, or reliability flaw with security consequences |
| Low | Hardening gap, limited metadata issue, or low-impact deviation from intended controls |
| Informational | Documentation, maintainability, or defense-in-depth recommendation without direct security impact |

## Expected deliverables

- Executive summary and release recommendation.
- Findings with severity, affected repository/SHA, evidence, impact,
  reproduction, and remediation guidance.
- Coverage statement describing what was and was not tested.
- Retest report mapping each accepted fix to a new commit SHA.
- Separate disclosure of documentation/privacy mismatches even when the code is
  not directly exploitable.

