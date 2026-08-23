# Deep Debugging

## Root-cause analysis
Inspect the error, relevant code/files, expected behavior, actual behavior, and reproduction path.

1. Attempt to reproduce or localize the issue using repository evidence.
2. List up to three plausible root causes, ranked by evidence.
3. Separate confirmed facts from hypotheses.
4. Identify the smallest next action that can confirm or reject the leading hypothesis.
5. Do not patch symptoms before understanding a non-trivial root cause.

## Fix
Once the cause is confirmed, make the minimum necessary fix, preserve unrelated behavior, add a regression test where practical, and run relevant validation.

## Regression check
Inspect adjacent paths, relevant boundaries, error paths, concurrency/retry behavior when applicable, and public API/data-format compatibility. Report only risks with a plausible mechanism.
