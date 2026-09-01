# Deployment and Operations Review

## Production request path

```text
iOS -> api.tgtelescan.ru:443 -> EU nginx TLS relay
    -> WireGuard -> Moscow nginx origin
    -> private Docker network -> Telescan API
    -> MongoDB / photo storage / internal bot callback
```

The EU relay is a trusted TLS termination point and an availability dependency.
The Moscow API and MongoDB ports are intended to be published only on loopback.
The WireGuard origin listener is restricted to the EU peer. Moscow nginx also
serves the main-domain legal pages and a documented direct-origin recovery path;
DNS and firewall policy must keep that path distinct from normal API routing.

## Release flow

1. CI verifies formatting, types, tests, container build/configuration, and
   repository-specific policy.
2. A serialized production workflow creates and validates an encrypted
   off-host database backup.
3. The current API container/image identity is captured.
4. The new API image is built while the old service remains available.
5. Migrations run in dry-run mode.
6. The API is stopped for apply-mode migrations.
7. The new service starts and must become Docker-healthy.
8. On migration/startup/readiness failure, the workflow retags and force
   recreates the previous image.

Rollback restores application code, not database state. Every deployed
migration must therefore be idempotent and backward compatible with the prior
application image.

## Secret classes

- JWT signing secret.
- Normal and Review link-code HMAC secrets.
- User-bot and moderation service credentials.
- Telegram bot tokens.
- MongoDB application/root credentials.
- Photo-storage credentials.
- TLS, SSH, WireGuard, Restic, GitHub environment, monitoring, and alerting
  credentials.

Production startup rejects development-prefixed application secrets, duplicated
application secret values, and wildcard/empty CORS configuration. This check is
not a substitute for external secret rotation and access-control review.

## Auditor deployment checks

- Enumerate every public IPv4/IPv6 listener from outside and on each host.
- Confirm direct-origin and alternate-host behavior matches documentation.
- Verify internal/schema routes return `404` through every public edge.
- Inspect TLS versions, certificate renewal, HSTS, proxy headers, request limits,
  timeout behavior, and upstream identity.
- Confirm containers are unprivileged/read-only where documented, drop
  capabilities, set `no-new-privileges`, and use bounded writable mounts/tmpfs.
- Confirm `.env`, Git metadata, tests, caches, and private material are excluded
  from image contexts and layers.
- Validate that migration and health-check failures actually restore the prior
  image.
- Verify alerting for edge/origin/API/database/backup/telemetry failure.
- Perform restore only into an isolated MongoDB instance before any production
  recovery decision.

## Production testing restriction

This package does not authorize production penetration testing. Any production
test requires a written change record specifying auditor source IPs, endpoints,
time window, request ceiling, data restrictions, monitoring contacts, rollback,
and stop conditions.

## Verification limitation

The package describes source-controlled topology and workflows. It does not by
itself prove the current production firewall, DNS, secrets, images, or host
state. Those require a dated operational evidence capture at handoff.

