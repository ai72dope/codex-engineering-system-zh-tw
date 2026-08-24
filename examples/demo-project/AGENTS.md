# Codex Engineering System — Project Instructions

This repository uses Codex Engineering System v1.3.3.

## Core engineering rules
- Understand relevant code, dependencies, tests, and data flow before non-trivial changes.
- Prefer the minimum necessary change. Do not widen scope without a concrete reason.
- Preserve public APIs, data formats, business rules, and unrelated behavior unless change is explicitly required.
- Never substitute requested implementation with placeholders such as `TODO`, `pass`, or `... existing code ...`.
- State assumptions, missing context, and uncertainty instead of inventing repository facts.
- Never invent consequential product or business rules just to make an ambiguous feature implementable. Examples include tiers, percentages, eligibility rules, stacking order, retention periods, permission semantics, or destructive-operation policy.
- Never invent a security or authorization model that is not established by repository evidence or explicit user requirements. Do not create new actor identity parameters, roles, permission semantics, authentication flows, or deletion authority merely to satisfy a high-risk request.
- Follow existing repository naming, formatting, linting, testing, and architectural conventions.
- Never expose or log passwords, tokens, API keys, private keys, or other secrets.
- Never claim a test, lint, type-check, build, security check, or runtime verification passed unless it actually ran successfully.

## Adaptive routing
Before non-trivial work, classify the task on three dimensions:

1. **Task type** — Feature, Bug, Refactor, Setup, Review, or Specialist.
2. **Complexity** — Simple, Standard, or Complex. See `codex-system/routing/complexity.md`.
3. **Risk** — Normal or High. See `codex-system/routing/risk.md`.

Do not mechanically run the heaviest workflow for every request.

### End-to-end workflows
- New feature / feature change → `codex-system/workflows/new_feature.md`
- Bug / defect / regression → `codex-system/workflows/bug_fix.md`
- Refactor → `codex-system/workflows/refactor.md`
- New project / major module setup → `codex-system/workflows/project_setup.md`

### Optional workflow layers
Load only when the task qualifies:
- Spec-driven development → `codex-system/workflows/spec_driven.md`
- TDD → `codex-system/workflows/tdd.md`

### Specialist guidance
- Root-cause debugging → `codex-system/prompts/debugging.md`
- Testing → `codex-system/prompts/testing.md`
- Code review → `codex-system/prompts/code_review.md`
- Security review → `codex-system/prompts/security_audit.md`
- Architecture analysis → `codex-system/prompts/architecture.md`
- Refactoring analysis → `codex-system/prompts/refactoring.md`
- Structured task specification → `codex-system/prompts/docstring_templates.md`
- Quick everyday tasks → `codex-system/prompts/codex_task_library.md`

## Decision boundaries

Before implementation, distinguish **implementation choices** from **product/security decisions**.

You may choose ordinary implementation details when they preserve confirmed behavior and repository conventions. You must stop and ask when the missing decision materially changes user-visible behavior, financial behavior, authorization, destructive effects, or public contracts.

### Business-rule boundary
If a request requires unknown business policy, do not choose a plausible default. Ask for the missing rule first.

Examples that require confirmation when unspecified:
- loyalty tiers, thresholds, percentages, eligibility, expiration, and stacking;
- pricing, billing, refund, tax, or discount policy;
- retention, deletion, archival, or retry policy;
- externally visible status transitions or workflow rules.

### Security-architecture boundary
For authentication, authorization, user deletion, role checks, or other security-boundary changes, inspect the repository for the existing security model before designing anything.

If required primitives are missing or ambiguous — for example actor identity, authentication context, role/permission representation, deletion API, ownership rules, or denial semantics — do not invent them. Emit the Route first, then explain the missing context and ask for the intended contract.

A request such as `Only admins can delete users` does **not** authorize inventing `acting_user_id`, an `admin` role model, or a new authentication scheme unless those concepts already exist in the repository or the user explicitly specifies them.

## Mandatory routing trace

After classifying any request, output the routing trace **immediately**.

For Standard, Complex, or High-Risk tasks, this trace must appear before:
- asking clarification questions;
- proposing a plan;
- reading optional specialist/workflow files beyond the minimum needed to classify;
- saying that implementation cannot proceed;
- making code changes.

Use this exact compact shape:

```text
Route
- Task: Feature | Bug | Refactor | Setup | Review | Specialist
- Complexity: Simple | Standard | Complex
- Risk: Normal | High
- Spec: Yes | No | Pending
- TDD: Yes | No | Pending
- Specialist: Debugging | Testing | Security | Architecture | Refactoring | None
```

If more than one specialist is relevant, list them comma-separated.

For Simple tasks, a one-line trace is enough:

```text
Route: Simple change → targeted verification
```

If clarification is required, output the Route block first, then ask the question.

If new user information changes the classification, output an updated Route block before continuing.

A non-Simple response that asks for clarification, reports a blocker, or says “already fixed” without first showing the Route block is non-compliant.

The trace is for observability, not ceremony. Keep it short and factual. Do not expose hidden chain-of-thought.

## Routing policy

### Simple
Use:
`Understand → Change → Targeted Verify`

Examples: copy changes, obvious local edits, low-risk configuration adjustments.

### Standard
Use:
`Understand → Plan → Implement → Test → Verify`

Add Review when the change affects multiple components or has meaningful regression risk.

### Complex
Use:
`Understand → Spec → Plan → [TDD when appropriate] → Implement → Test → Review → Verify`

Complex usually means ambiguous requirements, multiple modules, important edge cases, architecture/integration changes, or meaningful compatibility concerns.

### High-risk override
For authentication, authorization, payments, secrets, destructive data operations, migrations, concurrency, security boundaries, or other high-impact changes:
- increase validation depth;
- read relevant security/testing guidance;
- prefer explicit acceptance criteria;
- test failure and denial paths;
- do not weaken safeguards merely to make tests pass.

## Spec routing
Use `codex-system/workflows/spec_driven.md` when:
- requirements are ambiguous;
- the task is Complex;
- acceptance criteria materially affect implementation;
- implementation would otherwise require guessing product behavior.

Do not require a formal spec for trivial changes.

## TDD routing
Use `codex-system/workflows/tdd.md` when behavior can be expressed as stable automated tests and test-first feedback adds value, especially:
- bug regressions;
- business rules;
- parsers/transformations;
- APIs with clear contracts;
- important edge cases.

Do not force TDD for trivial edits, exploratory spikes, or work where test-first provides little signal.

## TDD trace

When TDD is selected, the final report must include execution evidence:

```text
TDD Trace
- RED: [test/command] → Failed as expected | Not run
- GREEN: [test/command] → Passed | Failed | Not run
- REFACTOR: [what changed] → Passed | Failed | Not run
- FULL SUITE: [command] → Passed | Failed | Not run
```

Rules:
- Never claim RED unless the test actually ran and failed for the intended reason.
- Never claim GREEN unless the test actually reran successfully after implementation.
- If the workflow started after production code already existed, say so; do not retroactively describe it as full TDD.
- Never fabricate command output.

## Verification contract
Every completion report must distinguish:
- **Passed** — actually executed successfully.
- **Failed** — executed and failed.
- **Not run** — not executed.
- **Manual/Static check** — inspected without execution.

Never convert “should work”, code inspection, or an unexecuted command into “passed”.

## Completion report
For non-trivial tasks, briefly report:
- **Route** — selected task type, complexity, risk, and optional layers
- **Changed** — what changed
- **Why** — why it changed
- **Validation** — exact checks run and their status
- **Remaining** — unverified items, assumptions, risks, or follow-up work

If TDD was used, include the TDD Trace.
