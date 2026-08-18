---
id: orchestration.deliberation-fusion
version: 1.0.0
title: Deliberation and Fusion Loop
---

# Purpose

Generate genuinely different solutions, test them independently, and fuse
surviving mechanisms without producing a consensus average.

# Inputs

- `PROBLEM`, `CONSTRAINTS`, `EVIDENCE`, `EVALUATION_CRITERIA`, `MAX_ROUNDS` (default 2)

# Template

```text
Normalize PROBLEM and CONSTRAINTS into a decision frame. Generate three
candidates with different mechanisms: conservative/minimal,
ambitious/structural, and orthogonal or assumption-challenging.

For each give its causal story, assumptions, strongest evidence, cost, failure
modes, falsifier, and smallest discriminating test. Evaluate independently
against EVALUATION_CRITERIA before exposing scores to one another.

Run a collision pass: identify incompatible claims, compatible useful features,
and trade-offs that must stay explicit. Fuse only compatible, causally
justified components. Never average away a hard constraint or accumulate every
feature into a maximal design.

Test the fusion against the best standalone candidate and a do-nothing
baseline. Run at most MAX_ROUNDS; another round requires new evidence or a
failed discriminating test.
```

# Output contract

Decision frame; candidate cards; independent score/evidence matrix; collision
ledger; fused proposal with component provenance; tests and stop reason.

# Stop and escalate

Stop when one proposal dominates or the remaining choice is a value judgment
for the decision owner.

# Failure modes

Stylistic variants; majority vote replacing evidence; fusion by accumulation;
hidden disagreement; rounds without new information.
