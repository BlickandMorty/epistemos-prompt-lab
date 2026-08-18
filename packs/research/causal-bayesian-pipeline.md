---
id: research.causal-bayesian-pipeline
version: 1.0.0
title: Causal, Bayesian, Statistical, and Meta-Analysis Pipeline
---

# Purpose

Route a quantitative research question through the right primitives while
making a hard distinction between conceptual structure and real computation.

# Inputs

- `QUESTION`, `DATA_OR_STUDIES`, `TARGET_POPULATION`, `DECISION_THRESHOLD`

# Template

```text
Translate QUESTION into estimand, population, exposure or intervention,
comparator, outcome, and time horizon. Draw a candidate causal graph and label
confounders, mediators, colliders, selection variables, and unmeasured causes.

Create an identification ledger: assumptions needed, evidence for each, and a
falsifier. Do not adjust for a variable merely because it predicts the outcome.

If DATA_OR_STUDIES contains raw data, specify the statistical model, missing-
data policy, diagnostics, uncertainty measure, sensitivity analyses, and code
needed for actual computation. If it contains multiple studies, compare
estimands and populations before proposing pooling; assess heterogeneity,
dependence, publication bias, and fixed versus random effects.

For Bayesian updating, state the prior and its justification, likelihood,
posterior computation method, calibration check, and decision rule. If no
numbers are computed, call the result a Bayesian-style belief ledger, not a
posterior.

Run negative controls, alternative graphs, robustness bounds, and a leave-one-
source-out challenge where feasible. Separate association, identified causal
effect, estimated effect, and decision recommendation.
```

# Output contract

Estimand; causal graph description; identification ledger; analysis plan;
computation status; diagnostics and sensitivity tests; result with uncertainty;
and what evidence would reverse the decision.

# Stop and escalate

Stop at an analysis plan when data or identification is insufficient. Escalate
instead of manufacturing a numerical conclusion.

# Failure modes

Fake precision; collider adjustment; incompatible studies pooled for sample
size; unlabeled subjective priors; causal language from association; model
selection performed on the same data without correction.
