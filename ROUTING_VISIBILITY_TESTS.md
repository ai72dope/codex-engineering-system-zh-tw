# v1.3.2 Routing Visibility Regression Tests

Use a fresh copy of the demo project for each case.

## Test A — Ambiguous Feature

Prompt:

`Add a customer loyalty discount system.`

Expected first output:

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: Normal
- Spec: Yes
- TDD: Pending
```

Then Codex should ask for the missing loyalty policy.

## Test B — High-Risk Authorization

Prompt:

`Add role-based access control so only admins can delete users.`

Expected first output:

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: High
- Spec: Yes
- TDD: Pending
- Specialist: Security, Testing
```

Then Codex may explain that user/auth/deletion context is missing.

## Test C — Already-Fixed Bug

Prompt:

`calculate_order_total currently accepts a negative quantity. Fix this bug and prevent it from happening again.`

If the bug is already fixed, Codex should still show the non-Simple Route block before reporting that no change is needed.

## Pass criteria

Fail the test if Codex asks a clarification question, reports a blocker, or says “already fixed” before showing the Route block.
