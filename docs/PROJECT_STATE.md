# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 2 (Assertions, Evidence Schema & Unit Tests)
- [x] Phase 0 & Phase 1 completed (Mock Provider, Core Runner, Pytest setup).
- [ ] Implement Evidence and TestRun output schemas.
- [ ] Expand Assertion logic (e.g., regex, heuristic).
- [ ] Store run evidence to disk for reporting.
## Architecture & Decisions
- **Testing:** Implemented automated testing for the `EvaluationRunner` to verify both secure and vulnerable application responses.
