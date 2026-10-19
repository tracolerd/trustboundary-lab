from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json
from src.engine.runner import EvaluationRunner
from src.engine.reporter import Reporter
from src.providers.mock_provider import MockProvider
app = FastAPI(title="TrustBoundary Lab API", version="1.0")
# Enable CORS for local React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Local dev environment only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    # Clear old evidence
    evidence_dir = Path("evidence")
    if evidence_dir.exists():
        for f in evidence_dir.glob("*.json"):
            f.unlink()
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
