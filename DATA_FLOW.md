# Security-Critical Data Flows

## 1. Apple authentication and device session

1. iOS creates a nonce and invokes Sign in with Apple.
2. The API verifies token signature, issuer, audience, expiry, and nonce.
3. The stable Apple subject maps to an `apple_identities` record.
4. The API creates or replaces the `(user_id, device_id)` session.
5. iOS stores the access and refresh tokens in Keychain.
6. The server stores only a SHA-256 refresh-token digest.
7. Refresh rotates the token; reuse of the prior token revokes the affected
   session.

Audit focus: nonce binding, Apple key fetch failure behavior, subject/account
conflicts, session replacement, token reuse races, logout, and deleted users.

## 2. Telegram profile linking

1. The user bot reads only the current public Telegram ID, name, username, and
   explicit photo state.
2. The bot authenticates to the internal API with `BOT_SERVICE_SECRET`.
3. The API issues a random eight-character code, stores only its HMAC digest,
   and permits at most one active normal code for the Telegram target.
4. Authenticated iOS submits the clear code to
   `/api/v1/users/me/telegram/link`.
5. The API prepares a durable merge journal, atomically consumes the code, and
   binds the consumed digest/device proof to that exact operation.
6. Idempotent steps preserve the Telegram profile as canonical, migrate or
   revoke placeholder sessions, deduplicate domain references, and retry
   obsolete-photo cleanup. Interrupted work is resumed from the journal.
7. The API returns a replacement access token for the existing device session;
   the code itself never creates a session.

Audit focus: one-time atomicity, enumeration, HMAC separation, rate limiting,
identity-adoption partial failure, public-username validation, and code leakage.
Completed proof/journal metadata is bounded to 30 days; incomplete operations
remain until reconciled.

## 3. App Review codes

Review codes use the same iOS input and authenticated link endpoint but a
separate collection and HMAC secret. The API tries the normal-code store first
and the Review-code store second. Each code is scoped to one existing synthetic
review profile, consumed atomically once, and records lifecycle metadata. Clear
codes are displayed only once during batch issuance.

The default operational plan issues batches valid for 30 days and removes their
metadata 90 days after expiry. See [APP_REVIEW.md](APP_REVIEW.md).

## 4. BLE discovery and local history

1. Advertising exposes a fixed service UUID.
2. A scanner reads the peer's random public `telescan_id` as 16 bytes.
3. A compatible scanner writes its own ID plus observed RSSI back to the peer.
4. Each device resolves the ID through the authenticated profile endpoint.
5. The raw identifier creates no row, Met entry, badge, quick action, or
   notification. Only a complete authenticated, non-blocked resolution for the
   current account generation becomes user-visible.
6. RSSI and distance are processed locally.
7. A resolved profile leaving Nearby enters a persistent heartbeat buffer and
   then the local 24-hour Met list.
8. Explicitly Saved profiles persist only on that device.

Audit focus: replay/correlation, malformed GATT values, restoration state,
resource exhaustion, blocked-cache behavior, and cross-account local-state
cleanup. A cap remains only for unresolved BLE identifiers; resolved profile
history and its resolved transition buffer are not capped at 500.

Sign-out, deletion, invalid-session startup, and account replacement advance an
account generation before clearing state. Late network/refresh/photo/profile
callbacks captured under an older generation must be rejected.

## 5. Profile photos

For replacement, the API uploads the new object, commits the new URL to
MongoDB, and then deletes the obsolete object. If the database update fails,
the API attempts to remove the newly uploaded unreferenced object. Cleanup of an
obsolete object does not invalidate the now-live profile.

For deletion, the profile URL is cleared before object-prefix cleanup, allowing
a repeated delete request to finish storage cleanup after a partial failure.

Audit focus: object ownership, URL parsing, content validation, size limits,
orphan cleanup, retry behavior, and account-deletion races.

## 6. Reports, blocks, and moderation

- A report uses a client request UUID that iOS preserves across retry, including
  a successful-report/lost-response or later block failure.
- The comment is optional and limited to 500 characters.
- The API captures limited target-profile context and attempts a deterministic
  copy of the live photo to separate moderation evidence. It records
  `available`, `absent`, or `copy_failed` rather than conflating those states.
- Internal storage retains the universal `other` enum for schema compatibility.
- The admin bot is Telegram-ID allow-listed and uses a credential distinct from
  the user bot.
- Blocks are unique per pair and enforced bidirectionally by the API.
- Mutations compare a report revision, enforce the finite transition graph, and
  append an actor/time/status/note event. Closed reports are terminal and expire
  with their evidence after 180 days.

Audit focus: reporter/target authorization, idempotency races, moderator
allow-list bypass, service-secret confusion, stored content injection, and
blocked profile lookup.

## 7. Account deletion

The API creates or resumes a durable deletion journal, revokes all sessions
first, then removes live photos, link and Review codes, confirmations, blocks,
Apple identity, device sessions, and the user. Reports are anonymized and kept
only under moderation retention. Object cleanup is retried idempotently.

iOS advances its account generation and clears Keychain/account state, Met,
Saved, blocked IDs, encounter buffer, pending resolution, quick actions, caches,
badges, BLE work, and account-specific singleton state after a successful or
already-completed deletion response. The installation device ID may remain.

The operation is durable but still crosses standalone MongoDB and object
storage. Auditors must inject interruption at every step and exercise
reconciliation; see the candidate disposition for `R-003` in
[OPEN_RISKS.md](OPEN_RISKS.md).
