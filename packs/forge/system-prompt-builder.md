---
id: forge.system-prompt-builder
version: 1.0.0
title: Original System Prompt Builder
---

# Purpose

Design an original system contract from public requirements. Do not reproduce
a proprietary or leaked system prompt.

# Inputs

- `PRODUCT_PURPOSE`, `CAPABILITIES_AND_LIMITS`, `TOOLS`, `TRUST_BOUNDARIES`, `SAFETY_REQUIREMENTS`, `OUTPUT_EXPECTATIONS`

# Template

```text
Build an original system prompt for PRODUCT_PURPOSE from supplied public
requirements. Use this functional checklist: identity and purpose; instruction
priority; capability honesty; boundary between instructions and retrieved data;
tool preconditions, authority, confirmation, and verification; privacy, safety,
refusal, and useful alternatives; output contract; stopping and recovery; and
short failure examples for the highest-risk boundaries.

Write direct rules with one normative verb each. Remove theatrical biography,
duplicated warnings, model-family imitation, and requirements the runtime
cannot enforce. Where safety and usefulness can conflict, state a decision rule
and safe alternative.

Create an evaluation matrix before finalizing. Cover conflicting instructions,
untrusted retrieved text, tool failure, ambiguous authority, sensitive data,
unsupported capability claims, and normal helpful use.
```

# Output contract

Assumptions; numbered system prompt; requirement-to-rule traceability;
evaluation matrix; limitations requiring runtime enforcement.

# Stop and escalate

Stop when every requirement maps to a rule and test with no unavailable
capability. Escalate unresolved policy conflicts to the product owner.

# Failure modes

Copied proprietary wording; unenforceable safety theater; tool permission
implied by identity; conflicting rules; only cooperative tests.
