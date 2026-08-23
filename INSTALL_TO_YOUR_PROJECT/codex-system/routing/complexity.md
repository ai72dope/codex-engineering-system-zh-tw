# Complexity Routing

Classify the task before choosing workflow depth.

## Simple
Use when the change is local, obvious, low-risk, and has little behavioral ambiguity.

Typical signals:
- one or very few files;
- no public contract change;
- no meaningful data/schema impact;
- no security-sensitive behavior;
- expected result is obvious.

Default path:
`Understand → Change → Targeted Verify`

## Standard
Use when implementation requires a short plan and meaningful validation but the desired behavior is reasonably clear.

Typical signals:
- several related files;
- normal feature or bug work;
- existing patterns can be followed;
- moderate regression surface.

Default path:
`Understand → Plan → Implement → Test → Verify`

Add Review when useful.

## Complex
Use when the task has ambiguity, broad impact, important edge cases, or architectural/integration consequences.

Typical signals:
- multiple modules or services;
- new public behavior or contract;
- unclear requirements;
- migrations or compatibility concerns;
- substantial security/reliability impact;
- several valid implementation approaches with real tradeoffs.

Default path:
`Understand → Spec → Plan → TDD when appropriate → Implement → Test → Review → Verify`

## Rule
Complexity controls workflow depth, not code size alone. A one-line authorization change may be high-risk; a larger documentation change may still be Simple.
