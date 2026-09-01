# High-Value Source Map

Paths are relative to the named repository and must be resolved at the frozen
SHA. The list prioritizes security review entry points; it is not a complete
source inventory.

## Telescan-iOS

| Area | Entry points |
| --- | --- |
| Network/auth | `TelescaniOS/App/Services/NET/APIClient.swift`, `FetchService.swift`, session storage under `Services/Storage` |
| Registration/linking | `TelescaniOS/App/ViewModels/CodeVM.swift`, `Views/Screens/Registration/` |
| Session cleanup | `TelescaniOS/App/Views/Navigation/Coordinator/AppCoordinator.swift` |
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
| Profile/photo/deletion | `src/use_cases/profiles.py`, `src/services/photos.py`, photo storage adapter |
| Reports/blocks | Moderation use cases/repositories and schemas |
| Persistence contract | `src/infrastructure/mongodb/documents.py`, migration scripts |
| Runtime configuration | `src/core/config.py`, `.env.example`, `Dockerfile`, Compose |
| Deployment | `.github/workflows/deploy.yml` |
| Legal pages | `src/api/presentation/legal.py`, legal router/static assets |
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
| `Telescan-db` | MongoDB users/bindings, backup encryption, off-host retention, restore drill |
| `Telescan-monitoring` | Compose pins, scrape/log transport, alerts, Grafana access, Telegram egress |

## Documentation and public commitments

| Repository | Authoritative content |
| --- | --- |
| `Telescan-info` | Public Privacy Policy, Terms, security contact, product claims |
| `Telescan-internal-docs` | Architecture, production operations, security model, known risks, moderation, App Review runbook |

Any mismatch between this package and the frozen source must be corrected before
handoff or disclosed as documentation drift. Any mismatch between public
commitments and shipped behavior is a release-blocking finding.

