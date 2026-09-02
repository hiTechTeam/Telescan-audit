# Apple App Review Access

App Review codes are for Apple reviewers entering a code in the shipped iOS
application. They are separate from security-auditor credentials and must not
be included in this package or source control.

## Implemented path

1. The reviewer completes Sign in with Apple.
2. The normal eight-character Telegram-link input is shown.
3. iOS submits the entered value to the authenticated
   `/api/v1/users/me/telegram/link` endpoint.
4. The API checks normal link codes first and the separate `review_codes`
   collection second.
5. The Review code is verified with a dedicated HMAC secret, atomically consumed
   once, and links only its assigned synthetic review profile.

No Review-specific iOS UI or hidden bypass exists. A Review code cannot create a
primary session without a valid Apple-authenticated device session.

## Preconditions

- Create two synthetic Telegram profiles: Review A and Review B.
- Use no personal data; keep public usernames active through review and appeal.
- Start the production user bot once for each profile.
- Record each `telescan_id` outside source control.
- Confirm production `REVIEW_CODE_HMAC_SECRET` is configured and distinct from
  every other application secret.

A review profile can be attached to only one Apple identity at a time. Multiple
codes in one batch support retries/reinstalls using the same Apple subject; they
are not a way to attach the same Telegram profile to unrelated Apple identities.
Use Review A and Review B for independent identities/two-device BLE testing.

The final archive must be signed by the publishing company's paid Apple
Developer team. Register `hiTeam.TelescaniOS` for that team, enable Sign in with
Apple, and use a build number not already uploaded to App Store Connect.

## Issue a batch on the production host

```sh
docker compose exec telescan-api /app/.venv/bin/python -m scripts.review_codes issue \
  --telescan-id REVIEW_PROFILE_ID \
  --count 10 \
  --valid-days 90 \
  --issued-by OPERATOR_IDENTIFIER \
  --apply \
  --confirm ISSUE_REVIEW_CODES
```

The command prints clear codes once after successfully inserting the complete
batch. Copy them directly to the approved secret-delivery location. Do not pipe
the output into ordinary shell history, CI logs, tickets, or evidence files.

## Inspect or revoke

```sh
docker compose exec telescan-api /app/.venv/bin/python -m scripts.review_codes status \
  --batch-id BATCH_ID

docker compose exec telescan-api /app/.venv/bin/python -m scripts.review_codes revoke \
  --batch-id BATCH_ID \
  --revoked-by OPERATOR_IDENTIFIER \
  --apply
```

## Submission procedure

1. Issue separate batches for Review A and Review B, valid for 90 days.
2. Consume one code from each batch in a final clean-install/two-device test.
3. Put only unused codes and synthetic usernames in private App Store Connect
   Review Notes.
4. Include Sign in with Apple, Telegram-linking, Bluetooth permission, and
   two-device discovery instructions.
5. Monitor the review contact throughout review and appeal.
6. Revoke every unused batch after completion.
7. Never place clear codes in this package, Git, screenshots, or security-audit
   findings.

## Pre-submission checks

- Production API, bot, Privacy Policy, Terms, and support contact are reachable.
- Review A and B have valid public usernames and discover each other on physical
  devices.
- Every supplied code is still `issued`, unexpired, and unused.
- Rate limits permit the documented path without weakening normal protection.
- Account deletion succeeds for a synthetic review account.
- The demonstration video and notes contain no phone numbers, private chats,
  tokens, or other personal data.
- The exact submitted build has passed publishing-team signed Apple-first login,
  Telegram linking, account deletion, and two-device BLE checks.
