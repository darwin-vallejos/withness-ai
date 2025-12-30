\# Witness-AI Governance Contract



\## Role

Witness-AI is a deterministic attestation engine.



It observes inputs, evaluates rules, and emits receipts.

It does not learn, reinterpret, or revise history.



---



\## Allowed Actions

Witness-AI MAY:

\- Evaluate inputs deterministically

\- Produce receipts

\- Declare schema\_version and receipt type

\- Refuse to act when rules fail



---



\## Forbidden Actions

Witness-AI MUST NOT:

\- Modify existing receipts

\- Recompute hashes retroactively

\- Change canonicalization rules silently

\- Alter receipt meaning

\- Depend on external state for verification



---



\## Determinism

Given identical input:

\- Output MUST be identical

\- Hash MUST match

\- Decision MUST match



Non-determinism is forbidden.



---



\## Evolution Rules

Witness-AI evolves ONLY via:

\- New schema versions

\- New receipt types

\- New endpoints



Existing behavior is immutable.



---



\## Authority Boundary

Witness-AI does not decide truth.

It decides permission and proves the decision.



Receipts stand independently of Witness-AI.



