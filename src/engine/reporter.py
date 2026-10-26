import json
from pathlib import Path


class Reporter:
    def __init__(self, evidence_dir="evidence"):
        self.evidence_dir = Path(evidence_dir)

    def generate_summary(self) -> dict:
        evidence_files = sorted(self.evidence_dir.glob("*_evidence.json"))
        passed = 0
        failed = 0
        inconclusive = 0
        details = []

        for evidence_file in evidence_files:
            with open(evidence_file, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
            outcome = data.get("outcome")
            # Backwards compatibility for evidence created before outcomes were
            # explicit; new evidence always includes outcome.
            if outcome not in {"passed", "failed", "inconclusive"}:
                outcome = "passed" if data.get("passed") is True else "failed"
            if outcome == "passed":
                passed += 1
            elif outcome == "failed":
                failed += 1
            else:
                inconclusive += 1
            details.append({
                "scenario_id": data.get("scenario_id"),
                "threat_category": data.get("threat_category"),
                "passed": data.get("passed"),
                "outcome": outcome,
                "assertion_type": data.get("assertion_type"),
                "assertion_note": data.get("assertion_note"),
            })

        evaluated = passed + failed
        summary = {
            "total_run": passed + failed + inconclusive,
            "evaluated": evaluated,
            "passed": passed,
            "failed": failed,
            "inconclusive": inconclusive,
            # Exclude inconclusive heuristic outcomes from the denominator.
            "pass_rate": f"{(passed / evaluated) * 100:.2f}%" if evaluated else "N/A",
            "details": details,
        }
        summary_file = self.evidence_dir / "summary_report.json"
        with open(summary_file, "w", encoding="utf-8-sig") as f:
            json.dump(summary, f, indent=2)
        return summary
