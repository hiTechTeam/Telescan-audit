# Production Deployment Status

**Deployment window (UTC):** 2026-09-01T09:26:13Z to
2026-09-01T09:29:08Z  
**Result:** changed server components deployed successfully; frozen unchanged
infrastructure remained at previously verified production SHAs.

## September 1 deployments

| Component | Source SHA | Production result |
| --- | --- | --- |
| API | `8eebf456ee16a49832cd71116e6ff8d6fe7a954d` | Workflow succeeded after lint, type-check, tests, image build, a production database backup, dry-run/apply migrations, rollout, and Docker health verification |
| User bot | `816deb82c91488044b3372fc35708d95310e60e4` | Workflow succeeded after validation, image build, rollout, and Docker health verification |
| Admin bot | `9b9cdbeab7b3542fb0f82c0afd4d03f041102456` | Workflow succeeded after validation, image build, rollout, and Docker health verification |

Exact workflow URLs and completion times are recorded in
[CI_RUNS.md](CI_RUNS.md).

## Unchanged production infrastructure

Nginx, EU relay, MongoDB, and monitoring source trees already matched their
remote frozen SHAs. Their latest exact-SHA validation/deployment runs were
green, so no empty commit or unnecessary production restart was introduced.

## Distribution boundary

The iOS source is synchronized and its CI is green. This operation did not
publish a new TestFlight or App Store build because the repository has no
distribution workflow and an App Store release is a separate signed release
action. `Telescan-info` and `Telescan-internal-docs` are documentation
repositories and do not define deployment workflows.

## Evidence limitation

Successful workflows prove the configured GitHub production jobs completed
their backup/upload/rollout/health gates. They do not replace a separately
signed operator attestation for firewall, DNS, secret values, image digests,
or isolated backup restoration.
