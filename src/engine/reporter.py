import json
from pathlib import Path
class Reporter:
    def __init__(self, evidence_dir="evidence"):
        self.evidence_dir = Path(evidence_dir)
    def generate_summary(self) -> dict:
        evidence_files = list(self.evidence_dir.glob("*_evidence.json"))
        total = len(evidence_files)
        passed = 0
        failed = 0
        details = []
        for ef in evidence_files:
            with open(ef, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
                if data.get("passed"):
                    passed += 1
                else:
                    failed += 1
                details.append({
                    "scenario_id": data.get("scenario_id"),
                    "threat_category": data.get("threat_category"),
                    "passed": data.get("passed")
                })
        summary = {
            "total_run": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": f"{(passed / total) * 100:.2f}%" if total > 0 else "0.00%",
            "details": details
        }
        # Save summary report
        summary_file = self.evidence_dir / "summary_report.json"
        with open(summary_file, "w", encoding="utf-8-sig") as f:
            json.dump(summary, f, indent=2)
        return summary
