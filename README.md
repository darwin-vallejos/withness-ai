# Witness AI — Deterministic Decision Attestation

Witness AI is a **deterministic, cryptographically verifiable decision-attestation system** for AI and automated workflows.

It decides **whether** an action is allowed *before* an AI model responds and produces a **receipt** that any third party can independently verify offline — without trusting the AI, the operator, or Witness itself.

This repository contains the **reference implementation** of the Witness Receipt Format (WRF).

---

## What Witness Is (and Is Not)

**Witness AI:**
- Evaluates risk and trust *before* an AI acts
- Produces immutable, verifiable receipts
- Is deterministic and auditable
- Works offline
- Requires no cloud services

**Witness AI is NOT:**
- A model
- A learning system
- A policy engine
- A blockchain
- A logging framework

Witness does not decide what is *true*.  
It decides **whether an action is permitted** and proves that decision afterward.

---

## System Overview

High-level flow:

