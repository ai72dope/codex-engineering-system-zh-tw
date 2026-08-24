# New Feature Workflow

## Phase 0 — Route
Classify complexity and risk using `routing/complexity.md` and `routing/risk.md`.

- Simple feature change: use the lightweight path.
- Standard feature: use the normal workflow below.
- Complex or materially ambiguous feature: load `spec_driven.md`.
- Use `tdd.md` when behavior is testable and test-first work adds value.
- High-risk feature: increase review and validation depth.

## Phase 1 — Understand
Read relevant code, tests, `AGENTS.md`, dependencies, and existing patterns. Identify affected behavior and important unknowns. Separate ordinary implementation details from consequential product/security decisions.

Before implementation, stop for clarification if the feature would require inventing material business rules, authorization semantics, destructive-operation policy, or public-contract behavior that is not established by repository evidence or the user.

## Phase 2 — Define
For Standard work, state the intended behavior and key edge cases in the plan.
For Complex/ambiguous work, create a proportional spec with acceptance criteria and out-of-scope boundaries.

Do not fill open product questions with plausible defaults. Loyalty tiers, discount rates, eligibility, stacking, permission models, actor identity, and destructive-operation semantics are requirements, not implementation details.

## Phase 3 — Plan
Create the minimum implementation plan: files/components to change, API/data impact, compatibility concerns, risks, and validation strategy.

## Phase 4 — Implement
Implement the confirmed approach. Preserve unrelated behavior and avoid unnecessary dependencies or scope expansion.

If TDD is selected, follow Red → Green → Refactor rather than implementing first.

## Phase 5 — Test
Add or update tests for the required behavior. Actually run relevant tests plus applicable lint, type-check, and build checks.

## Phase 6 — Review
Review the diff for correctness, security, error handling, maintainability, performance where relevant, scope creep, compatibility, and test coverage.

## Phase 7 — Verify
Check implementation against the requirements/acceptance criteria. Report Changed / Why / Validation / Remaining using the verification contract.


## Observability
For Standard, Complex, or High-Risk work, emit the compact Routing Trace defined in `AGENTS.md`. If TDD is selected, include the TDD Trace with actual execution evidence.


## v1.3.2 observability rule
For non-Simple work, emit the Route block immediately after classification and before clarification, planning, blocker messages, or implementation. If TDD is used, include the required TDD Trace with actual execution evidence.
