# High-Value Source Map

Paths are relative to the named repository and must be resolved at the frozen
SHA. The list prioritizes security review entry points; it is not a complete
source inventory.

## Telescan-iOS

| Area | Entry points |
| --- | --- |
| Network/auth | `TelescaniOS/App/Services/NET/APIClient.swift`, `FetchService.swift`, `Services/Auth/AuthSessionStore.swift`, `AccountSessionGeneration.swift` |
| Registration/linking | `TelescaniOS/App/ViewModels/CodeVM.swift`, `Views/Screens/Registration/` |
| Session cleanup | `TelescaniOS/App/Views/Navigation/Coordinator/AppCoordinator.swift`, account generation and coordinator-owned profile/photo view models |
| BLE | `TelescaniOS/App/Services/BLE/BLEManager.swift`, `App/ViewModels/PeopleVM.swift` |
| Met/Saved storage | `TelescaniOS/App/Services/Storage/EncounterHistoryStore.swift`, `Views/Screens/People/SystemSwipeList.swift` |
| Reports/blocks/profile UI | `TelescaniOS/App/Views/Screens/People/`, `Views/Screens/Profile/`, `Views/Structures/ProfileOverview.swift` |
| Platform declarations | `TelescaniOS/Configuration/Info.plist`, `TelescaniOS/TelescaniOS.entitlements`, privacy manifests, localized permission strings |
| Tests | `TelescanTests/` |

## Telescan-api

| Area | Entry points |
| --- | --- |
| App/exception surface | `src/app.py` |
| Route authorization | `src/api/routers/`, `src/dependencies/auth.py`, internal/moderation dependencies |
| Authentication/session | `src/use_cases/auth.py`, `src/services/sessions.py`, session repositories |
| Codes/App Review | `src/services/codes.py`, link/review repositories, `scripts/review_codes.py` |
| Profile/photo/deletion | `src/use_cases/profiles.py`, `src/services/photos.py`, `src/services/account_deletions.py`, deletion repository, photo storage adapter |
| Identity adoption | `src/use_cases/auth.py`, `src/services/account_merges.py`, merge/link-code repositories and invariant migrations |
| Reports/blocks/evidence | Moderation use case/router/repository/schemas, `src/services/report_evidence.py`, MongoDB report events/evidence fields |
| Persistence contract | `src/infrastructure/mongodb/documents.py`, account-operation/link-code/moderation migration and invariant scripts |
| Runtime configuration | `src/core/config.py`, `.env.example`, `Dockerfile`, Compose |
| Deployment | `.github/workflows/deploy.yml` |
| Legal pages | Vendored `src/api/presentation/legal_documents.json`, `legal.py`, legal router/template, sync and deployment checkers |
| Tests | `tests/` |

## Telegram bots

- `Telescan-bot-app`: service API client, Telegram handlers, username/photo
  synchronization, confirmation recovery, runtime configuration, Docker/CI.
- `Telescan-admin-bot`: allow-list configuration, moderation API client, report
  rendering, status/note actions, runtime configuration, Docker/CI.

Neither bot should have MongoDB or photo-storage credentials.

## Infrastructure

| Repository | Review focus |
| --- | --- |
| `Telescan-nginx` | Moscow edge routes, origin binding, TLS/legal pages, internal/OpenAPI denial |
| `Telescan-relay` | EU TLS termination, WireGuard proxying, SSH/deploy boundary, certificate renewal |
| `Telescan-db` | MongoDB users/bindings, fail-closed compose validation, consistent backup, current-schema isolated restore and application-role proof |
| `Telescan-monitoring` | Restricted ingest, scrape/log transport, state freshness and capacity alerts, Grafana key migration, Telegram drill, production attestation |

## Documentation and public commitments

| Repository | Authoritative content |
| --- | --- |
| `Telescan-info` | Canonical localized legal JSON, generated Privacy Policy/Terms, manifest, security contact, product claims |
| `Telescan-internal-docs` | Architecture, production operations, security model, known risks, moderation, App Review runbook |
| `Telescan-audit` | Frozen baseline plus explicitly separated P0 remediation/evidence delta |

Any mismatch between this package and the frozen source must be corrected before
handoff or disclosed as documentation drift. Any mismatch between public
commitments and shipped behavior is a release-blocking finding.
