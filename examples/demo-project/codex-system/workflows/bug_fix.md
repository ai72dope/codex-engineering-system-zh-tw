# Bug Fix Workflow

## Phase 0 — Route
Classify complexity and risk. Load debugging/testing/security guidance only when relevant.

## Phase 1 — Reproduce
Use a failing test, error, log, or reliable reproduction path. If reproduction is not possible, say so and identify what evidence is available.

## Phase 2 — Root Cause
Trace from symptom to cause. Distinguish repository evidence from hypotheses. Do not patch the first suspicious line without explaining why it causes the observed behavior.

## Phase 3 — Regression Test
When practical, create a test that demonstrates the bug before the fix and protects against recurrence.

For suitable bugs, use the TDD loop:
`Red → Minimal Fix → Green → Refactor`

## Phase 4 — Minimal Fix
Fix the confirmed root cause with the smallest appropriate change. Do not swallow errors, disable safeguards, or hard-code around the symptom.

## Phase 5 — Verify
Run the focused regression test and relevant broader checks. For high-risk fixes, test important failure/boundary paths.

## Phase 6 — Report
Report root cause, changed behavior, exact validation status, and any remaining uncertainty.


## Observability
For Standard, Complex, or High-Risk work, emit the compact Routing Trace defined in `AGENTS.md`. If TDD is selected, include the TDD Trace with actual execution evidence.


## v1.3.2 observability rule
For non-Simple work, emit the Route block immediately after classification and before clarification, planning, blocker messages, or implementation. If TDD is used, include the required TDD Trace with actual execution evidence.
