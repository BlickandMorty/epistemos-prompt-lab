# Provenance and IP Boundary

This library is an original consolidation of methods developed in Epistemos
research notes, prompt experiments, agent workflows, and software projects.
The public wording was rewritten for standalone use and screened to exclude
private context.

## Influences

The library builds on broadly published prompt-engineering practices:

- task-scoped reusable patterns, as demonstrated by the MIT-licensed
  [Fabric](https://github.com/danielmiessler/Fabric) project;
- structured instructions, examples, evaluation, and iteration described in
  the official [OpenAI prompting guide](https://developers.openai.com/api/docs/guides/prompting)
  and [Anthropic prompting documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview);
- programmatic prompt optimization as represented by
  [DSPy optimizers](https://dspy.ai/learn/optimization/optimizers/);
- the documented Codex
  [durable-goal workflow](https://learn.chatgpt.com/use-cases/follow-goals),
  which emphasizes one objective, a verifiable stopping condition, named
  evidence, and checkpoints;
- official Claude Code documentation for
  [session continuation and bounded CLI runs](https://code.claude.com/docs/en/cli-usage)
  and [project memory files](https://code.claude.com/docs/en/memory);
- ordinary software assurance practices: least privilege, threat modeling,
  testable acceptance criteria, and provenance.

## What is not included

- leaked, extracted, or reconstructed proprietary system-prompt text;
- confidential employer, client, school, or personal material;
- local machine paths, credentials, account identifiers, or private logs;
- jailbreak payload collections or instructions for bypassing safeguards;
- claims that prompt wording alone constitutes formal proof or statistical
  computation.

References to commercial model families are comparative concepts only. The
system-prompt builder uses common architectural ideas—identity, capability
honesty, tool contracts, safety boundaries, instruction priority, and output
contracts—in independently written language.

## Derivation policy

When incorporating an external open-source artifact, preserve its license and
attribution. When learning from a proprietary product, retain only high-level,
publicly documented concepts and write a new implementation. Similar function
does not justify copied expression.
