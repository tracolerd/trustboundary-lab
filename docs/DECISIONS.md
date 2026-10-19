# Architectural Decisions
## 1. Engine & Data Validation
- **Decision:** Used Python with Pydantic.
- **Rationale:** Strongly typed JSON validation prevents malformed inputs and ensures scenario files always adhere to the threat model schema.
## 2. Evaluation Provider Strategy
- **Decision:** Default `MockProvider` with optional `GeminiProvider`.
- **Rationale:** Ensures the CI pipeline and local lab remain completely free, fast, and deterministic. Live models are strictly opt-in via CLI flag (`--provider gemini`) and respect budget limits (`max_output_tokens`).
## 3. Tool Authorization Boundary
- **Decision:** Implemented `ToolRegistry` at the application layer.
- **Rationale:** LLMs cannot be trusted with direct execution. The model only requests a tool (`CALL_TOOL: name`), while the app layer uses the deterministic `user_role` to approve or deny.
## 4. RAG Sandbox Isolation
- **Decision:** `MockDocumentStore` handles retrieval.
- **Rationale:** Separates trusted app logic from untrusted retrieved text, explicitly testing indirect prompt injections without requiring a heavy ChromaDB setup for the MVP.
