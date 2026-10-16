# TrustBoundary Lab

**Evaluate AI application security with repeatable tests and inspectable evidence.**

TrustBoundary Lab is a planned evaluation workbench for testing security boundaries in LLM-powered applications. It focuses on prompt injection, untrusted retrieved content, tool authorization, and accidental disclosure of synthetic sensitive data.

> **Project status:** Initial planning and repository setup. The evaluation engine, sandbox, provider adapters, and dashboard are not implemented yet.

## Why this matters

An LLM feature may process user instructions, retrieved documents, tool outputs, and application data in a single context. These inputs do not have equal trust. A useful security evaluation should test whether the surrounding application preserves permissions and data boundaries even when model output is unreliable.

TrustBoundary Lab is designed to help developers run controlled, repeatable tests and compare results as prompts, retrieval logic, tools, or guardrails change.

## Scope of the first version

- A versioned test-case format with setup, adversarial input, expected security property, and evaluation logic.
- A deterministic mock model/provider so core workflows work without external API credentials.
- Direct prompt-injection scenarios against a local demonstration application.
- Indirect injection scenarios using explicitly untrusted sample documents.
- Tool-boundary tests that verify application-side authorization.
- Synthetic canary values for detecting accidental disclosure.
- Run history with input version, output, observed evidence, and pass/fail/indeterminate state.
- A report that explains the test result and notes important limitations.

## Proposed architecture

~~~mermaid
flowchart TD
    A[Versioned Test Cases] --> B[Evaluation Runner]
    B --> C[Mock or Configured Provider]
    C --> D[Isolated Demo Application]
    D --> E[Observed Behavior]
    E --> F[Deterministic Assertions]
    F --> G[Evidence and Evaluation Report]
    G --> H[Regression Comparison]
~~~

The evaluation runner should be independent of the user interface. Provider adapters should implement a small explicit interface and should not bypass the application's own authorization checks.

## Proposed technology

| Area | Planned choice |
|---|---|
| Core engine | Python |
| API | FastAPI |
| Dashboard | React and TypeScript |
| Initial provider | Deterministic mock provider |
| Optional retrieval | ChromaDB for a local RAG demonstration |
| Optional model providers | Gemini, OpenAI, or Anthropic adapters |
| Optional orchestration | Direct implementations first; LangChain or LlamaIndex only when useful |
| Test data | Versioned synthetic and controlled security scenarios |

Live model calls may cost money, depend on rate limits, or change behavior between model versions. External providers are optional and must be configured explicitly. A subscription to a consumer AI product should not be assumed to include API access or quota.

## Evaluation model

Each scenario should record:

- A unique scenario ID and version.
- Threat category and the security property being tested.
- Controlled application setup and test input.
- Expected safe behavior and the assertion method.
- Observed response and relevant evidence.
- Result: passed, failed, or indeterminate.
- Provider/model/configuration metadata where applicable.
- Known limitations and reproduction instructions.

A single numerical security score cannot prove that an application is secure. Reports should include test coverage, false-positive risks, and the limits of the test corpus.

## Development roadmap

1. Define the scenario schema and security threat model.
2. Implement a deterministic mock provider and a small local demo app.
3. Add the evaluation runner and repeatable unit tests.
4. Persist run evidence and expose a simple API.
5. Add a local RAG demonstration with explicitly untrusted documents.
6. Build the dashboard and historical regression comparison.
7. Add optional provider adapters with explicit configuration.
8. Add CI workflows that run a stable, cost-free subset of tests.

## Testing strategy

- Known-safe and known-unsafe synthetic scenarios.
- Negative tests for unauthorized tool calls.
- Tests verifying that retrieved content cannot grant permissions by itself.
- Synthetic canary disclosure tests.
- Regression tests for changes in guardrails and application behavior.
- Tests for malformed cases and incomplete evaluation evidence.
- Provider adapter contract tests and mock responses.
- Explicit tests for indeterminate outcomes where the evidence is insufficient.

## Security and ethical boundaries

This project is for testing systems you own or have explicit permission to assess. The initial release should run against an isolated local demonstration application, not public third-party services. Test data must not contain real credentials or personal information. Any live-provider integration should use environment-based secrets, explicit budget/rate limits, and safe logging.

## Current status

This repository contains the initial project brief and MIT license. No security result, provider integration, RAG protection, or guardrail effectiveness has been established yet.

## Author & Development

**Project author and solo developer:** [Nurul Faiyaz](https://github.com/tracolerd).

This project is independently developed and maintained by Nurul Faiyaz. AI-assisted tools may be used as part of the development workflow; the project author remains responsible for technical decisions, code review, validation, and maintenance.

## License

MIT. See [LICENSE](LICENSE).
