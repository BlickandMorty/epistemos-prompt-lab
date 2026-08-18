---
id: orchestration.codex-goal-adapter
version: 1.0.0
title: Codex Durable Goal Adapter
---

# Purpose

Turn the model-agnostic durable-goal loop into a concrete Codex `/goal`
contract. Official OpenAI documentation recommends a single objective,
verifiable stopping condition, required source material, proof commands or
artifacts, checkpoints, and a short progress log.

# Inputs

- `OBJECTIVE`, `VERIFIABLE_END_STATE`, `READ_FIRST`, `CONSTRAINTS`
- `PROOF_COMMANDS_OR_ARTIFACTS`, `AUTHORIZED_ACTIONS`, `PAUSE_CONDITIONS`

# Template

```text
/goal Complete OBJECTIVE without stopping until VERIFIABLE_END_STATE.

Read READ_FIRST before changing anything. Build a requirement ledger from the
objective, constraints, authorized actions, and end state. Preserve unrelated
user work and do not infer permission for publication, deletion, external
communication, spending, or access changes.

Work in checkpoints. At each checkpoint:
1. compare current evidence with the requirement ledger;
2. choose the smallest action that closes a real gap;
3. execute it within authority;
4. run the relevant PROOF_COMMANDS_OR_ARTIFACTS;
5. record outcome, evidence, remaining gap, and next action.

After interruption or context compression, resume from repository state,
receipts, and the checkpoint record. Do not redo verified work. Treat a test as
evidence only for the behavior it covers. Before completion, audit every
requirement against current files, command output, runtime behavior, or remote
state. Do not stop because the task is long or the context is low.

Pause on PAUSE_CONDITIONS, missing authority, destructive ambiguity, or an
external blocker that safe alternatives cannot bypass. Otherwise continue
until the end state is proved.
```

# Output contract

Compact progress reports naming the checkpoint, what changed, what was
verified, what remains, and any blocker; a final requirement-to-evidence table;
and direct artifact locations.

# Stop and escalate

Stop only when the verifiable end state is established, the user cancels or
pauses, a declared budget ends, or an explicit pause condition occurs. A vague
confidence judgment is not a stopping condition.

# Failure modes

Loose unrelated backlog disguised as one goal; activity reported as progress;
tests narrower than the completion claim; repeated work after resumption;
authority expansion; completion because time or context is low.
