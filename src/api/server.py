from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json
import os
from src.engine.runner import EvaluationRunner
from src.engine.reporter import Reporter
from src.engine.evidence_archive import archive_existing_evidence
from src.providers.mock_provider import MockProvider
app = FastAPI(title="TrustBoundary Lab API", version="1.0")
# CORS restricts browser origins; it does not provide authentication. Keep
# credentials disabled and configure exact frontend origins for each environment.
_default_origins = "http://localhost:5173,http://127.0.0.1:5173"
_allowed_origins = [
    origin.strip()
    for origin in os.getenv("TRUSTBOUNDARY_CORS_ORIGINS", _default_origins).split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)
@app.get("/api/scenarios")
def get_scenarios():
    scenarios = []
    for p in Path("scenarios").glob("*.json"):
        with open(p, "r", encoding="utf-8-sig") as f:
            scenarios.append(json.load(f))
    return {"scenarios": scenarios}
@app.post("/api/run")
def run_all_scenarios():
    # Preserve prior results before writing new evidence.
    evidence_dir = Path("evidence")
    archive_existing_evidence(evidence_dir)
    # We use MockProvider by default to ensure safe, cost-free UI testing
    provider = MockProvider()
    runner = EvaluationRunner(provider)
    results = []
    for s in Path("scenarios").glob("*.json"):
        res = runner.run_scenario(str(s))
        results.append(res)
    reporter = Reporter()
    summary = reporter.generate_summary()
    return {"summary": summary, "details": results}
@app.get("/api/reports/summary")
def get_summary_report():
    summary_path = Path("evidence/summary_report.json")
    if summary_path.exists():
        with open(summary_path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return {"error": "Report not found. Please run evaluations first."}
