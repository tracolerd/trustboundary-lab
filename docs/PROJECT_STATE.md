# TrustBoundary Lab - Project State
## Mission
Evaluate the trust boundaries of an LLM application securely and deterministically using a local, defensive test lab.
## Current Phase: Phase 7 (CI Suite & Final Review)
- [x] Phase 5 completed (Tool Authorization).
- [x] Phase 6 completed (Live Gemini Provider Adapter integrated via opt-in CLI flag, respecting `.env` secrets).
- [ ] Review final architecture.
- [ ] Prepare for any future CI integration or dashboard rendering.
## Architecture & Decisions
- **Live Provider:** Implemented `GeminiProvider` using the official `google-genai` SDK. It is opt-in (`python run_lab.py --provider gemini`) to keep the default execution cost-free and deterministic.
- **Security:** `.env` is fully ignored by Git. Secrets are loaded dynamically via `python-dotenv`. Added `max_output_tokens` constraint to the provider call.
