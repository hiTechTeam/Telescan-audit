# API Surface Inventory

The frozen OpenAPI document and nginx routing configuration are authoritative.
This inventory is a review map and must be regenerated/compared at baseline.

## Public and bootstrap routes

| Method | Path | Authority / exposure |
| --- | --- | --- |
| `GET` | `/privacy` | Public legal page; canonical version and SHA-256 headers; not in OpenAPI |
| `GET` | `/terms` | Public legal page; canonical version and SHA-256 headers; not in OpenAPI |
| `GET` | `/health/live` | Process liveness; edge exposure depends on nginx policy |
| `GET` | `/health/ready` | Database-aware readiness; edge exposure depends on nginx policy |
| `POST` | `/api/v1/auth/apple` | Public with Apple identity token, nonce, and installation device ID |
| `POST` | `/api/v1/auth/refresh` | Public with rotating refresh token |
| `POST` | `/api/v1/auth/link` | Legacy non-production migration-test path; `404` when disabled and forbidden by production startup |

## Active device-session routes

All routes below require an access JWT, active non-revoked device session, and
attached Apple identity.

| Method | Path | Purpose |
| --- | --- | --- |
| `DELETE` | `/api/v1/auth/session` | Revoke current session |
| `POST` | `/api/v1/auth/logout-all/request` | Retained confirmation contract |
| `GET` | `/api/v1/auth/logout-all/requests/{confirmation_id}` | Confirmation status |
| `GET` | `/api/v1/users/me` | Current profile/session validation |
| `PATCH` | `/api/v1/users/me` | Update BIO |
| `DELETE` | `/api/v1/users/me` | Delete account |
| `POST` | `/api/v1/users/me/telegram/link` | Consume normal or Review link code |
| `PUT` | `/api/v1/users/me/photo` | Replace photo |
| `DELETE` | `/api/v1/users/me/photo` | Remove photo |
| `GET` | `/api/v1/profiles/{telescan_id}` | Resolve accessible shared profile |
| `POST` | `/api/v1/reports` | Submit idempotent universal report with optional 0–500 comment |
| `GET` | `/api/v1/users/me/blocks` | List blocks |
| `PUT` | `/api/v1/users/me/blocks/{target_telescan_id}` | Block profile |
| `DELETE` | `/api/v1/users/me/blocks/{target_telescan_id}` | Unblock profile |

## User-bot internal routes

Every route requires `BOT_SERVICE_SECRET` and must be denied at public edges.

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/internal/v1/link-codes` | Upsert Telegram profile/photo state and issue normal code |
| `PUT` | `/internal/v1/confirmations/{confirmation_id}/message` | Associate Telegram message metadata |
| `GET` | `/internal/v1/confirmations/pending` | Recover pending confirmations after bot restart |
| `POST` | `/internal/v1/confirmations/{confirmation_id}/decision` | Submit Telegram confirmation decision |

## Moderation internal routes

Every route requires the separate `MODERATION_SERVICE_SECRET` and must be
denied at public edges.

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/internal/v1/moderation/reports` | List queue, optional status and bounded limit |
| `GET` | `/internal/v1/moderation/reports/{report_id}` | Read one report |
| `PATCH` | `/internal/v1/moderation/reports/{report_id}` | Revision-CAS status/note mutation; closed states terminal |

## OpenAPI and static routes

FastAPI keeps `/openapi.json`, `/docs`, and `/redoc` for loopback/admin use.
Both public nginx edges must return `404` for them and all `/internal/` paths.
The API also mounts application-owned static legal assets under `/public`.

## Current rate-limit map

| Scope | Limit |
| --- | --- |
| Legacy link by IP | 30 per 5 minutes in non-production migration testing only |
| Legacy link by device | 10 per 5 minutes in non-production migration testing only |
| Apple sign-in by IP | 30 per 5 minutes |
| Apple sign-in by device | 10 per 5 minutes |
| Refresh by IP | 60 per minute |
| Refresh by token digest | 30 per minute |
| Authenticated Telegram/Review linking | 10 per user per 5 minutes |
| Public-profile resolution | 120 per user per minute |
| BIO update | 20 per user per hour |
| Photo replacement | 10 per user per hour |
| Report submission | 10 per user per hour |
| Block creation | 60 per user per hour |
| Bot code issuance | 6 per Telegram ID per 5 minutes |

The absence of an explicit endpoint-specific limit does not remove the need for
global proxy/body/time limits and authenticated authorization. Auditors should
test distributed attempts, IPv6/proxy identity, key cardinality, TTL cleanup,
and resource-exhaustion paths.

## Contract checks

- Compare this table with the frozen OpenAPI paths and router source.
- Verify every protected route applies the intended dependency after router
  inclusion and middleware composition.
- Verify user-bot and moderation secrets cannot authorize each other's routes.
- Test path encoding, duplicate slashes, case, query ambiguity, alternate
  methods, and forwarded headers through both public edges.
- Confirm legacy routes remain disabled in the audited production state.
