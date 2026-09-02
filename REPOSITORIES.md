# Repository Inventory and Pre-Release Baseline

**Inventory captured:** September 2, 2026 at 20:44:06 UTC

**Baseline state:** Published remotely; configured CI/CD verified

| Repository | Branch | Current HEAD | Working tree at capture |
| --- | --- | --- | --- |
| `Telescan-iOS` | `main` | `7e5a96b898f91f510703eaf03414c4b77abcd71f` | Clean |
| `Telescan-api` | `main` | `ca92c03be39a3006f43754c41cf23c809b8fd700` | Clean |
| `Telescan-bot-app` | `main` | `87a76179f552b7d73fd2778e98c59e6be1ec62bc` | Clean |
| `Telescan-admin-bot` | `main` | `cce205998e50f5528fc884949ed14d81d4d7af60` | Clean |
| `Telescan-nginx` | `main` | `4242bcd54eb79f205ef99afffc8f14436bd46260` | Clean |
| `Telescan-relay` | `main` | `dc9d38e3b17cffae661def499eeba14481e7260d` | Clean |
| `Telescan-db` | `main` | `94cac3380f014b55c8bbc6f26cab6407c53ae924` | Clean |
| `Telescan-monitoring` | `main` | `bc66e60a2fa6d1f96db1cde2e3a2888b5510c0aa` | Clean |
| `Telescan-info` | `main` | `59176141e495f26d47d86144af225d0026c71cda` | Clean |
| `Telescan-internal-docs` | `main` | `b1929466f3a1efe9f166050e072220ce82f61f12` | Clean |

All implementation repositories use the GitHub organization path
`https://github.com/hiTechTeam/<repository>.git`. The confidential audit package
is maintained separately at `https://github.com/hiTechTeam/Telescan-audit.git`
and is intentionally excluded from its own baseline manifest.

## Freeze rules

1. Treat the SHAs above as the source baseline for the first App Store release.
2. Any source change after this point requires a new relevant CI/CD run and an
   updated baseline before the signed Archive is accepted.
3. Record the final publishing-team signed build and immutable server image
   identifiers without rewriting Git history.
4. Never commit App Review codes, credentials, `.env` files, user data, or
   production logs containing private payloads.

## Baseline acceptance record

```text
Baseline frozen at (UTC): 2026-09-02T20:44:06Z
Approved by: PENDING RELEASE-OWNER SIGN-OFF
App version/build: 1.0 (2)
Production API source: ca92c03be39a3006f43754c41cf23c809b8fd700
All working trees clean: YES AT CAPTURE
All configured CI/CD runs green: YES — see evidence/CI_RUNS.md
Baseline manifest SHA-256: fc5818bb115237c3773d9f017e5ed81593318ae4f35ac159bd4bed94206a7dde
```
