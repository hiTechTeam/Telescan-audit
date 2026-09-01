# Repository Inventory and Baseline

**Inventory captured:** September 1, 2026 at 09:11:44 UTC  
**Baseline state:** Frozen locally; remote/CI verification pending

## Current inventory

| Repository | Branch | Current HEAD | Working tree at capture |
| --- | --- | --- | --- |
| `Telescan-iOS` | `main` | `316a68095d7caa959abe8c65bf6431a023c11d3c` | Clean |
| `Telescan-api` | `main` | `8eebf456ee16a49832cd71116e6ff8d6fe7a954d` | Clean |
| `Telescan-bot-app` | `main` | `816deb82c91488044b3372fc35708d95310e60e4` | Clean |
| `Telescan-admin-bot` | `main` | `9b9cdbeab7b3542fb0f82c0afd4d03f041102456` | Clean |
| `Telescan-nginx` | `main` | `b29c523edeec1009c925f8162b953441c3c210d7` | Clean |
| `Telescan-relay` | `main` | `730c271bfc4f7aaed08f244baaf5a0fc58bf801b` | Clean |
| `Telescan-db` | `main` | `3194ba786436cdb5a266c40ae84971cd01b60e7e` | Clean |
| `Telescan-monitoring` | `main` | `07b6c6b00218e420d09201e0c4219f12790586a3` | Clean |
| `Telescan-info` | `main` | `986ce607d38be2e71c3d28989decb681feb74bd3` | Clean |
| `Telescan-internal-docs` | `main` | `c05fb982319e9462c4bed7c00f657e4b5cb2042c` | Clean |

## Canonical remotes

All implementation repositories currently use the private/public GitHub
organization path `https://github.com/hiTechTeam/<repository>.git`. Auditors
must receive read-only access only to the repositories listed in the signed
scope.

## Freeze procedure

1. Review and commit every intended audit-readiness change in each repository.
2. Confirm `git status --porcelain=v1` is empty everywhere.
3. Run `scripts/collect_snapshot.sh` from this package.
4. Replace the provisional inventory with the generated SHAs.
5. Confirm CI is green for every frozen commit.
6. Prefer signed, annotated tags such as `audit-2026-09-01` where repository
   policy permits them.
7. Record the App Store build number and API/container release identifiers that
   correspond to the frozen source.
8. Share later fixes as separate commits; never rewrite the original audit
   baseline.

## Baseline acceptance record

Complete this block immediately before external handoff:

```text
Baseline frozen at (UTC): 2026-09-01T09:11:44Z
Approved by: PENDING RELEASE-OWNER SIGN-OFF
App version/build: 1.0 (2)
Production API release: PENDING
All working trees clean: YES AT CAPTURE
All required CI runs green: PENDING
Snapshot manifest SHA-256: 87eb5936d3dce8826b0a783016d9c4691f9e601d7f9ce785df942e06d36fe98f
```
