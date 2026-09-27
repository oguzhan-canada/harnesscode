# Controlled Harness Engineering Skill

## Purpose

Create a reusable GitHub Copilot skill that adapts HarnessCode's strongest
coordination ideas into a controlled, evidence-driven development workflow.
The skill must support long, multi-feature implementation without inheriting
HarnessCode's unsafe unattended execution model.

## Scope

The skill will be installed in two locations:

- Repository: `.github/skills/controlled-harness-engineering/`
- Personal: `C:\Users\Owner\.agents\skills\controlled-harness-engineering\`

The repository copy is the source of truth. The personal copy must be an exact
copy so the workflow is available in other repositories.

## Trigger

Use the skill for substantial implementation work involving multiple features,
dependencies, checkpoints, or verification stages. Do not use it for simple
questions, one-file edits, documentation-only corrections, or tasks that fit
within a few direct tool calls.

## Workflow

1. Intake repository instructions, requirements, architecture, and available
   validation commands.
2. Clarify unresolved requirements and significant design decisions.
3. Convert approved requirements into a dependency-aware feature ledger with
   measurable acceptance criteria.
4. Establish an isolated branch or worktree and record the baseline state.
5. Implement each ready feature with a failing test first.
6. Run deterministic repository validation and preserve useful regression
   tests.
7. Perform independent review after implementation.
8. Pause for human approval before risky, destructive, external, or
   irreversible actions.
9. Declare completion only when every acceptance criterion has fresh evidence.

## Safety invariants

- No infinite or unattended execution loop.
- No automatic commits, pushes, merges, releases, deployments, or destructive
  actions without explicit user authorization.
- No global tool or user configuration changes without explicit approval.
- No deleting generated tests merely because they pass.
- A skipped validation layer is unresolved, not passing.
- Agent-authored status files are claims, not evidence.
- Completion requires deterministic command output or directly inspectable
  artifacts.
- Work must stop when requirements conflict, required credentials are absent,
  or a meaningful design choice remains unresolved.
- Security review is required when the task explicitly requests vulnerability
  analysis or materially changes a sensitive security boundary.

## State model

The skill uses a small set of persistent artifacts:

- Feature ledger: requirements, dependencies, status, acceptance criteria, and
  changed files.
- Blocker report: unresolved questions and the work they block.
- Verification report: commands, timestamps, exit results, and skipped checks.
- Completion report: requirement-to-evidence mapping and unresolved risks.

Repository-native task tracking should be preferred when available. Artifacts
must not contain credentials, tokens, personal data, or confidential content.

## Roles

- Coordinator: maintains state and selects only dependency-ready work.
- Implementer: follows test-driven development and does not self-approve.
- Verifier: runs deterministic checks and records full evidence.
- Reviewer: independently checks requirements, regressions, and meaningful
  design flaws.
- Human approver: decides ambiguous requirements and authorizes risky actions.

Roles may be phases in one session or separate subagents when the tasks are
genuinely independent. Role labels do not justify unnecessary delegation.

## Skill package

```text
.github/skills/controlled-harness-engineering/
├── SKILL.md
├── LICENSE-HARNESSCODE
├── references/
│   ├── workflow.md
│   ├── safety-gates.md
│   ├── role-definitions.md
│   └── state-schema.md
└── templates/
    ├── feature-ledger.json
    ├── blocker-report.json
    ├── verification-report.json
    └── completion-report.md
```

## Attribution

The workflow is adapted from the role separation, state-file coordination, and
review loops in `yzddp/harnesscode`, which is licensed under the MIT License.
The skill will include the upstream license. Instructions will be rewritten
rather than copied verbatim except where a concise concept or field name is
necessary for compatibility or attribution.

## Acceptance criteria

- `SKILL.md` has valid frontmatter and an explicit trigger description.
- Every referenced file exists.
- Every JSON template parses successfully.
- The skill forbids automatic commits and deletion of generated tests.
- The skill defines skipped validation as unresolved.
- The skill requires test-first implementation and fresh verification.
- The repository and personal copies are byte-for-byte identical.
- The repository contains automated tests enforcing the structural and safety
  contract.
