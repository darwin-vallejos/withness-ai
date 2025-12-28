\# Witness Receipt Protocol (WRP)



\## Core Law

Evolution is allowed. Mutation is forbidden.



The system may only evolve via:

\- schema\_version bumps

\- new endpoints

\- new receipt types



Silent changes are prohibited.



---



\## 1. Immutability

Once a receipt is issued:

\- Its payload

\- Its canonicalization rules

\- Its hash

\- Its meaning



MUST remain valid forever.



No receipt may be reinterpreted retroactively.



---



\## 2. Schema Versioning

Every receipt declares a `schema\_version`.



Any change to:

\- fields

\- canonicalization

\- hashing rules

\- required values



REQUIRES a new schema\_version.



Old schemas remain supported indefinitely.



---



\## 3. Canonicalization

Canonical JSON is defined as:



\- UTF-8 encoding

\- Sorted keys

\- separators = (",", ":")

\- ensure\_ascii = false



Any change requires a schema\_version bump.



---



\## 4. Endpoint Stability

Endpoints are append-only.



Existing endpoints:

\- MUST NOT change behavior

\- MUST NOT change semantics



New behavior requires new endpoints or versioned paths.



---



\## 5. Receipt Types

Each receipt declares a `type`.



Different claims require different receipt types.

Receipt meaning is defined solely by its type + schema\_version.



---



\## 6. Verifiability

Any third party must be able to:

\- Recompute the canonical payload

\- Recompute the hash

\- Verify the receipt offline



Failure = protocol violation.



---



\## 7. Silent Changes

Silent changes are forbidden.



If a verifier cannot reproduce a hash later,

the system is considered compromised.



