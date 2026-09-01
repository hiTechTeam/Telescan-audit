# Auditor Access and Test Environment

## Principle

Grant the least privilege needed for the signed scope, prefer staging and
synthetic identities, time-bound every credential, and revoke access immediately
after the final retest.

## Recommended access matrix

| Resource | Default access | Notes |
| --- | --- | --- |
| In-scope GitHub repositories | Read-only | Exact repositories and frozen SHAs only |
| CI results/artifacts | Read-only | Sanitized logs; no environment secrets |
| Staging iOS build | TestFlight/internal distribution | Separate from production user data |
| Synthetic Apple identities | Test-only | No personal Apple accounts supplied by Telescan |
| Synthetic Telegram Review A/B | Controlled test use | No real chats, contacts, phone numbers, or personal profile data in evidence |
| Staging API | Authorized dynamic testing | Production-equivalent security settings and isolated data |
| Staging user/admin bots | Synthetic accounts and tokens | Distinct from production tokens |
| Staging MongoDB/photo storage | Read-only by default | Temporary scoped credentials only if source/API testing is insufficient |
| Sanitized monitoring/logs | Read-only | Filter personal data and secrets before sharing |
| Production | No access by default | Requires separate written rules of engagement |

## Staging requirements

- Same security-sensitive configuration shape as production.
- Distinct JWT, code-HMAC, service, database, storage, bot, TLS, SSH, and
  WireGuard credentials.
- Synthetic database and photo objects only.
- Ability to reset accounts, sessions, rate limits, reports, blocks, and Review
  codes without affecting production.
- Request and audit logs sufficient to correlate tests without logging secrets.
- Monitoring contact able to distinguish planned tests from an incident.
- Tested backup/reset procedure for the staging environment.

## Credential delivery

1. Name an owner for each credential and access grant.
2. Deliver credentials through the agreed encrypted secret-sharing channel,
   never through Git, ordinary email, chat history, or this package.
3. Record only credential identifiers, scope, issuer, issue time, expiry, and
   revocation confirmation—not secret values.
4. Require MFA for GitHub, cloud, Telegram operator, and administrative access
   where available.
5. Rotate any shared long-lived value after the engagement even if no compromise
   is suspected.

## Production exception record

Complete and approve this block before any production test:

```text
Change/authorization ID: PENDING
Approved auditor source IPs: PENDING
Allowed hosts and endpoints: PENDING
Start/end UTC: PENDING
Maximum request rate and volume: PENDING
Prohibited actions/data: PENDING
Monitoring contact: PENDING
Emergency stop contact: PENDING
Rollback/containment owner: PENDING
```

## Offboarding

- Revoke repository, CI, staging, VPN, SSH, bot, cloud, database, storage, and
  monitoring access.
- Revoke unused Review/test codes and delete synthetic accounts not needed for
  retest evidence.
- Rotate shared credentials.
- Remove auditor keys from allow-lists and hosts.
- Confirm the auditor's retention/destruction obligations for source, logs,
  screenshots, builds, and findings.
- Preserve only the agreed final report, sanitized evidence, and remediation
  record.

