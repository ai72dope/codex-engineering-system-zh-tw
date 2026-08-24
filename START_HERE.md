# START HERE — Codex Engineering System v1.3.2

## Install once

Copy:

```text
INSTALL_TO_YOUR_PROJECT/
├── AGENTS.md
└── codex-system/
```

into your repository root:

```text
your-project/
├── AGENTS.md
├── codex-system/
├── src/
└── tests/
```

## Then use Codex normally

No special command syntax is required.

Examples:

- `Fix this login bug.`
- `Add a password reset feature.`
- `Refactor this module without changing its public API.`
- `Review my current changes for security issues.`

## What happens behind the scenes?

v1.3.2 first considers:
1. What kind of task is this?
2. Is it Simple, Standard, or Complex?
3. Is it high risk?
4. Does it need a spec?
5. Would TDD provide useful signal?

That keeps small changes lightweight while giving complex or risky work more engineering discipline.

See `codex-system/docs/WORKFLOW_GUIDE.md` for the routing model.


## New in v1.3.2

For non-trivial work, Codex now reports the selected route.

Example:

```text
Route
- Task: Bug
- Complexity: Standard
- Risk: Normal
- Spec: No
- TDD: Yes
```

If TDD is used, the final report should also show real RED / GREEN / REFACTOR evidence.


## v1.3.2 routing visibility

For Standard, Complex, or High-Risk tasks, the first substantive output should be the Route block.

Even when Codex only needs to ask a clarification question, report an existing fix, or explain that project context is missing, the Route block should appear first.
