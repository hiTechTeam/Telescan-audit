# Pre-Release CI/CD Runs

**Evidence captured (UTC):** 2026-09-02T20:44:06Z

**Result:** every configured workflow for the current pre-release SHA completed
successfully. GitHub links require authorized repository access where private.

| Repository | Frozen SHA | Workflow | Completed (UTC) | Result |
| --- | --- | --- | --- | --- |
| `Telescan-iOS` | `7e5a96b898f91f510703eaf03414c4b77abcd71f` | [iOS CI](https://github.com/hiTechTeam/Telescan-iOS/actions/runs/33678047504) | 2026-09-02T20:23:47Z | SUCCESS — XCTest, unsigned Release build, bundle validation |
| `Telescan-api` | `ca92c03be39a3006f43754c41cf23c809b8fd700` | [Deploy Telescan API](https://github.com/hiTechTeam/Telescan-api/actions/runs/33671211277) | 2026-09-02T19:10:02Z | SUCCESS — validate, backup, migrations, rollout, health gate |
| `Telescan-bot-app` | `87a76179f552b7d73fd2778e98c59e6be1ec62bc` | [Deploy Telescan Bot](https://github.com/hiTechTeam/Telescan-bot-app/actions/runs/33641968109) | 2026-09-02T14:28:51Z | SUCCESS — validate, image, rollout, health gate |
| `Telescan-admin-bot` | `cce205998e50f5528fc884949ed14d81d4d7af60` | [Deploy Telescan Admin Bot](https://github.com/hiTechTeam/Telescan-admin-bot/actions/runs/33570880123) | 2026-09-01T23:28:31Z | SUCCESS — validate, image, rollout, health gate |
| `Telescan-db` | `94cac3380f014b55c8bbc6f26cab6407c53ae924` | [Deploy Telescan MongoDB](https://github.com/hiTechTeam/Telescan-db/actions/runs/33570482988) | 2026-09-01T23:20:36Z | SUCCESS — validation, durable rollout, database health |
| `Telescan-nginx` | `4242bcd54eb79f205ef99afffc8f14436bd46260` | [Deploy Telescan Nginx](https://github.com/hiTechTeam/Telescan-nginx/actions/runs/33569059605) | 2026-09-01T23:02:17Z | SUCCESS — transaction fixtures, deployment, route checks |
| `Telescan-relay` | `dc9d38e3b17cffae661def499eeba14481e7260d` | [Validate and deploy EU relay](https://github.com/hiTechTeam/Telescan-relay/actions/runs/33568801105) | 2026-09-01T22:59:08Z | SUCCESS — validation, deployment, end-to-end health |
| `Telescan-monitoring` | `bc66e60a2fa6d1f96db1cde2e3a2888b5510c0aa` | [Monitoring stack](https://github.com/hiTechTeam/Telescan-monitoring/actions/runs/33569022579) | 2026-09-01T23:06:47Z | SUCCESS — rules/config validation, deployment, readiness |
| `Telescan-info` | `59176141e495f26d47d86144af225d0026c71cda` | [Validate legal source](https://github.com/hiTechTeam/Telescan-info/actions/runs/33562511667) | 2026-09-01T21:42:32Z | SUCCESS — canonical legal generation check |

`Telescan-internal-docs` at
`b1929466f3a1efe9f166050e072220ce82f61f12` has no GitHub Actions workflow;
its clean local `main` and `origin/main` were compared after publication.

The audit package uses its deterministic package checker and SHA-256 manifest.
