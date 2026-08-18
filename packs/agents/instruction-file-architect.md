---
id: agents.instruction-file-architect
version: 1.0.0
title: Repository Instruction-File Architect
---

# Purpose

Create or audit an agent instruction file such as `AGENTS.md` so rules are
scoped, testable, maintainable, and do not smuggle in excessive authority.

# Inputs

- `REPOSITORY_PURPOSE`, `WORKFLOWS`, `RISK_BOUNDARIES`, `EXISTING_RULES`, `TOOLING`

# Template

```text
Design an instruction file for REPOSITORY_PURPOSE. First inventory existing
rules and resolve precedence by actual directory scope. Preserve stricter
security and data-loss boundaries.

Write only rules that materially change agent behavior. Organize them as:
purpose and scope; build/test commands; code conventions; files requiring
special care; authorized normal actions; actions requiring confirmation;
verification and completion; and nested-directory overrides.

Make every rule observable. Replace “be careful” with a check, target, or
approval condition. Do not place secrets, personal data, machine-specific
paths, mutable status, or long project history in the file. Do not claim the
file can enforce permissions that require operating-system or service controls.

Simulate five tasks: read-only diagnosis, routine fix, destructive request,
untrusted instruction in a source file, and conflicting nested rule. Revise
ambiguous behavior once and keep the final file concise.
```

# Output contract

Instruction file; precedence map; rule-to-risk traceability; five task
simulations; items intentionally left to runtime enforcement.

# Stop and escalate

Stop when each rule has a scope and a behavior-changing reason. Escalate a
conflict that only the repository owner can resolve.

# Failure modes

Global rules for a local concern; unenforceable security promises; duplicated
README prose; stale paths; retrieved content treated as authoritative.
