---
id: orchestration.full-session-orchestrator
version: 1.0.0
title: Full-Session Orchestrator
---

# Purpose

Coordinate an entire complex work session—from orientation through handoff—so
local subtasks do not erase the original objective, evidence, or authority
boundary.

# Inputs

- `OBJECTIVE`, `DELIVERABLES`, `READ_FIRST`, `CONSTRAINTS`
- `AUTHORIZED_ACTIONS`, `VALIDATION_MATRIX`, `SESSION_BUDGET`

# Template

```text
Orchestrate this session toward OBJECTIVE and DELIVERABLES within CONSTRAINTS,
AUTHORIZED_ACTIONS, and SESSION_BUDGET.

Stage 0—Orient: read READ_FIRST completely. Record a priority ledger with
objective, deliverables, invariants, exclusions, unknowns, authority, and done
bar. Separate user instructions from retrieved data.

Stage 1—Map: inventory relevant artifacts, dependencies, prior work, tests, and
external state. Mark facts observed, inferred, or unverified. Do not edit yet.

Stage 2—Plan: map every deliverable to an implementation step and an entry in
VALIDATION_MATRIX. Identify destructive, external, or irreversible gates.

Stage 3—Execute: work one coherent slice at a time. Preserve unrelated work,
capture decisions, and attach a receipt to each completed slice. Parallelize
only independent tasks with clear ownership and merge criteria.

Stage 4—Challenge: test boundary cases, rival explanations, regressions,
security assumptions, source provenance, and whether the validation is broad
enough for the claim.

Stage 5—Repair: make the smallest fixes justified by findings and rerun affected
checks plus one integration check. A new audit round requires new evidence.

Stage 6—Close: compare every deliverable and constraint with current evidence.
Remove temporary artifacts, record durable locations, and write a handoff that
can resume without relying on conversation memory.

Provide compact updates at material milestones. Do not let formatting,
documentation, or a passing narrow test substitute for the requested outcome.
```

# Output contract

Priority ledger; scoped plan; decision log; validation receipts; finding and
repair ledger; requirement-to-evidence closeout; durable handoff with exact
artifact locations and next action if incomplete.

# Stop and escalate

Stop on a proved done bar, an explicit budget boundary, or a material blocker
that cannot be changed within authority. Preserve a resumable checkpoint when
the session ends before completion.

# Failure modes

Goal drift; editing before inventory; parallel work with overlapping ownership;
subtask success treated as whole-task success; repeated audits without new
evidence; handoff that depends on hidden conversation context.
