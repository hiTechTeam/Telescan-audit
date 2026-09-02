# Telescan Pre-Release Baseline

**Captured (UTC):** 2026-09-02T20:44:06Z

**Workspace:** local operator checkout

**Remote verification:** every listed local `main` matched `origin/main` at
capture

| Repository | Branch | Commit SHA | Tree | Remote |
| --- | --- | --- | --- | --- |
| `Telescan-iOS` | `main` | `7e5a96b898f91f510703eaf03414c4b77abcd71f` | CLEAN | `https://github.com/hiTechTeam/Telescan-iOS.git` |
| `Telescan-api` | `main` | `ca92c03be39a3006f43754c41cf23c809b8fd700` | CLEAN | `https://github.com/hiTechTeam/Telescan-api.git` |
| `Telescan-bot-app` | `main` | `87a76179f552b7d73fd2778e98c59e6be1ec62bc` | CLEAN | `https://github.com/hiTechTeam/Telescan-bot-app.git` |
| `Telescan-admin-bot` | `main` | `cce205998e50f5528fc884949ed14d81d4d7af60` | CLEAN | `https://github.com/hiTechTeam/Telescan-admin-bot.git` |
| `Telescan-nginx` | `main` | `4242bcd54eb79f205ef99afffc8f14436bd46260` | CLEAN | `https://github.com/hiTechTeam/Telescan-nginx.git` |
| `Telescan-relay` | `main` | `dc9d38e3b17cffae661def499eeba14481e7260d` | CLEAN | `https://github.com/hiTechTeam/Telescan-relay.git` |
| `Telescan-db` | `main` | `94cac3380f014b55c8bbc6f26cab6407c53ae924` | CLEAN | `https://github.com/hiTechTeam/Telescan-db.git` |
| `Telescan-monitoring` | `main` | `bc66e60a2fa6d1f96db1cde2e3a2888b5510c0aa` | CLEAN | `https://github.com/hiTechTeam/Telescan-monitoring.git` |
| `Telescan-info` | `main` | `59176141e495f26d47d86144af225d0026c71cda` | CLEAN | `https://github.com/hiTechTeam/Telescan-info.git` |
| `Telescan-internal-docs` | `main` | `b1929466f3a1efe9f166050e072220ce82f61f12` | CLEAN | `https://github.com/hiTechTeam/Telescan-internal-docs.git` |

**Baseline result:** VALID — every listed repository was present, clean,
synchronized with its authorized remote, and checked after `git fetch --prune`.

Configured CI/CD results for these exact SHAs are recorded in
[CI_RUNS.md](CI_RUNS.md). `Telescan-internal-docs` has no GitHub Actions
workflow; its remote SHA was verified directly. The audit package itself is
excluded to avoid a self-referential manifest.
