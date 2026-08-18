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
| [System prompt builder](packs/forge/system-prompt-builder.md) | Building an original, testable system contract |
| [Durable goal loop](packs/orchestration/durable-goal-loop.md) | Long-running tasks that survive interruptions |
| [Deliberation and fusion](packs/orchestration/deliberation-fusion.md) | Combining independent candidate solutions |
| [Codex goal adapter](packs/orchestration/codex-goal-adapter.md) | A `/goal` contract with checkpoints and verifiable stopping |
| [Claude Code loop adapter](packs/orchestration/claude-code-loop-adapter.md) | Resumable work grounded in repository instructions and artifacts |
| [Memory architect](packs/memory/memory-architect.md) | Useful memory with consent, provenance, and expiration |

Each file is a template, not a claim that prompting alone performs statistical
estimation, formal verification, or security testing. Use real tools and domain
review when those claims matter.

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

## Authorship and assistance

The underlying research direction, experiments, selection criteria, and
Epistemos methodology are the project author's work. AI tools assisted with
implementation, consolidation, editing, and testing. That distinction is made
explicit because provenance is more useful than pretending a tool was absent.

## License

MIT. See [LICENSE](LICENSE).
