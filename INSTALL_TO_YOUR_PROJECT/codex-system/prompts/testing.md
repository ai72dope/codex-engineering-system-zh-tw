# Testing Guidance

Design tests around observable behavior.

Consider as applicable:
- Happy path
- Boundary values
- Empty / null
- Invalid input
- Error paths
- Regression
- External dependency failures

Use the repository's existing test framework and conventions.

After creating or updating tests, actually run the relevant test set. If applicable, run lint/type checks. Never describe generated tests as passing unless they executed successfully.
