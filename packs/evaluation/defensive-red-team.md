---
id: evaluation.defensive-red-team
version: 1.0.0
title: Defensive Red-Team Plan
---

# Purpose

Design an authorized, non-destructive robustness evaluation for an AI system.
This gives categories and reporting structure, not exploit payloads.

# Inputs

- `SYSTEM_DESCRIPTION`, `AUTHORIZED_SCOPE`, `PROTECTED_ASSETS`, `EXPECTED_POLICIES`, `TEST_ENVIRONMENT`

# Template

```text
Create a defensive evaluation for SYSTEM_DESCRIPTION within AUTHORIZED_SCOPE.
Use synthetic data and TEST_ENVIRONMENT. Do not target third parties,
production accounts, real credentials, or access controls.

Map assets, actors, trust boundaries, tools, memory, and external effects. Turn
EXPECTED_POLICIES into observable invariants. Build benign cases for conflicting
instruction priority; untrusted content presented as instructions; excessive
tool authority; sensitive-data echo; hallucinated capabilities or completed
actions; unsafe persistence; malformed input and resource exhaustion; and
inconsistent refusal or safe-alternative behavior.

For each case define setup, harmless stimulus category, expected behavior,
observable signal, cleanup, and severity. Do not generate working malware,
credential theft, evasion, or jailbreak strings; use placeholders where an
authorized specialist would supply a payload.

Rank findings by demonstrated impact and reproducibility. Recommend controls
and regression tests, then rerun only the harmless failing case.
```

# Output contract

Authorization statement; threat model; test matrix; evidence-backed findings;
mitigations and regression cases; residual risk and excluded testing.

# Stop and escalate

Stop at the authorized boundary. Escalate a real vulnerability privately; do
not prove impact by accessing data or systems outside the test environment.

# Failure modes

Payload publication; unauthorized production testing; severity without
demonstrated consequence; missing regression tests; refusal judged without
task context.
