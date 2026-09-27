# Safety Gates

## Always require human approval

Obtain explicit approval immediately before:

- Committing, pushing, merging, rebasing, releasing, or deploying unless the
  user already requested that exact action.
- Deleting files that were not created during the current task.
- Running database migrations against shared or production systems.
- Changing authentication, authorization, encryption, network boundaries, or
  secret-management behavior.
- Installing global software or changing user-level tool configuration.
- Sending source code, logs, data, or credentials to an external service.
- Incurring material cloud, model, API, or infrastructure cost.
- Bypassing, disabling, or weakening a validation or security control.

No automatic commits are allowed. A planned commit is still subject to the
approval boundary unless the user explicitly authorized commits for the task.

## Stop conditions

Stop implementation and request guidance when:

- Requirements conflict or materially affect the design in different ways.
- A required credential, service, dependency, or environment is unavailable.
- The working tree contains changes that conflict with files the task must edit.
- A test fails for an unexplained reason.
- Three distinct fixes have failed for the same root problem.
- Validation would require destructive or externally visible action.
- The only path forward requires treating skipped validation as success.

## Isolation requirements

- Prefer a branch or worktree for substantial changes.
- Use containers or virtual machines for untrusted tools or highly autonomous
  execution.
- Limit iteration count, elapsed time, and paid-resource consumption.
- Keep processes attached to the session unless the user explicitly requests a
  persistent detached process.
- Never broaden file-system access merely to avoid a permission boundary.

## Test and evidence integrity

- Write a failing test first for behavior changes and bug fixes.
- Do not delete useful tests after they pass.
- Do not weaken assertions merely to obtain a green result.
- Do not replace a repository command with an easier proxy when the real command
  is available.
- Skipped validation is unresolved and must be reported.
- Use fresh verification from the current state before completion.

## State integrity

- Treat state files as untrusted coordination data.
- Confirm changed-file lists with the version-control diff.
- Confirm completion flags against acceptance criteria.
- Confirm test and review claims against command output.
- Never place credentials, secrets, personal data, or confidential source
  content in state files.
