# Design Language

## The Epistemos pattern

These prompts begin as high-context exploration and end as a compact,
testable contract. Their characteristic moves are:

1. **Read-first priority ledger.** Restate the objective, hard constraints,
   evidence already available, unknowns, and the definition of done.
2. **Outcome before procedure.** Choose steps because they support the done
   bar, not because a familiar workflow says they should exist.
3. **Observed versus inferred.** Label direct evidence, derived conclusions,
   hypotheses, and missing evidence separately.
4. **Falsifier before confidence.** State what evidence would overturn the
   leading conclusion and actively look for it.
5. **Merge without silent loss.** When combining drafts, preserve distinct
   useful claims or record why one was rejected.
6. **Proof-carrying output.** Attach tests, citations, diffs, measurements, or
   other receipts to claims of completion.
7. **Bounded recursive audit.** Reinspect after repair, but stop on a declared
   clean condition, budget, or escalation condition.
8. **Scope and authority fences.** An agent may reason broadly but must act
   only inside the authority it was actually given.
9. **Conservative failure.** Abstain, ask, or propose a reversible experiment
   when evidence is insufficient.
10. **Collision-resistant structure.** Stable identifiers, explicit versions,
    and output schemas make work comparable across runs.

## Compression rules

A raw brain dump often contains the right intent alongside repetition,
project-local paths, stale names, and conflicting instructions. The public
templates remove those accidents while retaining the reasoning structure.

- Replace personal paths and product-specific state with named variables.
- Put constraints in priority order and make conflicts resolvable.
- Prefer one accountable role over a theatrical cast of agents.
- Convert adjectives such as "deep" or "complete" into observable checks.
- Make looping conditional on new evidence or a failed check.
- Preserve supplied tone constraints without claiming to impersonate a user.
- Do not treat an LLM label such as "Bayesian" as actual computation unless a
  model, data, calculation, and validation procedure are present.

## Standard prompt anatomy

Every pack includes purpose, explicit inputs, a reusable template, a required
output contract, stopping and escalation rules, and evaluable failure modes.
A prompt is valuable when another person can run it, inspect the result, and
tell why it stopped.
