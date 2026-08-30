# Epistemos Prompt Lab

An evidence-first prompt engineering library for research, software delivery,
AI evaluation, memory design, and approval-gated agents.

This repository was assembled in August 2026 from prompt systems developed
across the broader Epistemos research and engineering work. The public
repository is new; the underlying methods are not a one-day project. They were
consolidated here so the useful patterns can be reviewed and tested without
publishing private brain dumps, machine-specific paths, or a pile of tiny
repositories.

## What is distinctive here

The prompts treat an answer as a small proof obligation. They ask for an
explicit objective, evidence, alternatives, falsifiers, scope boundaries,
verification receipts, and a stopping rule. The recurring pattern is:

`frame -> inspect -> propose -> test -> falsify -> repair -> verify -> stop`

The library favors conservative uncertainty over confident invention and
separates observed facts, inferences, and unresolved questions.

## Prompt packs

| Pack | Use it for |
| --- | --- |
| [Deep research](packs/research/deep-research.md) | Source-grounded synthesis with rival explanations |
| [Falsifier-first review](packs/research/falsifier-first-review.md) | Trying to disprove a claim before accepting it |
| [Causal/Bayesian pipeline](packs/research/causal-bayesian-pipeline.md) | Structuring quantitative research without fake computation |
| [Plan-build-verify](packs/engineering/plan-build-verify.md) | Implementing a scoped software change with receipts |
| [Recursive auditor](packs/engineering/recursive-auditor.md) | Finding and repairing defects until a bounded clean state |
| [Model-output rubric](packs/evaluation/model-output-rubric.md) | Repeatable AI-output evaluation |
| [Defensive red team](packs/evaluation/defensive-red-team.md) | Safe robustness testing without exploit payloads |
| [Approval-gated agent](packs/agents/approval-gated-agent.md) | Tool-using agents with explicit authority boundaries |
| [Instruction-file architect](packs/agents/instruction-file-architect.md) | Repository-level agent rules with testable scope |
| [Prompt upgrader](packs/forge/prompt-upgrader.md) | Compressing a brain dump without silently changing intent |
| [Precision-with-context editor](packs/forge/precision-with-context-editor.md) | Making writing clearer without sanding off the person's point, voice, or stakes |
| [System prompt builder](packs/forge/system-prompt-builder.md) | Building an original, testable system contract |
| [Durable goal loop](packs/orchestration/durable-goal-loop.md) | Long-running tasks that survive interruptions |
| [Deliberation and fusion](packs/orchestration/deliberation-fusion.md) | Combining independent candidate solutions |
| [Full-session orchestrator](packs/orchestration/full-session-orchestrator.md) | From read-first orientation through verified handoff |
| [Codex goal adapter](packs/orchestration/codex-goal-adapter.md) | A `/goal` contract with checkpoints and verifiable stopping |
| [Claude Code loop adapter](packs/orchestration/claude-code-loop-adapter.md) | Resumable work grounded in repository instructions and artifacts |
| [Memory architect](packs/memory/memory-architect.md) | Useful memory with consent, provenance, and expiration |

Each file is a template, not a claim that prompting alone performs statistical
estimation, formal verification, or security testing. Use real tools and domain
review when those claims matter.

## How the prompts make decisions less careless

These prompts are not based on the idea that a model becomes smarter because a
prompt sounds emotional or intense. They are built to give the model more of
the context that a careful person would notice before acting.

- **Precision:** say exactly what has to be true, what the output should look
  like, and what would count as a failure.
- **Context:** make the goal, audience, source material, and hard constraints
  visible instead of assuming the model will infer them.
- **Human signal:** when editing, preserve the part of the text that shows why
  the writer cares or what they are trying to protect. This is not a truth
  signal; it helps avoid a rewrite that is technically clean but misses the
  actual point.
- **Caution:** separate direct facts from inference, identify what is missing,
  and ask before making a change that would alter authority, sensitive details,
  or a material claim.

The practical loop is still simple:

`understand -> state the constraints -> make the smallest useful change -> check what changed -> stop`

## Design language

See [DESIGN_LANGUAGE.md](DESIGN_LANGUAGE.md) for the prompt-engineering style
and [PROVENANCE.md](PROVENANCE.md) for the intellectual-property boundary.

## Validate the library

```bash
python scripts/validate_prompts.py
python -m unittest discover -s tests -v
```

The validator checks required sections and scans for common publication
mistakes such as local absolute paths, secrets, impersonation language, and
claims that a proprietary system prompt was copied.

## Responsible use

The defensive red-team pack is for systems you own or are authorized to test.
It deliberately supplies test categories and reporting structure rather than
harmful payloads. The agent pack requires least authority, explicit approval
for consequential actions, and a reversible-by-default operating model.

## Authorship and AI assistance

> **AI assistance:** substantial
> `████████░░` AI helped with implementation, consolidation, editing, examples,
> and testing across the library.

The author selected the problems the packs are meant to address, chose the
patterns worth keeping, and reviewed the published wording and validation
results. The library also reflects real work in AI evaluation, research
workflows, operations, and the Epistemos project. It does not claim that every
line was manually written without AI or that every template has been proven to
improve every model.

The packs should be judged by whether they are clear, runnable, testable, and
honest about their limits. AI assistance is shown here because hiding it would
be less useful than explaining how the work was made.

## License

MIT. See [LICENSE](LICENSE).
