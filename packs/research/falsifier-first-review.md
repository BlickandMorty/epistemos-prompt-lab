---
id: research.falsifier-first-review
version: 1.0.0
title: Falsifier-First Review
---

# Purpose

Stress-test a claim, theorem sketch, model, or conclusion before investing
confidence in it.

# Inputs

- `CLAIM`, `SUPPORTING_EVIDENCE`, `DOMAIN_ASSUMPTIONS`, `CONSEQUENCE_IF_WRONG`

# Template

```text
Treat CLAIM as unproven. Normalize it into premises, quantifiers, scope, and
predicted observations without strengthening a vague claim.

Construct the strongest fair case for it, then attack it with the smallest
counterexample, boundary and degenerate cases, an alternative mechanism, a
violated hidden assumption, measurement or selection error, and the chance
that a valid result is irrelevant to the intended conclusion.

For each attack say whether it refutes, weakens, or leaves the claim intact.
For formal notation check type, domain, quantifier order, and where each
assumption is used. Do not call a theorem verified unless a proof checker or a
complete human-reviewable proof actually verifies it.

Repair only the smallest necessary part and rerun the decisive counterexample.
```

# Output contract

Normalized claim; strongest support; ranked falsification attempts; surviving
counterexample; minimal repaired claim; verdict; and next discriminating test.

# Stop and escalate

Stop after high-risk failures and a boundary case are tested. Escalate when
required domain expertise or tooling is unavailable.

# Failure modes

Straw attacks; unchecked counterexamples; confusing no found counterexample
with proof; repairing so broadly that the original claim disappears.
