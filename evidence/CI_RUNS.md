# Frozen Baseline CI/CD Runs

**Evidence captured (UTC):** 2026-09-01T09:39:49Z  
**Result:** every configured workflow for the frozen baseline completed
successfully. GitHub links require authorized repository access.

## Application repositories

| Repository | Frozen SHA | Workflow | Completed (UTC) | Result |
| --- | --- | --- | --- | --- |
| `Telescan-iOS` | `316a68095d7caa959abe8c65bf6431a023c11d3c` | [iOS CI](https://github.com/hiTechTeam/Telescan-iOS/actions/runs/33492223348) | 2026-09-01T09:38:47Z | SUCCESS — XCTest, Release build, and bundle validation |
| `Telescan-api` | `8eebf456ee16a49832cd71116e6ff8d6fe7a954d` | [Deploy Telescan API](https://github.com/hiTechTeam/Telescan-api/actions/runs/33492210275) | 2026-09-01T09:29:08Z | SUCCESS — lint, types, tests, image build, backup, migration, deploy, health gate |
| `Telescan-bot-app` | `816deb82c91488044b3372fc35708d95310e60e4` | [Deploy Telescan Bot](https://github.com/hiTechTeam/Telescan-bot-app/actions/runs/33492207198) | 2026-09-01T09:28:13Z | SUCCESS — lint, types, tests, image build, deploy, health gate |
| `Telescan-admin-bot` | `9b9cdbeab7b3542fb0f82c0afd4d03f041102456` | [Deploy Telescan Admin Bot](https://github.com/hiTechTeam/Telescan-admin-bot/actions/runs/33492207083) | 2026-09-01T09:28:12Z | SUCCESS — lint, types, tests, image build, deploy, health gate |

## Infrastructure repositories

These repositories were already synchronized and unchanged during the
September 1 baseline publication. Their exact frozen SHAs already had green
validation and production deployment runs.

| Repository | Frozen SHA | Workflow | Completed (UTC) | Result |
| --- | --- | --- | --- | --- |
| `Telescan-nginx` | `b29c523edeec1009c925f8162b953441c3c210d7` | [Deploy Telescan Nginx](https://github.com/hiTechTeam/Telescan-nginx/actions/runs/32725603431) | 2026-08-24T12:10:21Z | SUCCESS |
| `Telescan-relay` | `730c271bfc4f7aaed08f244baaf5a0fc58bf801b` | [Validate and deploy EU relay](https://github.com/hiTechTeam/Telescan-relay/actions/runs/32725602533) | 2026-08-24T12:10:19Z | SUCCESS |
| `Telescan-db` | `3194ba786436cdb5a266c40ae84971cd01b60e7e` | [Deploy Telescan MongoDB](https://github.com/hiTechTeam/Telescan-db/actions/runs/32726766081) | 2026-08-24T12:23:08Z | SUCCESS |
| `Telescan-monitoring` | `07b6c6b00218e420d09201e0c4219f12790586a3` | [Monitoring stack](https://github.com/hiTechTeam/Telescan-monitoring/actions/runs/32239623432) | 2026-08-19T09:50:28Z | SUCCESS |

## Repositories without GitHub Actions

`Telescan-info` at `bc92242f5b7bff907dd2453fb78ee42b73522212`
and `Telescan-internal-docs` at
`c05fb982319e9462c4bed7c00f657e4b5cb2042c` do not define GitHub Actions
workflows. Their local `main` branches and `origin/main` were compared after
publication and matched exactly.

The audit package is published privately at
`https://github.com/hiTechTeam/Telescan-audit`. Its deterministic local package
checker and integrity manifest are the applicable validation controls.
