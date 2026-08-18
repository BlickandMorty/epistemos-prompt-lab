---
id: orchestration.durable-goal-loop
version: 1.0.0
title: Durable Goal Loop
---

# Purpose

Keep a long-running task aligned across interruptions, context compression,
tool failures, and partial progress.

# Inputs

- `OBJECTIVE`, `DONE_BAR`, `CONSTRAINTS`, `AUTHORIZED_ACTIONS`, `BUDGET_OR_DEADLINE`

# Template

```text
Create a checkpoint containing OBJECTIVE, DONE_BAR, CONSTRAINTS,
AUTHORIZED_ACTIONS, current evidence, decisions, artifacts, next action, and
open risks. It records state; it does not broaden authority.

Loop: reread the goal and compare state to the done bar; choose the smallest
action that produces evidence or closes a gap; execute within authority and
capture a receipt; update decisions, artifacts, risks, and next action; verify
whether the done bar is satisfied.

After interruption or compression, resume from artifacts and receipts without
redoing finished work. If three consecutive iterations hit the same external
blocker and no safe alternative makes progress, report the exact condition and
required state change.

Do not mark complete because time or context is low. Do not loop without new
evidence. Preserve user work and prefer reversible actions.
```

# Output contract

Compact milestone checkpoints; evidence-linked progress; blocker record;
final done-bar checklist and artifact locations.

# Stop and escalate

Stop only on verified completion, explicit cancellation, exhausted declared
budget, or the repeated external-blocker condition.

# Failure modes

Goal drift; completed work repeated; completion by assertion; difficulty called
a blocker; infinite retries with unchanged inputs.
