# Build, Test, and Evidence Guide

## Baseline rules

- Run checks from a clean checkout at the frozen SHA.
- Use example configuration only; never copy production `.env` files into an
  auditor workstation.
- Record tool versions, command exit status, UTC timestamp, and commit SHA.
- Store sanitized logs under `evidence/`; do not store tokens, credentials, user
  data, or clear Review codes.

## API

Prerequisites: Python 3.13, `uv`, Docker with Compose.

```sh
cd Telescan-api
uv sync --frozen
uvx --from ruff==0.16.3 ruff check .
uvx --from ruff==0.16.3 ruff format --check .
uvx --from pyright==1.1.411 pyright
uv run pytest
uv lock --check
docker compose config --quiet
```

The production Dockerfile installs `--no-dev`; CI installs the development
group for tests.

## User bot

```sh
cd Telescan-bot-app
uv sync --frozen
uvx --from ruff==0.16.3 ruff check .
uvx --from ruff==0.16.3 ruff format --check .
uvx --from pyright==1.1.411 pyright
uv run pytest
uv lock --check
docker compose config --quiet
```

## Admin bot

```sh
cd Telescan-admin-bot
uv sync --frozen
uvx --from ruff==0.16.3 ruff check .
uvx --from ruff==0.16.3 ruff format --check .
uvx --from pyright==1.1.411 pyright
uv run pytest
docker compose config --quiet
```

One admin-bot test binds a temporary localhost port. A restricted test runner
must explicitly permit loopback binding.

## Infrastructure repositories

At minimum, validate Compose rendering in `Telescan-nginx`, `Telescan-relay`,
`Telescan-db`, and `Telescan-monitoring` using their documented example
configuration. Review every rendered public port, volume, capability, network,
health check, and secret mount.

Additional required checks:

- nginx configuration syntax and public denial of `/internal/`, `/docs`,
  `/redoc`, and `/openapi.json`;
- WireGuard listener bindings and peer restrictions;
- encrypted backup integrity and an isolated restore drill;
- monitoring rules, missing-telemetry alerts, and restricted alert egress;
- deployment workflow shell/YAML syntax and rollback behavior.

## iOS

Prerequisites: supported macOS/Xcode, iOS Simulator runtime, Swift Package
dependencies resolved from the lockfile.

```sh
cd Telescan-iOS

xcodebuild build-for-testing \
  -project TelescaniOS.xcodeproj \
  -scheme Telescan \
  -configuration Debug \
  -destination 'generic/platform=iOS Simulator' \
  CODE_SIGNING_ALLOWED=NO

xcodebuild test \
  -project TelescaniOS.xcodeproj \
  -scheme Telescan \
  -destination 'platform=iOS Simulator,name=iPhone 16'

xcodebuild build \
  -project TelescaniOS.xcodeproj \
  -scheme Telescan \
  -configuration Release \
  -destination 'generic/platform=iOS Simulator' \
  CODE_SIGNING_ALLOWED=NO
```

Also verify:

- Release entitlements and Sign in with Apple;
- privacy manifests and Bluetooth/photo/camera permission strings;
- English/Russian localization-key parity;
- no local configuration or repository metadata in the `.app` bundle;
- physical-device BLE discovery on two iPhones;
- iOS 18 and iOS 26 behavior for navigation bars, swipe actions, context menus,
  background restoration, badges, and local-state cleanup.

## Current pre-release evidence

The following checks were completed against the September 2 pre-release
baseline. Exact remote runs are linked from `evidence/CI_RUNS.md`:

| Check | Result |
| --- | --- |
| API pytest | 157 passed |
| API Ruff/Pyright | Passed; zero type errors |
| User-bot pytest | 44 passed |
| User-bot Ruff/Pyright | Passed |
| Admin-bot pytest | 41 passed |
| Admin-bot Ruff/Pyright | Passed |
| API/user-bot uv lock checks | Passed |
| API/user-bot Compose rendering | Passed |
| iOS unsigned Release simulator build | Passed |
| iOS remote XCTest on Xcode 26.3 | Passed |
| iOS remote Release build and bundle validation | Passed |
| MongoDB validator/deployment fixtures | 10 Python tests plus Node and shell fixtures passed |
| nginx/relay immutable transaction fixtures | Passed |
| Monitoring safety, attestation-negative, and transaction fixtures | Passed |
| Canonical legal generation and two-origin digest check | Passed |
| Repository whitespace/error check | `git diff --check` passed |

The local full XCTest launch reached `Testing started` but the local Xcode
runner stalled at `waiting for workers to materialize` and was interrupted
after 270 seconds. The clean GitHub Actions run for the same iOS SHA completed
XCTest successfully. The current workflow retains logs but does not
upload the `.xcresult`; retain that artifact in a future audit-specific run if
the auditor requires bundle-level test evidence.

## Minimum dynamic test set

- Concurrent normal-code and Review-code consumption.
- Refresh rotation and reuse from two devices.
- Apple/Telegram identity conflict and adoption interruption.
- Exact consumed-proof binding, repeated completed merge, and one-active-code
  concurrency.
- Bidirectional blocked-profile lookup.
- Duplicate report requests with the same idempotency UUID.
- Report evidence copy/retry/cleanup, moderation transition/CAS races, and
  missing/null/string note semantics.
- Photo upload failure before and after database commit.
- Account-deletion retry after each resource boundary.
- Public-path normalization and internal-route denial at EU and Moscow edges.
- BLE malformed identity, replay, background restoration, and cross-account
  local-state cleanup.
- Raw/unresolved BLE notification suppression and late A-to-B callback/refresh
  rejection.
- Current-schema encrypted restore with journal/evidence indexes, domain
  references, and application-role negative boundaries.
- Cross-repository host-lock contention, failed-health rollback, restricted
  monitoring ingestion, stale/missing telemetry, and firing/resolved delivery.
