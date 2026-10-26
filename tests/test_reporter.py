import json

from src.engine.reporter import Reporter


def write_evidence(path, scenario_id, outcome, passed):
    path.write_text(
        json.dumps({
            "scenario_id": scenario_id,
            "threat_category": "direct_injection",
            "passed": passed,
            "outcome": outcome,
            "assertion_type": "heuristic_safe" if outcome == "inconclusive" else "regex_match",
            "assertion_note": None,
        }),
        encoding="utf-8",
    )


def test_summary_reports_inconclusive_separately_and_excludes_from_pass_rate(tmp_path):
    write_evidence(tmp_path / "one_evidence.json", "one", "passed", True)
    write_evidence(tmp_path / "two_evidence.json", "two", "failed", False)
    write_evidence(tmp_path / "three_evidence.json", "three", "inconclusive", None)

    summary = Reporter(tmp_path).generate_summary()

    assert summary["total_run"] == 3
    assert summary["evaluated"] == 2
    assert summary["passed"] == 1
    assert summary["failed"] == 1
    assert summary["inconclusive"] == 1
    assert summary["pass_rate"] == "50.00%"
    assert {item["outcome"] for item in summary["details"]} == {"passed", "failed", "inconclusive"}


def test_summary_uses_na_when_no_scenario_has_deterministic_verdict(tmp_path):
    write_evidence(tmp_path / "one_evidence.json", "one", "inconclusive", None)
    summary = Reporter(tmp_path).generate_summary()
    assert summary["evaluated"] == 0
    assert summary["pass_rate"] == "N/A"
