# Audit Evidence Directory

Do not add raw production secrets, clear tokens/codes, personal data, database
dumps, or private photos here.

## Expected evidence

| Suggested file | Contents |
| --- | --- |
| `BASELINE.md` | Output of `scripts/collect_snapshot.sh` after freeze |
| `CI_RUNS.md` | Repository/SHA, workflow URL, UTC time, result |
| `TEST_RESULTS.md` | Tool versions and sanitized command results |
| `IOS_MATRIX.md` | Device, OS, build, gesture/BLE/background results |
| `CONTAINER_IMAGES.md` | Reviewed image names and immutable digests |
| `SBOM/` | Per-component CycloneDX or SPDX inventories generated from the frozen source/images |
| `EXTERNAL_SURFACE.md` | Dated, authorized public listener/route observations |
| `DEPLOY_ROLLBACK.md` | Non-production rollback exercise |
| `BACKUP_RESTORE.md` | Encrypted backup and isolated restore evidence |
| `PRODUCTION_ATTESTATION.md` | Operator-confirmed DNS/firewall/config state without secret values |

## Evidence rules

- Name the source repository and frozen SHA.
- Use UTC timestamps.
- Redact secrets and personal data at collection time where possible.
- Preserve original hashes for binary logs/screenshots retained in the approved
  secure evidence channel.
- Store large/private artifacts outside Git and reference their approved secure
  location and SHA-256 here.
- Have a second person review every artifact before auditor handoff.
