# Test-Driven Development Workflow

Use TDD when expected behavior can be expressed clearly and test-first development provides useful feedback.

## Red
Write or update the smallest meaningful test for the required behavior.
Run it and confirm it fails for the expected reason.

If it unexpectedly passes, investigate whether the behavior already exists or the test is ineffective.

## Green
Implement the minimum production change required to make the test pass.
Run the focused test again.

## Refactor
Improve structure only after behavior is green.
Keep tests passing while refactoring.

## Expand
Add important edge, error, and regression cases when justified.

## Verify
Run the relevant broader test set and applicable lint/type/build checks.

## Rules
- A test that was never run is not a Red test.
- Do not weaken assertions merely to reach Green.
- Do not overfit production code to a single test.
- Prefer observable behavior over implementation-detail assertions.
- For bug fixes, prefer a regression test that fails before the fix and passes after it.


## Required evidence

When this workflow is used, include a `TDD Trace` in the final report.

Minimum evidence:
1. RED command/test name and its actual failing result.
2. GREEN command/test name and its actual passing result.
3. REFACTOR change, if any, plus post-refactor test status.
4. Broader suite status.

If the workflow starts after production code already exists, say so. Do not retroactively describe the work as full TDD.


## v1.3.2 observability rule
For non-Simple work, emit the Route block immediately after classification and before clarification, planning, blocker messages, or implementation. If TDD is used, include the required TDD Trace with actual execution evidence.
