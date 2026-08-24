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
8. Verify that the repository actually contains the security/data primitives required by the request before implementation.
9. If authentication context, actor identity, roles/permissions, ownership rules, destructive-operation contract, or other security semantics are missing or ambiguous, stop and ask rather than designing a new model implicitly.

Risk escalation does not automatically mean a large implementation. It means stronger reasoning and verification.


## High-risk context gate

High-risk work has a mandatory context gate before implementation.

For authorization or destructive operations, confirm from repository evidence:
- how the acting user/request identity is represented;
- how authentication is established;
- how roles/permissions/ownership are represented;
- what operation/API is being protected;
- what denied requests must do (including no unintended mutation);
- any audit, recovery, or compatibility requirements that materially affect behavior.

If these are necessary for the requested change but absent, do not create substitute architecture merely to complete the task. Emit the routing trace, report the missing contract, and request clarification or the correct repository context.
