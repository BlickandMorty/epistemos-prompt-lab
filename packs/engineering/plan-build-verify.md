---
id: engineering.plan-build-verify
version: 1.0.0
title: Plan, Build, Verify
---

# Purpose

Deliver a scoped software change with evidence it works and without silently
overwriting unrelated work.

# Inputs

- `REQUEST`, `REPOSITORY_CONTEXT`, `CONSTRAINTS`, `AUTHORIZED_ACTIONS`, `ACCEPTANCE_TESTS`

# Template

```text
Implement REQUEST inside AUTHORIZED_ACTIONS.

Inspect repository instructions, current state, relevant code, tests, and user
changes. Build a priority ledger: objective, invariants, exclusions, unknowns,
and acceptance tests. Trace the smallest affected surface and state only
reversible assumptions that do not expand scope.

Make the smallest coherent change. Preserve unrelated edits and public
interfaces unless authorized otherwise. Test near the change and at the
integration boundary, including negative and boundary cases proportional to
risk. Review the final diff adversarially for security, error paths,
concurrency, data loss, compatibility, and documentation. Repair material
findings and rerun affected checks plus one integration check.

Never report completion from inspection alone when an executable check exists.
Never broaden permissions, delete data, publish, or contact an external party
without matching authority.
```

# Output contract

Outcome first; files and behavior changed; checks and exact results;
assumptions; residual risks; blocked checks and reproduction steps.

# Stop and escalate

Stop when acceptance tests pass, no unrelated diff remains, and adversarial
review is clean. Escalate destructive ambiguity, missing authority, or
conflicting repository rules.

# Failure modes

Activity presented as outcome; tests changed to hide a defect; broad refactor
during a narrow fix; skipped checks hidden; user work erased for a clean tree.
