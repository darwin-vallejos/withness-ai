# Witness AI

Witness AI is a **deterministic decision-attestation system** for AI.

It evaluates a request **before** an AI model responds and decides whether the action is permitted based on a mathematically defined trust score.  
Every decision produces a **cryptographically verifiable receipt** that can be independently validated offline.

Witness does not generate answers.  
It decides **whether an answer is allowed** and proves that decision afterward.

---

## System Flow

1. **Sensors**  
   Independent evidence providers that analyze the input and emit bounded signals (e.g., risk, length, heuristics).

2. **Decision Engine**  
   Computes coherence and trust using fixed mathematics.

3. **Decision Gate**  
   If trust is below threshold, the request is denied.

4. **Receipt Generation**  
   A deterministic payload is hashed to produce a cryptographic receipt.

5. **Verification**  
   Any third party can recompute the hash and verify correctness.

---

## Decision Mathematics

Coherence:
