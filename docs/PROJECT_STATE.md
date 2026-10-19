# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 6 (Live Provider Adapter)
- [x] Phase 4 completed (Local RAG Sandbox).
- [x] Phase 5 completed (Unauthorized Tool Execution blocked at App Boundary).
- [ ] Implement an optional adapter for a live provider (e.g., Gemini/OpenAI).
- [ ] Ensure live provider uses `.env` secrets and respects cost/rate limits.
## Architecture & Decisions
- **Tool Authorization:** Created `ToolRegistry` in the application layer. Even if the LLM attempts to call a sensitive tool, the execution is intercepted and blocked based on the deterministic `user_role` field, preventing privilege escalation.
