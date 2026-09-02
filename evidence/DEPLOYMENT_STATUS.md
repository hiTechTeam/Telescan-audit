# Production Deployment Status

**Observed (UTC):** 2026-09-02T20:31:00Z to 2026-09-02T20:34:00Z

**Result:** current server-component workflows completed successfully and the
deployed public/Moscow/EU/monitoring health checks below passed.

## Source-to-production mapping

| Component | Source SHA | Production evidence |
| --- | --- | --- |
| API | `ca92c03be39a3006f43754c41cf23c809b8fd700` | Workflow `33671211277` succeeded; public and loopback liveness/readiness returned 200/OK |
| User bot | `87a76179f552b7d73fd2778e98c59e6be1ec62bc` | Workflow `33641968109` succeeded; container healthy |
| Admin bot | `cce205998e50f5528fc884949ed14d81d4d7af60` | Workflow `33570880123` succeeded; container healthy |
| MongoDB | `94cac3380f014b55c8bbc6f26cab6407c53ae924` | Workflow `33570482988` succeeded; container healthy; backup timer active and latest service result successful |
| Moscow nginx | `4242bcd54eb79f205ef99afffc8f14436bd46260` | Workflow `33569059605` succeeded; container running; current release pointer present |
| EU relay | `dc9d38e3b17cffae661def499eeba14481e7260d` | Workflow `33568801105` succeeded; relay healthy; WireGuard origin check returned OK |
| Monitoring | `bc66e60a2fa6d1f96db1cde2e3a2888b5510c0aa` | Workflow `33569022579` succeeded; Grafana, Prometheus, and Loki healthy; Alloy running |
| Legal source | `59176141e495f26d47d86144af225d0026c71cda` | Both public origins served version `2026-09-01` and approved SHA-256 `f3bddc01a0013a89086044509ba85e1e63edc6bde7e45732a7e0c9803257045e` |

No failed systemd units were reported on the three checked hosts. Moscow and EU
certificate-renewal timers were active. The Moscow MongoDB backup timer was
active; its latest recorded service result was `success` with exit status 0.

## Distribution boundary

The iOS source is synchronized, its CI is green, and a clean unsigned Release
simulator build succeeded locally. No TestFlight or App Store binary is implied:
the repository intentionally has no distribution workflow, and the final
archive must be signed by the publishing company's Apple Developer team.

## Evidence limitation

This is a read-only smoke and workflow check. It does not replace a full
sanitized attestation of firewall, SSH, listener, image-digest, mount, secret,
restricted-ingest, and alert-delivery state, or a current-schema isolated
production-snapshot restore.
