# Best Practices
## AGENTS.md
Keep root instructions concise, stable, and executable. Put lasting repository rules there rather than temporary task details. Large repositories can use more specific instructions in subdirectories when appropriate.

## Verifiable environment
Good prompts do not replace a runnable environment. Keep installation, tests, lint/type checks, environment examples, and repository docs usable.

## Avoid fake precision
Rules such as "every function must be under 40 lines" can create mechanical refactors. Prefer understandable responsibilities, readability, maintainability, and testability.

## Security
AI review is assistance, not security certification. High-risk functionality needs appropriate professional review.

## Maintenance
When Codex behavior or your product changes materially, review `AGENTS.md`, compatibility claims, changelog, and the demo flow.
