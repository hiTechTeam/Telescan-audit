# Repository Inventory and Baseline

**Inventory captured:** September 1, 2026 at 09:39:49 UTC

**Baseline state:** Published remotely; configured CI/CD verified

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
| `Telescan-info` | `main` | `bc92242f5b7bff907dd2453fb78ee42b73522212` | Clean |
| `Telescan-internal-docs` | `main` | `c05fb982319e9462c4bed7c00f657e4b5cb2042c` | Clean |

## Canonical remotes

All implementation repositories currently use the private/public GitHub
organization path `https://github.com/hiTechTeam/<repository>.git`. Auditors
must receive read-only access only to the repositories listed in the signed
scope.

The confidential audit package is published separately at
`https://github.com/hiTechTeam/Telescan-audit.git`. Its repository is private
and must not be made public because it contains internal architecture, threat,
and operational context.

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
Baseline frozen at (UTC): 2026-09-01T09:39:49Z
Approved by: PENDING RELEASE-OWNER SIGN-OFF
App version/build: 1.0 (2)
Production API release: 8eebf456ee16a49832cd71116e6ff8d6fe7a954d (run 33492210275)
All working trees clean: YES AT CAPTURE
All configured CI/CD runs green: YES — see evidence/CI_RUNS.md
Snapshot manifest SHA-256: d6318ec0c8836f4bd7f82462c27df8ac5fc99b176300969e05a5f81cd0414660
```
