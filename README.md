# Codex Engineering System v1.3.2 — English Edition

A repository-installable engineering workflow system for Codex.

Install it once, then keep giving Codex normal requests. The system routes work by **task type, complexity, and risk** instead of forcing every task through the same process.

## Install

Copy these two items from `INSTALL_TO_YOUR_PROJECT/` into your repository root:

```text
AGENTS.md
codex-system/
```

## What changed in v1.3.2?

v1.3.2 fixes routing visibility.

For every non-Simple task, Codex must show the `Route` block immediately after classification — before clarification, planning, blocker messages, or implementation.

Example:

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: High
- Spec: Yes
- TDD: Pending
- Specialist: Security, Testing
```

This addresses a v1.3.1 test result where Codex made the correct routing decision but did not always show it to the user.

## What changed in v1.3.1?

v1.3.1 adds **workflow observability** on top of v1.3's adaptive routing.

For non-trivial tasks, Codex can now show a compact trace such as:

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: Normal
- Spec: Yes
- TDD: Yes
- Specialist: Testing
```

When TDD is used, the system also requires evidence of:

`RED → GREEN → REFACTOR → Full Suite`

This makes it easier to verify that the workflow was actually followed instead of only claimed.

## Adaptive routing introduced in v1.3

v1.3 adds adaptive engineering depth:

```text
Your request
     ↓
Task type + Complexity + Risk
     ↓
┌────────────┬──────────────┬───────────────────────────┐
│ Simple     │ Standard     │ Complex                   │
│ Understand │ Understand   │ Understand                │
│ Change     │ Plan         │ Spec                      │
│ Verify     │ Implement    │ Acceptance Criteria       │
│            │ Test         │ TDD when appropriate      │
│            │ Verify       │ Implement → Review → Verify│
└────────────┴──────────────┴───────────────────────────┘
```

High-risk work such as authentication, payments, destructive data operations, migrations, secrets, or security boundaries automatically receives stronger validation guidance.

## Included

- Feature development workflow
- Root-cause bug fixing
- Refactoring and project setup
- Complexity routing
- Risk routing
- Spec-driven development
- Optional TDD workflow
- Debugging, testing, code review, security, architecture, and refactoring guidance
- Issue / PR / changelog templates
- Demo project

## The idea

The goal is not to make Codex “magically smarter.” It is to give coding work a more consistent engineering process while keeping trivial tasks lightweight.

You can still say:

> Fix this login bug.

> Add password reset.

> Refactor this module without changing its public API.

The system decides how much process the task needs.

## Verification contract

Codex must distinguish checks that actually ran from checks that did not:

- **Passed**
- **Failed**
- **Not run**
- **Manual/Static check**

A code inspection is never reported as a passing test.

## Important

This toolkit provides workflow and project instructions. It does not guarantee error-free, secure, or production-ready AI-generated code. Production changes still require appropriate testing and human judgment.
