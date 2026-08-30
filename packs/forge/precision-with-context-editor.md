---
id: forge.precision-with-context-editor
version: 1.0.0
title: Precision-with-Context Editor
---

# Purpose

Edit a prompt, message, README, or piece of writing so it is clearer and more
useful without flattening the person's intent, voice, stakes, or unusual
details. The point is not to make every draft sound polished. The point is to
make the important thing easier to understand.

# Inputs

- `SOURCE_TEXT`, `EDIT_GOAL`, `AUDIENCE`, `NON_NEGOTIABLES`, `RISK_LEVEL`

# Template

```text
Edit SOURCE_TEXT for AUDIENCE and EDIT_GOAL.

First read it on four layers:
1. Literal layer: facts, requests, constraints, and claims that must stay true.
2. Intent layer: what the person is trying to get done, including details that
   may look repetitive but are carrying meaning.
3. Human-signal layer: tone, urgency, hesitation, investment, humor, or
   personal language that should not be erased just because it is informal.
4. Risk layer: sensitive facts, promises, names, credentials, or implications
   that must not be invented, strengthened, or made more specific.

Write a short preservation ledger before editing: facts to retain, phrases or
tone to retain, sensitive material to remove or generalize, and places where
the intended meaning is unclear. Treat NON_NEGOTIABLES as hard constraints.

Make only the smallest edits needed for readability: fix spelling and grammar,
split run-on sentences, group related ideas, remove accidental repetition, and
move sentences when order is the problem. Keep distinctive wording when it is
carrying the person's real meaning. Do not add polished transitions, fake
confidence, professional jargon, claims of expertise, or a new personality.

For uncertain edits, show a cautious alternative instead of silently changing
the claim. For sensitive or high-risk content, generalize only what is needed
and say what was removed. Do not infer facts from emotion or use emotional
language as proof that a conclusion is true.

Return the edited version, then a compact change ledger. The ledger must say
what was corrected, what was reordered, what was preserved on purpose, and
what was left unchanged because changing it would alter intent.
```

# Output contract

Preservation ledger; edited text; optional cautious alternative for genuinely
ambiguous wording; concise change ledger; one question only if the ambiguity
would materially change facts, authority, safety, or the requested outcome.

# Stop and escalate

Stop when the text is easier to read and every item in the preservation ledger
is either retained, intentionally generalized, or explicitly flagged. Escalate
only when a factual or sensitive choice cannot be made safely from the source.

# Failure modes

Making informal writing sound generic; treating emotion as a defect; treating
emotion as evidence; deleting an unusual detail that carries the actual point;
inventing competence; adding facts to make the author look stronger; removing
too much under the name of safety.
