# Refactor Workflow
## 1. Baseline
Confirm current behavior and existing tests. If important behavior is untested, consider a characterization test first.

## 2. Plan
State the concrete goal: readability, responsibility boundaries, duplication, coupling, or testability.

## 3. Refactor
Make small behavior-preserving changes. Avoid unrelated dependency upgrades or business-rule changes.

## 4. Validate
Run the relevant baseline tests and applicable lint/type/build checks.

## 5. Review
Check for over-abstraction, excessive fragmentation, new coupling, performance regressions, or tests tied too tightly to implementation details.


## v1.3.2 observability rule
For non-Simple work, emit the Route block immediately after classification and before clarification, planning, blocker messages, or implementation. If TDD is used, include the required TDD Trace with actual execution evidence.
