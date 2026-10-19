# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 2 (Assertions, Evidence Schema & Unit Tests)
- [x] Phase 0 & Phase 1 completed.
- [x] Implement Evidence and TestRun output schemas.
- [x] Expand Assertion logic (exact_match, regex_match, heuristic_safe).
- [x] Store run evidence to disk for reporting.
- [ ] Create tests for Indirect Injection & Canary Leakage scenarios.
## Architecture & Decisions
- **Evidence Storage:** Run outcomes are saved locally as JSON files in an `evidence/` directory (ignored by git) to facilitate future dashboard generation.
- **Assertions:** Transitioned from single assertion to flexible multiple assertion strategies (`regex` and `heuristic`) to capture varying LLM behaviors.
