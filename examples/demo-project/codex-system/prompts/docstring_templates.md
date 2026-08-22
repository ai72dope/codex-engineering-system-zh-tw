# Structured Coding Prompt Templates

Use these when a task needs a more explicit specification.

## API Request
```text
[Task] Implement an API request
[Context] [language / framework / HTTP client]
[Inputs] [inputs and types]
[Outputs] [expected output]
[Behavior] [success path]
[Errors] [401/403, timeout, 5xx, invalid JSON, etc.]
[Constraints] Prefer existing project dependencies; follow AGENTS.md
[Validation] Add and actually run relevant tests
```

## Data Processing
```text
[Task] Clean and normalize raw data
[Inputs] [fields/types]
[Outputs] [target structure]
[Rules] [normalization rules]
[Edge Cases] null / empty / missing fields / duplicates / invalid dates
[Constraints] Do not mutate original input; avoid unnecessary repeated passes
[Validation] Test important boundaries
```

## Feature
```text
[Feature]
[Goal]
[Current System]
[Expected Behavior]
[Scope]
[Edge Cases]
[Validation]
Analyze and plan before broad changes.
```

## Bug
```text
[Problem]
[Expected]
[Actual]
[Error]
[Steps to Reproduce]
[Environment]
[Recent Changes]
Find the root cause before proposing a broad rewrite.
```

## Refactor
```text
[Goal]
[Current Problems]
[Constraints] Preserve behavior and public API unless explicitly approved
[Validation] Run existing tests and add regression coverage when needed
```
