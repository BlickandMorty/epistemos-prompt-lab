---
id: evaluation.model-output-rubric
version: 1.0.0
title: Model Output Evaluation Rubric
---

# Purpose

Evaluate model outputs consistently while separating factual quality, task
fit, and style.

# Inputs

- `TASK`, `OUTPUT`, `REFERENCE_MATERIAL`, `HARD_CONSTRAINTS`, `RISK_LEVEL`

# Template

```text
Evaluate OUTPUT only against TASK, REFERENCE_MATERIAL, HARD_CONSTRAINTS, and
this rubric. Do not reward verbosity, confidence, or agreement.

List every hard-constraint violation first; a material violation caps the
overall result. Score each axis from 0 to 4 with one evidence-based sentence:
Grounded, Correct, Constraint-faithful, Complete without padding, Actionable,
Calibrated, Adversarially robust, and Original/integrated.

Quote only the smallest excerpt needed to identify an error. Distinguish fact
defects from preferences. Propose the minimum repair for each material defect,
then rescore the hypothetical repaired output.
```

# Output contract

Hard-constraint gate; axis table with evidence; critical errors; minimal repair
plan; overall verdict and confidence; one test that could change the verdict.

# Stop and escalate

Stop after every axis has evidence and the score is internally consistent.
Escalate when the reference itself is contradictory or insufficient.

# Failure modes

Scoring style as truth; invented requirements; averaging away a hard failure;
numbers without evidence; penalizing a correct abstention.
