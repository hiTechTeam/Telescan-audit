# Privacy, Data Inventory, and Retention

This document is an engineering inventory, not legal advice. The public Privacy
Policy and the shipped implementation must agree with it before release.

## Server-side data

| Data | Store | Purpose | Retention/deletion |
| --- | --- | --- | --- |
| Public Telescan profile | `users` | Nearby profile resolution | Active account lifetime; deleted with account |
| Apple subject and optional Apple name/email | `apple_identities` | Primary authentication | Active account lifetime; deleted with account |
| Telegram ID, public name, username | `users` | Shared Telegram profile | Active account lifetime; deleted with account |
| Current profile photo | S3-compatible storage plus URL in `users` | Public profile display | Until replacement/account deletion; obsolete objects cleaned after DB commit |
| Normal link-code HMAC digest | `link_codes` | One-time Telegram linking | Default validity 10 minutes; TTL deletion at expiry |
| App Review code HMAC digest and lifecycle metadata | `review_codes` | Controlled Apple review access | Configurable 1–60 days, operational default 30; deleted 90 days after expiry |
| Device ID, refresh-token digest, session timestamps | `device_sessions` | Per-installation authentication | Default refresh lifetime 30 days; revoked on logout/deletion; TTL at expiry |
| Shared rate-limit counters | `rate_limits` | Abuse control | TTL at the end of each window |
| Confirmation request metadata | `confirmation_requests` | Retained server confirmation contract | Default validity 5 minutes; TTL at expiry |
| Blocks and captured display context | `blocks` | Bidirectional access suppression and management UI | Until unblock or either account deletion |
| Report identifiers, optional comment, target snapshot, moderator lifecycle | `reports` | Abuse review and audit | Pending while reviewed; resolved/dismissed scheduled for deletion after 180 days |

Only HMAC/SHA-256 derivatives of clear link and refresh values are stored. This
does not make short codes equivalent to passwords; entropy, rate limits, TTL,
and one-time atomic consumption remain necessary controls.

## Device-local data

| Data | iOS storage | Retention/deletion |
| --- | --- | --- |
| Access/refresh tokens | Keychain | Cleared on local sign-out, deletion, or invalid primary session |
| Installation `device_id` | Keychain | Remains as an unlinked installation identifier after account deletion |
| Profile/registration/scanning state | `UserDefaults` | Cleared with the local account session |
| Cached blocked IDs | `UserDefaults` | Current account session; refreshed from API |
| Met public profile snapshots and last-seen time | `UserDefaults` | Maximum 24 hours; also manual clear, block, sign-out, or deletion |
| Saved public profile snapshots | `UserDefaults` | Until explicit removal, sign-out, or deletion; never synchronized |
| Unresolved BLE identities and timestamps | `UserDefaults` | Bounded safety buffer and age pruning |
| RSSI, distance, current nearby presentation | Memory/local processing | Not uploaded; transient except documented encounter checkpoints |
| Selected/cached images and HTTP cache | App container/cache | Replaced or cleared through application/session lifecycle and OS cache policy |

## Data not intentionally collected

- GPS location or server-side movement history.
- Telegram messages, contacts, or passwords.
- Advertising identifiers.
- Server-side RSSI or precise-distance history.
- Third-party advertising or behavioral analytics data.

## Deletion behavior

1. Server sessions are revoked first.
2. Photos, normal and Review codes, confirmations, blocks, Apple identity,
   device sessions, and the live user are removed.
3. Reports are anonymized rather than immediately erased when limited
   moderation retention still applies.
4. iOS clears tokens, profile caches, Met, Saved, blocked-ID cache, quick-action
   state, and in-memory account-specific singleton state.

Account deletion spans MongoDB collections and object storage and is not fully
transactional. Auditors should test safe retry after interruption at every
step; see risk `R-003` in [OPEN_RISKS.md](OPEN_RISKS.md).

## Audit reconciliation checklist

- Compare MongoDB TTL indexes with every duration stated above.
- Compare Privacy Policy wording with actual iOS upload requests.
- Confirm neither Met nor Saved has an API repository/endpoint.
- Confirm logs do not contain clear tokens, codes, Apple identity tokens, photo
  bytes, service secrets, or user-provided sensitive content beyond the minimum
  operational need.
- Verify backup retention and deletion limitations are disclosed consistently.
- Verify account deletion using synthetic data in every collection and photo
  storage.

