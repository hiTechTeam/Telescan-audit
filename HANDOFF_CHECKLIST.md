# Pre-Release Handoff Checklist

## Source baseline and verification

- [x] Every in-scope repository is committed, clean, on `main`, and synchronized
      with `origin/main` after fetching remotes.
- [x] Current source SHAs and App version/build `1.0 (2)` are recorded.
- [x] Every configured exact-SHA CI/CD workflow is green.
- [x] API, user-bot, admin-bot, database, edge, monitoring, legal, and audit
      package checks were rerun or independently confirmed.
- [x] iOS exact-SHA XCTest, Release build, and bundle validation passed in CI;
      a second unsigned Release simulator build passed locally.
- [x] Public API/legal reachability, route denial, DNS, TLS, Moscow/EU service
      path, backup timer, and central monitoring health were checked read-only.
- [x] Architecture, data flow, risks, App Review, privacy/retention, deployment,
      and evidence indexes match the pre-release source baseline.
- [x] Public Privacy Policy and Terms match the deployed legal version/digest.
- [x] Package contains no `.env`, credentials, clear Review codes, user records,
      database dumps, or private photos; package checker and hashes pass.

## App Store submission

- [x] Two synthetic Telegram review profiles exist with public usernames and no
      personal profile data.
- [x] Separate ten-code batches were issued for 90 days and one code from each
      batch was consumed in the development linking test; nine unused codes per
      profile remain for private Review Notes.
- [x] Review profiles have no active Telescan sessions after operator testing.
- [x] Review notes template, two-device instructions, demonstration video,
      Privacy Policy, Terms, and support address are prepared.
- [ ] Publishing company invites the required people to Apple Developer and App
      Store Connect with least privilege.
- [ ] Replace the local Personal Team with the publishing company Team ID;
      register `hiTeam.TelescaniOS` and enable Sign in with Apple.
- [ ] Confirm build `2` has not already been uploaded, or increment the build.
- [ ] Create a signed Archive/TestFlight build and verify Apple-first sign-in,
      Telegram linking, account deletion, and two-device BLE on that exact build.
- [ ] Complete App Store Connect metadata, screenshots, age rating, privacy
      answers, export-compliance answers, contact phone/email, and paste only
      unused codes into private Review Notes.
- [ ] Monitor the review contact and revoke all remaining review-code batches
      after review and any appeal.

## Operational acceptance

- [ ] Restore a current-schema encrypted production snapshot in isolation and
      record snapshot age, elapsed restore time, indexes, references, and
      least-privilege application-role boundaries.
- [ ] Retain a full sanitized production attestation for DNS, TLS, listeners,
      firewall, WireGuard, SSH policy, mounts, timers, ports, and image digests.
- [ ] Complete restricted monitoring ingest and Grafana-key migration evidence;
      observe both firing and resolved Telegram drill messages.
- [ ] Retain a dated rollback exercise and immutable image/SBOM mapping for the
      frozen server release.
- [ ] Record accessibility and supported-iOS regression results for the signed
      release candidate.
- [ ] Obtain explicit product/release/security-owner sign-off or dated residual
      risk decisions.

## Final authorization

```text
Package version:
Baseline manifest SHA-256:
Signed iOS version/build:
Publishing Apple Team ID:
Security owner:
Product/release owner:
Approved handoff time (UTC):
```
