---
id: forge.prompt-upgrader
version: 1.0.0
title: Intent-Preserving Prompt Upgrader
---

# Purpose

Turn a brain dump or fragile prompt into a compact, testable specification
without silently deleting unusual but important intent.

# Inputs

- `RAW_PROMPT`, `TARGET_MODEL_OR_AGENT`, `AVAILABLE_TOOLS`, `RISK_LEVEL`

# Template

```text
Upgrade RAW_PROMPT for TARGET_MODEL_OR_AGENT.

Extract the objective, deliverables, hard constraints, preferences, context,
authorized actions, exclusions, and done bar. Flag contradictions and details
whose removal changes meaning.

Normalize by deduplicating repetition, replacing paths and stale names with
variables, ordering constraints by priority, translating vague intensifiers
into checks, and separating data from instructions.

Write one executable prompt containing inputs, procedure, tool and authority
contract, output schema, verification, stop rule, and escalation rule. Preserve
stated intent and explicit style constraints without claiming to impersonate
the user.

Attack it for omission, conflict, prompt injection, scope creep, premature
completion, endless looping, and unverifiable claims. Repair material failures
once. Do not add capabilities, facts, permissions, or restrictions absent from
the intent or stated risk. Record each substantive design choice.
```

# Output contract

Intent ledger; ambiguities; upgraded prompt; change log with preserved,
compressed, added, and omitted-with-reason items; five evaluation cases.

# Stop and escalate

Stop when all cases pass. Ask only when competing interpretations materially
change the outcome or authority.

# Failure modes

More words without better tests; novel constraint erased as repetition;
invented intent; hidden scope expansion; identity impersonation.
