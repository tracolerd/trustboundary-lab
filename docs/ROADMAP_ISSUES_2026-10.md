# Prioritized Engineering Backlog

These candidates reflect the documented mock-first LLM application security workbench and its local API boundary.

## Candidate issues

1. **Make API origin configurable for local and hosted modes** — Remove the hard-coded loopback-only assumption and document which modes are supported; never imply the public frontend includes a hosted evaluation service unless verified.
2. **Add deterministic scenario fixtures** — Version safe synthetic prompt-injection, untrusted-retrieval, canary-exposure, and tool-authorization scenarios with expected outcomes.
3. **Define a machine-readable evaluation result schema** — Give each observation a stable rule/scenario ID, evidence, severity, and limitations so results remain comparable across runs.
4. **Test tool authorization boundaries explicitly** — Prove that an untrusted prompt or retrieved document cannot grant a tool capability the caller does not already have.
5. **Separate model output from evaluator truth** — Ensure a model's self-reported assessment cannot mark a security test as passed; use explicit deterministic assertions where possible.
6. **Add request and evaluation timeouts** — Bound input sizes, execution duration, and result size; report timeout as a distinct outcome rather than a pass.
7. **Add regression tests for canary handling** — Cover direct exposure, transformed exposure, false positives, and redaction in reports using non-sensitive synthetic tokens.
8. **Make saved evaluation runs reproducible** — Record scenario version, configuration, evaluator version, and non-secret execution metadata without persisting secret values by default.
9. **Add API/frontend failure-state tests** — Cover unavailable API, invalid configuration, malformed results, and empty scenario sets.
10. **Add CI for backend, frontend, and security fixtures** — Run tests and builds with a clean environment and document any external prerequisites.

## Suggested order

Prioritize trust-boundary tests (2–7) before adding breadth. Keep all scenarios defensive, synthetic, and safely isolated; the workbench should measure application controls, not become a tool for attacking third-party systems.
