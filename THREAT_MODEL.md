# Threat Model

## Protected assets

- Apple subjects and account-to-Telegram identity bindings.
- Access tokens, refresh tokens, device sessions, and installation IDs.
- Telegram bot tokens and API service credentials.
- JWT, normal-link-code, and Review-code HMAC secrets.
- MongoDB application/root credentials and stored account/moderation data.
- Photo-storage credentials and objects.
- SSH, WireGuard, TLS, Restic, GitHub, monitoring, and deployment credentials.
- Availability and integrity of the API, bot, BLE experience, moderation, and
  deletion workflows.
- Privacy commitments concerning GPS, BLE measurements, Met, and Saved data.

## Adversaries

- Unauthenticated internet attacker.
- Authenticated malicious Telescan user.
- Nearby radio observer or BLE replay device.
- User with physical access to an unlocked or compromised iPhone.
- Compromised Telegram user/bot/admin account.
- Compromised CI runner, operator workstation, relay, origin, or monitoring
  host.
- Malicious or compromised dependency/build input.
- Well-intentioned operator making a dangerous deployment or recovery mistake.

## Primary entry points

- Public authentication, refresh, legal, and health endpoints.
- Authenticated profile, photo, report, block, and account endpoints.
- Internal bot and moderation routes.
- BLE advertisements, reads, writes, callbacks, and restoration state.
- Telegram bot messages and callbacks.
- Image uploads and public photo URLs.
- CI/CD workflows, SSH, Docker daemon, nginx, WireGuard, DNS, TLS renewal,
  backups, restore tools, logs, and alert delivery.

## Threat/control matrix

| Threat | Existing control | Residual concern / audit test |
| --- | --- | --- |
| Link-code guessing or replay | Eight-character random code, keyed digest, TTL, rate limits, atomic consume | Entropy assumptions, distributed attempts, race tests, log leakage |
| Review-code leakage | Separate HMAC secret/collection, scoped profile, one-time consume, revocation | Operator handling and App Store Connect exposure |
| Refresh-token theft/reuse | Keychain storage, server digest, rotation, active-session check, reuse revocation | Concurrent refresh and device restore behavior |
| JWT accepted after logout | Active session and Apple identity checked per request | Cache windows, middleware coverage, clock skew |
| Cross-account identity adoption | Conflict checks and explicit Apple identity move | Multi-resource partial failure is not transactional |
| IDOR/profile enumeration | Authenticated lookup, random UUID, block checks | Known UUID remains queryable without proof of proximity |
| BLE impersonation/correlation | Random Telescan ID, authenticated profile resolution | Stable radio identifier is replayable/correlatable by design |
| Block bypass | Server-side bidirectional relationship check | Race and offline-cache consistency |
| Duplicate/mutated reports | Client request UUID and unique index; captured snapshot | Abuse, content rendering, retention lifecycle |
| Moderator compromise | Explicit Telegram allow-list and separate service secret | Telegram account takeover; no granular roles/case assignment |
| Photo dangling reference | Upload, DB commit, old-object cleanup; compensation on DB failure | Cleanup retry and object-prefix authorization |
| Internal-route exposure | Public nginx `404`, loopback/private networks, distinct secrets | Alternate hosts, direct origin, IPv6, proxy normalization |
| Database exposure | Loopback publication, dedicated app account, private Docker network | Host compromise and backup credential handling |
| Supply-chain substitution | Lockfiles and CI checks | Base images and uv installer are not digest/checksum pinned |
| Secret leakage in build/image | `.dockerignore`, environment secrets, runtime validation | CI logs, image layers, artifacts, operator commands |
| Data retained after deletion | Session-first deletion and collection cleanup | No durable cross-resource deletion job/transaction |
| Local cross-account leakage | Session cleanup clears Met/Saved and in-memory state | Backup/restore and compromised-device exposure |
| Deployment outage | Serialized deploy, health checks, previous-image rollback | Database migrations must remain backward compatible |

## Required test hypotheses

Auditors should explicitly attempt to disprove these statements:

1. A code can be consumed no more than once under concurrent requests.
2. A Review code cannot be validated with the normal-code HMAC secret.
3. A Telegram code cannot create a primary session without Apple authentication.
4. Revoked, deleted, expired, or refresh-reuse sessions cannot call any protected
   route.
5. A blocked user cannot retrieve the blocker in either direction.
6. Bot and moderation credentials cannot be substituted for each other.
7. Internal and schema endpoints remain inaccessible through every public host,
   encoding variant, method, and proxy-normalization path.
8. Photo replacement never leaves a live database URL pointing to an object
   intentionally deleted before commit.
9. Sign-out/deletion cannot expose a prior account's Saved or Met profiles to
   the next account in the same process.
10. Shipped collection/retention behavior matches the public Privacy Policy.

