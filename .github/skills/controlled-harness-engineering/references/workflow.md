# Controlled Workflow

## Gate 0: Preflight

1. Read applicable repository and user instructions.
2. Inspect the repository status without modifying files.
3. Identify the requested outcome, constraints, and measurable success criteria.
4. Discover existing test, build, lint, type-check, formatting, and deployment
   commands.
5. Identify actions that need human approval under `safety-gates.md`.

Stop if the requested outcome is unclear or conflicts with repository rules.

## Gate 1: Design approval

For new behavior, architecture changes, or meaningful workflow changes:

1. Ask one focused clarification question at a time.
2. Present two or three feasible approaches.
3. Explain trade-offs in correctness, complexity, maintenance, and risk.
4. Recommend the smallest complete approach.
5. Obtain approval before changing production code.

Record the approved outcome and excluded scope. Do not silently enlarge the
task.

## Gate 2: Dependency-aware plan

Break the work into features that can each be proven independently. Every
feature must contain:

- A stable identifier.
- A concrete outcome.
- Acceptance criteria.
- Dependencies.
- Expected files or components.
- Required verification commands.
- Current status.

Allowed statuses are `pending`, `in_progress`, `blocked`, and `done`. A feature
may become `in_progress` only when all dependencies are `done`.

Use the environment's persistent task system when available. Use
`../templates/feature-ledger.json` only when no suitable tracker exists or the
user requests a repository artifact.

## Gate 3: Isolation and baseline

1. Prefer a dedicated worktree or branch for substantial work.
2. Preserve unrelated local changes.
3. Record the starting commit or equivalent baseline.
4. Run the smallest command that establishes a useful baseline.
5. If the baseline already fails, separate pre-existing failures from failures
   introduced by the task.

Do not create nested repositories or rewrite history.

## Gate 4: Test-driven execution

For each dependency-ready feature:

1. Mark the feature `in_progress`.
2. Write one minimal failing test first.
3. Run it and verify the failure demonstrates the missing behavior rather than
   a syntax, setup, or dependency error.
4. Implement the smallest complete change that makes the test pass.
5. Run the targeted test and the smallest related regression set.
6. Refactor only while tests remain green.
7. Record changed files and verification evidence.
8. Mark the feature `done` only after its acceptance criteria are proven.

Do not delete useful tests after execution. Do not mark a feature complete from
an agent's narrative claim.

## Gate 5: Verification

Verification must be deterministic whenever the repository provides a command
or inspectable artifact.

1. Run targeted tests for the changed behavior.
2. Run relevant build, type-check, lint, or static-analysis commands.
3. Escalate to broader checks when targeted results expose integration risk.
4. Record command, working directory, timestamp, exit code, and result.
5. If a check cannot run, record it as `unresolved` with the reason and impact.

Skipped validation is unresolved. It cannot be converted to `pass` by inference
or by another agent's statement.

## Gate 6: Independent review

After implementation:

1. Review the diff against the approved requirements.
2. Check for incorrect behavior, missing cases, regression risk, and unsafe
   error handling.
3. Verify that tests measure the requirement rather than a proxy.
4. Confirm there are no unintended configuration, dependency, or API changes.
5. Fix important findings one at a time and rerun affected checks.

The reviewer must not accept a suggested fix without checking it against the
actual codebase.

## Gate 7: Completion and handoff

Completion requires:

- Every feature is `done`.
- Every acceptance criterion maps to fresh verification evidence.
- Required checks pass.
- No blocker remains pending.
- Skipped or unavailable checks are explicitly resolved by implementation or a
  documented human decision.
- The final diff contains no unrelated changes.

Prepare the completion report from `../templates/completion-report.md`. If
commit, push, merge, deployment, or cleanup authorization has not already been
given, request human approval before performing it.

No automatic commits are permitted.
