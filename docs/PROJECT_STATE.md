# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 3 (Repeatable Reports & Summary)
- [x] Phase 2 completed (Assertions, Evidence Schema & Scenario Tests).
- [ ] Create a summary reporting script to aggregate evidence results.
- [ ] Design a simple CLI or output format for the final report.
## Architecture & Decisions
- **Data-Driven Testing:** Added a dynamic pytest that automatically validates and runs all `scenarios/*.json` files. This ensures no malformed scenarios break the pipeline and future scenarios are tested automatically.
