---
name: controlled-harness-engineering
description: "Coordinate substantial, multi-feature software work through explicit requirements, dependency-aware planning, test-driven implementation, deterministic verification, independent review, and human approval gates. Use for long-running implementation, migrations, or refactors that need persistent state and auditable evidence. Do not use for simple questions, tiny edits, or documentation-only corrections."
license: MIT
metadata:
  author: Oguzhan Tekin
  version: "1.0.0"
  adapted-from: yzddp/harnesscode
---

# Controlled Harness Engineering

Use a bounded, observable development loop. The goal is reliable completion,
not maximum autonomy.

## Non-negotiable rules

- No automatic commits, pushes, merges, releases, deployments, or destructive
  actions. Obtain explicit human approval first.
- Do not delete useful tests. Tests that establish required behavior become
  part of the repository unless the user explicitly requests a disposable
  experiment.
- Skipped validation is unresolved, not passing. Explain the missing evidence
  and either resolve it or obtain a documented user decision.
- Write a failing test first for every behavior change or bug fix. Confirm that
  it fails for the intended reason before changing production code.
- Use fresh verification evidence before saying work is complete.
- Use a branch or worktree for substantial implementation when the repository
  and environment support it.
- Do not modify global configuration, install global software, or access
  credentials without explicit human approval.
- Agent-authored ledgers and reports are coordination state, not proof. Verify
  their claims against code, commands, and inspectable artifacts.

Read `references/safety-gates.md` before making changes. Read
`references/workflow.md` before planning or executing work.

## Entry criteria

Use this skill when at least one condition applies:

- The task contains multiple independently verifiable features.
- Work spans several components or requires dependency ordering.
- The task may continue across sessions and needs persistent progress state.
- The user requests a controlled harness, implementation loop, or auditable
  agent-development workflow.

Do not invoke it when the task can be completed safely with a few direct reads,
edits, and checks.

## Controlled workflow

1. **Intake**
   - Read repository instructions and the smallest relevant set of files.
   - Identify existing test, build, lint, type-check, and security commands.
   - Record the current branch, worktree status, and relevant baseline.
2. **Clarify and design**
   - Stop for unresolved product behavior or significant implementation choices.
   - Present two or three viable approaches with trade-offs and a recommendation.
   - Obtain human approval before implementation.
3. **Create state**
   - Use the environment's persistent task tracker when available.
   - Otherwise create project-local state from `templates/feature-ledger.json`
     and `templates/blocker-report.json`.
   - Every feature needs measurable acceptance criteria and explicit
     dependencies.
4. **Isolate**
   - Prefer a new worktree or branch.
   - Never overwrite unrelated uncommitted work.
   - Run the smallest useful baseline check before making changes.
5. **Execute ready features**
   - Select only work whose dependencies are complete.
   - Follow a red-green-refactor cycle: failing test first, minimal
     implementation, passing test, then cleanup.
   - Preserve type safety and existing repository conventions.
6. **Verify**
   - Run the exact commands that prove the acceptance criteria.
   - Record results using `templates/verification-report.json`.
   - Treat missing tools, unavailable services, and skipped checks as unresolved.
7. **Review**
   - Use an independent review phase after implementation.
   - Check requirement coverage, regression risk, error handling, and meaningful
     design defects.
   - Use security review when the user requests vulnerability analysis or the
     change affects a sensitive security boundary.
8. **Finish**
   - Map every acceptance criterion to fresh verification evidence.
   - Record unresolved risks in `templates/completion-report.md`.
   - Ask the user whether to commit, push, open a pull request, keep the branch,
     or discard the work when those actions were not already authorized.

## Role boundaries

Read `references/role-definitions.md`. Roles can be sequential phases in one
session. Delegate only genuinely independent work that benefits from separate
context.

The implementer must not approve its own completion. The verifier must rely on
commands and artifacts rather than statements from another role. The reviewer
must evaluate suggestions against the actual repository before requesting
changes.

## State and evidence

Read `references/state-schema.md` before creating persistent state.

- Feature state describes what should happen.
- Blocker state describes why work cannot safely proceed.
- Verification state records what was actually run.
- Completion state maps requirements to evidence.

Never store secrets, credentials, personal data, or confidential source content
in skill state.

## Reference files

| File | Purpose |
|---|---|
| `references/workflow.md` | Detailed gated execution procedure |
| `references/safety-gates.md` | Mandatory approval and stop conditions |
| `references/role-definitions.md` | Coordinator, implementer, verifier, reviewer, and human roles |
| `references/state-schema.md` | State semantics and transition rules |
| `templates/feature-ledger.json` | Dependency-aware feature tracking |
| `templates/blocker-report.json` | Human and environmental blockers |
| `templates/verification-report.json` | Command-level evidence |
| `templates/completion-report.md` | Final requirement-to-evidence report |

## Attribution

This skill adapts role separation, state-file coordination, and iterative
review concepts from `yzddp/harnesscode`. The unsafe unattended execution
behavior is intentionally excluded. See `LICENSE-HARNESSCODE`.
