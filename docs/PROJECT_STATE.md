# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 4 (Local RAG Sandbox)
- [x] Phase 2 & Phase 3 completed (Assertions, Evidence Schema, Reporter, CLI Entry Point).
- [ ] Create a local RAG setup separating trusted and untrusted sources.
- [ ] Implement scenarios where document retrieval affects prompt execution.
## Architecture & Decisions
- **CLI Entry Point:** Created `run_lab.py` as the primary execution script. It runs all scenarios and outputs a high-level console summary, ensuring local validation is simple and quick.
- **Reporting:** `Reporter` class aggregates outcomes into `evidence/summary_report.json` to allow comparison between different configurations or future dashboards.
