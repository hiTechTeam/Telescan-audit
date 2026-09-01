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
3. The API issues a random eight-character code and stores only its HMAC digest.
4. Authenticated iOS submits the clear code to
   `/api/v1/users/me/telegram/link`.
5. The API atomically consumes the code and links or adopts the Telegram
   profile into the Apple-authenticated account.
6. The API returns a replacement access token for the existing device session;
   the code itself never creates a session.

Audit focus: one-time atomicity, enumeration, HMAC separation, rate limiting,
identity-adoption partial failure, public-username validation, and code leakage.

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
5. Unresolved, blocked, incomplete, or inaccessible profiles are not displayed.
6. RSSI and distance are processed locally.
7. A resolved profile leaving Nearby enters a persistent heartbeat buffer and
   then the local 24-hour Met list.
8. Explicitly Saved profiles persist only on that device.

Audit focus: replay/correlation, malformed GATT values, restoration state,
resource exhaustion, blocked-cache behavior, and cross-account local-state
cleanup. A cap remains only for unresolved BLE identifiers; resolved profile
history and its resolved transition buffer are not capped at 500.

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

- A report uses a client request UUID for idempotency and a universal
  user-facing reason.
- The API captures limited target-profile context so later profile edits do not
  erase the moderation record.
- Internal storage retains the universal `other` enum for schema compatibility.
- The admin bot is Telegram-ID allow-listed and uses a credential distinct from
  the user bot.
- Blocks are unique per pair and enforced bidirectionally by the API.

Audit focus: reporter/target authorization, idempotency races, moderator
allow-list bypass, service-secret confusion, stored content injection, and
blocked profile lookup.

## 7. Account deletion

The API revokes all sessions first, then removes photos, link and Review codes,
confirmations, blocks, Apple identity, device sessions, and the user. Reports
are anonymized and retained only under their moderation retention policy. iOS
clears Keychain/account state, Met, Saved, caches, and in-memory singleton state
after a successful or already-completed deletion response.

This is a multi-resource operation on standalone MongoDB and object storage; it
is not fully transactional. The residual failure/retry risk is disclosed in
[OPEN_RISKS.md](OPEN_RISKS.md).

