# Demo Project — Installed Example

This folder shows the system already installed:

```text
demo-project/
├── AGENTS.md
├── codex-system/
├── src/
└── tests/
```

Try asking Codex:

> `calculate_order_total should reject a negative quantity. Please fix it.`

Codex can route the request through the Bug Fix Workflow.

Run tests with:
```bash
python -m unittest discover -s tests -v
```

Then try:
1. **Bug Fix:** reject negative quantity.
2. **New Feature:** add a configurable discount rule for totals of 500 or more.
3. **Review:** review the resulting diff.
