# Prompt Guide
A strong coding request usually makes these explicit when they matter:
1. Task
2. Context
3. Scope
4. Expected behavior
5. Constraints
6. Edge cases
7. Validation

Generic template:
```text
[Task]
[Context]
[Scope]
Allowed changes:
Do not change:
[Expected Behavior]
[Constraints]
[Edge Cases]
[Validation]
```

Avoid vague requests such as "optimize this" without a target, broad rewrites by default, guarantees of zero bugs, or treating generated tests as executed tests.

Prompts do not need to be long. Make decision-critical information explicit and let Codex inspect repository context that is already available.
