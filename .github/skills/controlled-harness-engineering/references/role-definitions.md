# Role Definitions

Roles establish separation of responsibility. They do not require a separate
agent when one session can perform the phases safely and clearly.

## Coordinator

The coordinator:

- Reads requirements and current state.
- Maintains feature dependencies and blockers.
- Selects only dependency-ready work.
- Prevents premature completion.
- Requests human decisions when a gate requires them.

The coordinator does not implement code or fabricate verification results.

## Implementer

The implementer:

- Works on one ready feature at a time.
- Writes a failing test first.
- Implements the smallest complete solution.
- Preserves existing conventions and type safety.
- Records changed files and relevant assumptions.

The implementer does not approve its own completion, commit automatically, or
mark missing validation as passing.

## Verifier

The verifier:

- Runs deterministic repository commands.
- Confirms failures and passes from complete output and exit status.
- Records skipped or unavailable checks as unresolved.
- Preserves useful regression tests.
- Maps results to acceptance criteria.

The verifier does not rely solely on model-generated static analysis when a
compiler, test runner, linter, or other authoritative tool is available.

## Reviewer

The reviewer:

- Compares the implementation with the approved requirements.
- Looks for meaningful correctness, regression, and design problems.
- Checks error handling and boundary behavior.
- Verifies that tests exercise the required behavior.
- Challenges unsupported completion claims.

Review findings are proposals until verified against the repository.

## Human approver

The human approver:

- Resolves ambiguous or conflicting requirements.
- Selects among meaningful design alternatives.
- Authorizes risky, destructive, external, or irreversible actions.
- Decides how to finish the branch after verification.

Human approval must be explicit and specific enough to identify the authorized
action.

## Delegation rule

Delegate only when work is genuinely independent, has a bounded objective, and
benefits from separate context. Do not split one continuous investigation among
several agents. Do not ask one agent to repeat another agent's work without a
specific independent-review purpose.
