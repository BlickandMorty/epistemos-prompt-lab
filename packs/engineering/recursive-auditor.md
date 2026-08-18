---
id: engineering.recursive-auditor
version: 1.0.0
title: Bounded Recursive Auditor
---

# Purpose

Audit and repair a defined artifact until it meets a clean condition, without
an endless “keep looking” loop.

# Inputs

- `TARGET`, `INVARIANTS`, `RISK_MODEL`, `AUTHORIZED_REPAIRS`, `MAX_PASSES` (default 3)

# Template

```text
Audit TARGET against INVARIANTS and RISK_MODEL. Do not edit on the first pass.

Pass 1—Map: identify entry points, trust boundaries, dependencies, and high-
impact failure paths. Record findings with stable IDs, evidence, and severity.

Pass 2—Challenge: try to falsify each finding, search for duplicate or systemic
causes, and test boundaries. Remove findings that lack evidence.

Pass 3—Repair and verify: apply only AUTHORIZED_REPAIRS, test each changed
invariant, then rescan the affected surface for regression.

Continue only when a pass produces new material evidence or failed verification
and never exceed MAX_PASSES. Do not convert preferences into defects. Separate
observed facts from inferred risks.
```

# Output contract

Scope map; finding ledger; repairs and diffs; verification receipts; clean
condition, residual risk, or explicit blocker.

# Stop and escalate

Stop when in-scope invariants pass and no high-confidence material finding
remains, or at MAX_PASSES. Escalate critical findings rather than looping.

# Failure modes

Unbounded recursion; duplicate findings; unauthorized repairs; severity based
on tone; clean verdict without executed checks.
