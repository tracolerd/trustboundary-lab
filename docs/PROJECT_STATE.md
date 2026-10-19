# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 8 (FastAPI Backend Integration)
- [x] Phase 7 completed (Core MVP & CI).
- [x] Implemented FastAPI server to expose runner and evidence.
- [ ] Initialize React + TypeScript frontend.
- [ ] Connect frontend dashboard to FastAPI endpoints.
## Architecture & Decisions
- **Backend API:** Used FastAPI to wrap the existing Python evaluation engine. CORS is fully open `["*"]` strictly because this is a local defensive lab, allowing the upcoming React dev server to communicate without preflight issues.
- **API Runner Execution:** The `/api/run` endpoint currently defaults to the `MockProvider` to ensure the web UI can trigger evaluations without accidental API costs.
