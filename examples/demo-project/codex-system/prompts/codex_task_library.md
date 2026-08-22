# Everyday Task Library

## Quick root-cause analysis
Analyze the current failure. Identify up to three likely causes with evidence and give the smallest next validation step before changing code.

## Minimal bug fix
Fix the confirmed root cause with the minimum necessary change. Add a regression test where practical and run relevant tests.

## Unit tests
Add tests for the requested behavior, including relevant boundaries and error paths. Use the existing framework and actually run the tests.

## Code review
Review the current diff for correctness, security, error handling, maintainability, scope creep, and test gaps. Do not manufacture findings.

## Performance check
Look for concrete bottlenecks: algorithmic complexity, repeated I/O, database queries, network calls, or memory use. Prefer measurable improvements.

## Commit message
Generate a concise commit message based only on the actual diff.

## Technical documentation
Update documentation based on behavior that can be verified in the repository. Mark uncertainty explicitly.
