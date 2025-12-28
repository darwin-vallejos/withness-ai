\# Witness Receipt Verifier Contract



\## Definition

A verifier is any system that recomputes a receipt hash

and checks equality with the declared receipt\_hash.



---



\## Required Inputs

A verifier MUST require only:

\- Receipt JSON

\- schema\_version

\- receipt type



No network access is permitted.



---



\## Canonicalization (v1.0.0)

\- UTF-8 encoding

\- Sorted keys

\- separators = (",", ":")

\- ensure\_ascii = false



---



\## Hash Rule

receipt\_hash = SHA-256(canonical(payload))



---



\## Determinism

Same input MUST yield same result.



---



\## Failure Semantics

Verifier MUST distinguish:

\- Invalid receipt

\- Unsupported schema\_version

\- Unsupported receipt type



---



\## Backward Compatibility

Old schemas MUST NOT be reinterpreted.



---



\## Independence

Verification MUST NOT require:

\- APIs

\- Witness-AI

\- Secrets

\- Cloud services



---



\## Final Rule

If two verifiers disagree,

the receipt format is broken.



