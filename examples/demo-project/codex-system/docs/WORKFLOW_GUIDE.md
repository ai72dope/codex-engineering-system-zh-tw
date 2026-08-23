# Workflow Guide — v1.3 Adaptive Routing

Codex Engineering System v1.3 does not use the same process for every task.

## 1. Classify
Determine:
- task type;
- complexity: Simple / Standard / Complex;
- risk: Normal / High Risk.

## 2. Choose workflow depth

### Simple
`Understand → Change → Targeted Verify`

### Standard
`Understand → Plan → Implement → Test → Verify`

### Complex
`Understand → Spec → Plan → TDD when appropriate → Implement → Test → Review → Verify`

### High Risk
Keep the appropriate complexity path, but strengthen acceptance criteria, testing, security review, and reporting.

## 3. Add specialist guidance only when needed
Debugging, testing, code review, security, architecture, and refactoring documents are optional layers. Avoid loading everything by default.

## 4. Specs
Specs are for consequential ambiguity, not ceremony. A useful spec defines requirements, acceptance criteria, edge cases, out-of-scope work, and unresolved questions.

## 5. TDD
TDD is selected when a stable automated test can express the behavior and test-first feedback is valuable. It is especially useful for regressions and business rules.

## 6. Verification
The system distinguishes actual execution from reasoning:
- Passed
- Failed
- Not run
- Manual/Static check

This prevents “looks correct” from being reported as “tests passed”.


## 7. Observability

v1.3.1 exposes the chosen route so users can see the system working.

For non-trivial tasks, report:
- task type;
- complexity;
- risk;
- whether Spec is active;
- whether TDD is active;
- any specialist guidance loaded.

When TDD is active, preserve RED/GREEN/REFACTOR execution evidence.

See `OBSERVABILITY.md`.
