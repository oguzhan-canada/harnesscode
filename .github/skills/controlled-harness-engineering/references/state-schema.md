# State Schema

Use the environment's native persistent task tracker when available. The JSON
templates are a portable fallback, not a requirement to add state files to
every repository.

## Feature ledger

Source: `../templates/feature-ledger.json`

Each feature contains:

- `id`: stable kebab-case identifier.
- `title`: outcome-focused description.
- `status`: `pending`, `in_progress`, `blocked`, or `done`.
- `dependencies`: feature identifiers that must be `done` first.
- `acceptance_criteria`: observable statements that can be proven.
- `expected_files`: anticipated scope, updated as evidence develops.
- `changed_files`: files actually changed.
- `verification_commands`: commands expected to prove the feature.
- `evidence_ids`: links to verification records.

Only one feature should normally be `in_progress` per implementer. Do not mark a
feature `done` until every acceptance criterion has evidence.

## Blocker report

Source: `../templates/blocker-report.json`

Blockers use:

- `type`: `human_decision`, `missing_dependency`, `environment`,
  `permission`, `external_service`, or `baseline_failure`.
- `status`: `pending` or `resolved`.
- `blocks_features`: affected feature identifiers.
- `resolution`: the explicit decision or evidence that resolved the blocker.

Never invent a human decision. A declined question leaves the blocker pending
unless a safe documented default exists.

## Verification report

Source: `../templates/verification-report.json`

Each check records:

- Exact command or inspection.
- Working directory.
- Timestamp.
- Status: `pass`, `fail`, or `unresolved`.
- Exit code when applicable.
- Concise evidence.
- Acceptance criteria proven by the check.

Skipped validation is unresolved. Missing tools, credentials, or services are
reasons, not passes.

## Completion report

Source: `../templates/completion-report.md`

The report maps requirements to evidence, identifies unresolved risks, and
states which finishing action is authorized. It must not claim success beyond
the available evidence.

## Transition rules

```text
pending -> in_progress
pending -> blocked
in_progress -> blocked
in_progress -> done
blocked -> pending
```

`done` may return to `in_progress` only when later evidence reveals a regression
or an acceptance criterion was not actually satisfied. Record the reason.
