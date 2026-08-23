# Workflow Observability — v1.3.2

The system should make its chosen execution path visible without exposing hidden chain-of-thought.

## Timing requirement

For every non-Simple task, emit the Route block immediately after classification and before:
- clarification;
- planning;
- blocker/refusal messages;
- code changes.

Correct:

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: Normal
- Spec: Yes
- TDD: Pending
- Specialist: None

I need the loyalty policy before implementation...
```

Incorrect:

```text
I need the loyalty policy before implementation...
```

A clarification-only response still requires the Route block.

If new information changes the route, emit an updated Route block.

## TDD evidence

When TDD is used, report actual RED / GREEN / REFACTOR / FULL SUITE evidence.

Do not claim a stage that was not executed.

## Verification statuses

Use only:
- Passed
- Failed
- Not run
- Manual/Static check

This avoids turning “looks correct” into “tests passed”.
