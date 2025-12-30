# WRP Verifier
## Verification Contract

---

## Role

The WRP Verifier validates receipts produced under the
Witness Receipt Protocol (WRP).

It performs deterministic, offline verification.

It does not generate receipts.
It does not evaluate policy.
It does not interpret meaning.

---

## Verification Guarantees

The verifier MUST:

- Recompute canonical bytes
- Recompute the receipt hash
- Compare hashes exactly
- Fail on any mismatch

Verification is binary: PASS or FAIL.

---

## Statelessness

Verification:

- Does not depend on network access
- Does not depend on system state
- Does not depend on the issuing service

Only the receipt and protocol rules are required.

---

## Failure Conditions

Verification MUST fail if:

- Canonicalization differs
- Hash mismatch occurs
- Schema version is unknown
- Receipt structure is invalid

---

## Authority Boundary

The verifier does not decide truth.

It proves whether a receipt conforms to
the Witness Receipt Protocol rules.
