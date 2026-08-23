# Spec-Driven Development

Use this layer when implementation would otherwise require guessing important behavior.

## 1. Problem
State the user-visible problem and intended outcome.

## 2. Current behavior
Summarize relevant existing behavior from repository evidence.

## 3. Requirements
List concrete functional requirements.

## 4. Acceptance criteria
Write observable conditions that determine whether the work is complete.

Prefer testable statements such as:
- Given X, when Y, then Z.
- The API returns ...
- The system rejects ...
- Existing behavior A remains unchanged.

## 5. Edge cases
Identify meaningful boundaries, failures, permissions, empty states, retries, compatibility, and data conditions.

## 6. Out of scope
Explicitly state nearby work that is not part of this change.

## 7. Open questions
If an unresolved question materially changes product behavior, ask before implementing. Do not invent the answer.

## 8. Handoff
Use the accepted spec as the source for planning, tests, implementation, and final verification.

Keep specs proportional: enough to remove consequential ambiguity, not documentation for its own sake.


## v1.3.2 observability rule
For non-Simple work, emit the Route block immediately after classification and before clarification, planning, blocker messages, or implementation. If TDD is used, include the required TDD Trace with actual execution evidence.
