# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 1 (Mock Provider & Local Runner)
- [x] Phase 0 completed (Repo, Schemas, Threat Model).
- [x] Python Pydantic models for Scenario validation.
- [x] Deterministic MockProvider implemented.
- [x] Core EvaluationRunner created.
- [ ] Write pytest unit tests to verify runner behavior.
## Architecture & Decisions
- **Encoding Issue:** Used `utf-8-sig` in Python to handle Windows PowerShell BOM automatically.
- **Provider:** Started with a deterministic `MockProvider` to ensure zero-cost, reliable test execution before integrating external APIs.
