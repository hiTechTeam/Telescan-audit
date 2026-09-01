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

1. CI verifies formatting, types, tests, container/configuration semantics, and
   repository-specific policy.
2. A production job rejects any revision other than `main` and acquires its
   GitHub environment lock.
3. Every repository mutating a shared host also acquires the same bounded
   `/tmp/telescan-production-deploy.lock`; repository-level concurrency alone
   cannot serialize different repositories.
4. Preflight validates target identity, required files, configuration and the
   current healthy service. A complete immutable release, recovery controller,
   systemd watcher state, old/new image identities, and an fsynced transaction
   intent are durable before runtime mutation; activation uses an atomic
   `current` pointer.
5. The database workflow creates and validates a consistent encrypted off-host
   backup; API migrations run in dry-run before apply mode.
6. API deployment closes its owner-scoped ingress gate before migration. The
   candidate must pass local health, invariants, legal and exact singleton
   topology before a durable candidate commit and ingress reopen. Other
   services pass their repository-specific semantic readiness gates.
7. On interruption, reboot, migration, startup, or pre-commit readiness
   failure, boot/online recovery restores and verifies the prior immutable
   release and image. Injected child and outer-session termination fixtures
   exercise this boundary.
8. API public-origin verification runs after reopen. Failure closes ingress
   again and requires operator recovery; it does not start an incompatible old
   image against data already touched by the candidate.

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

Production startup rejects empty/default/placeholder credentials, duplicated or
cross-role application secrets, wildcard/invalid CORS origins, legacy
authentication, an administrative application database, and unexpected
storage/database routing. An empty CORS allow-list is valid and preferred for a
native-only client. These checks do not replace external secret rotation or
access-control review.

## P0 monitoring rollout boundary

The restricted ingest gateway, mandatory host-state freshness, and Grafana
secret-key transition are staged migrations. Run the repository runbooks in
order, keep the legacy ingest path available until every agent is proven on the
write-only path, then bind full Prometheus/Loki APIs to loopback. Rehearse and
back up Grafana data before changing its encryption key. P0 acceptance requires
observed Telegram firing and resolved messages and a passing fail-closed
attestation from all three host roles.

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
- Confirm restricted ingest rejects query/admin/read methods while authorized
  remote-write/push traffic succeeds; require fresh host-state series.
- Reconcile DNS, TLS hostname verification, listeners, firewall, WireGuard, SSH
  effective policy, mounted data filesystems, timers, Docker published ports,
  and running image digests with dated sanitized attestation output.
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
