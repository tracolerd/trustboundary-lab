# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 5 (Mocking Tool Authorization)
- [x] Phase 3 completed (Reporter & CLI).
- [x] Phase 4 completed (Local RAG Sandbox implemented with `MockDocumentStore`).
- [ ] Implement scenarios for unauthorized tool calls (simulating App boundary checks).
- [ ] Ensure model responses do not blindly authorize action.
## Architecture & Decisions
- **RAG Sandbox:** Used `MockDocumentStore` to simulate document retrieval. The `rag_document_id` in Scenario JSON dictates if a document gets appended.
- **Evidence Cleanup:** Updated `run_lab.py` to clear old evidence files automatically so reports stay fresh and accurate.
