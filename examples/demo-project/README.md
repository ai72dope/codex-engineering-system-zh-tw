# Demo Project — v1.3.2.2

This small project demonstrates how Codex Engineering System is installed.

The repository contains:
- `AGENTS.md`
- `codex-system/`
- sample source and tests

Try requests of different depth:
- Simple: `Rename a local variable for clarity without changing behavior.`
- Bug: `Find and fix the order total bug and add a regression test.`
- Complex feature: `Add discount rules with explicit acceptance criteria and tests.`

The purpose is to observe adaptive routing: trivial work stays lightweight, while ambiguous or risky work receives deeper specification and verification.

Use Test 7 to verify that the final response contains a real `TDD Trace` rather than only saying "using TDD".


For routing visibility tests, use a fresh copy of this demo for every test case.
The Route block should appear before clarification or blocker messages.
