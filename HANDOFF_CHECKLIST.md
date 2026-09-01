# Audit Handoff Checklist

## Scope and contracting

- [ ] Auditor, owner, dates, methodology, deliverables, confidentiality, and
      retest terms are agreed.
- [ ] `SCOPE.md` and production rules of engagement are signed.
- [ ] Emergency and ordinary communication channels are tested.
- [ ] Third-party/provider testing restrictions are understood.

## Baseline freeze

- [ ] Every in-scope change is reviewed and committed.
- [ ] Every repository working tree is clean.
- [ ] `REPOSITORIES.md` contains final commit SHAs and tags.
- [ ] App version/build and deployed API/container release are mapped to source.
- [ ] `scripts/collect_snapshot.sh` output is stored and SHA-256 recorded.
- [ ] `scripts/hash_package.py` output is stored outside the hashed file set and
      its manifest digest is recorded.
- [ ] No force-push or baseline rewrite is permitted during the audit.

## Verification evidence

- [ ] CI is green at every frozen SHA.
- [ ] API, user-bot, and admin-bot tests/lint/type checks are rerun.
- [ ] iOS Release build, `build-for-testing`, and a completed XCTest run are
      captured.
- [ ] iOS 18/26 and two-device physical BLE checks are recorded.
- [ ] Compose/nginx/WireGuard configuration checks are captured.
- [ ] Dependency inventories, container digests, and SBOM/provenance evidence are
      captured for the frozen baseline.
- [ ] Latest backup and isolated restore evidence is available.
- [ ] Deployment rollback has a dated non-production exercise.

## Documentation consistency

- [ ] Architecture, data flow, threats, risks, privacy, and production topology
      match the frozen source.
- [ ] Public Privacy Policy and Terms match the submitted build.
- [ ] App Store privacy answers match the privacy manifest and policy.
- [ ] Data-retention values match MongoDB TTL indexes and cleanup code.
- [ ] Known limitations are approved rather than silently omitted.

## Access and environment

- [ ] Read-only repository/CI access is provisioned.
- [ ] Staging contains synthetic data and production-equivalent security shape.
- [ ] Test Apple/Telegram identities are prepared without personal data.
- [ ] Auditor IPs, limits, windows, and stop contacts are recorded if production
      testing is authorized.
- [ ] Credential expiry and offboarding owners are recorded.

## App Review

- [ ] Review A and Review B profiles exist and have public usernames.
- [ ] Dedicated Review-code secret is distinct and configured in production.
- [ ] Fresh 30-day code batches are issued only after final build approval.
- [ ] One code per profile is consumed in a clean-install test.
- [ ] Only unused codes are placed in private App Store Connect Review Notes.
- [ ] Unused codes will be revoked after review.

## Secret and data hygiene

- [ ] Package contains no `.env`, tokens, keys, clear codes, user records,
      database dumps, or private photos.
- [ ] `scripts/check_package.py` passes.
- [ ] Logs/screenshots are sanitized and reviewed by a second person.
- [ ] The auditor's storage, retention, and destruction requirements are agreed.

## Final authorization

```text
Package version:
Baseline manifest SHA-256:
Security owner:
Product/release owner:
Approved handoff time (UTC):
Auditor recipient:
```
