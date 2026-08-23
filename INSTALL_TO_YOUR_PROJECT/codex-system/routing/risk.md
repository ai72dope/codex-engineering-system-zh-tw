# Risk Routing

Treat risk independently from complexity.

## High-risk signals
Escalate validation when a task affects:
- authentication or authorization;
- payments, billing, or financial calculations;
- secrets, credentials, cryptography, or security boundaries;
- destructive writes, deletion, migrations, or irreversible operations;
- privacy-sensitive or regulated data;
- concurrency, locking, distributed consistency, or idempotency;
- externally consumed APIs or compatibility-critical formats;
- production infrastructure or deployment controls.

## High-risk behavior
When high risk is detected:
1. Make assumptions and acceptance criteria explicit.
2. Prefer minimal, reversible changes.
3. Load relevant testing/security guidance.
4. Test failure paths and boundary conditions.
5. Preserve existing safeguards.
6. Report anything that could not be validated.
7. Never trade security or data integrity for superficial test success.

Risk escalation does not automatically mean a large implementation. It means stronger reasoning and verification.
