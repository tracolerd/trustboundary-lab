from datetime import datetime, timezone
import json

from src.engine.evidence_archive import archive_existing_evidence


def test_archives_existing_evidence_without_overwriting(tmp_path):
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    old_report = evidence / "scenario_evidence.json"
    old_summary = evidence / "summary_report.json"
    old_report.write_text('{"scenario_id":"old"}', encoding="utf-8")
    old_summary.write_text('{"passed":1}', encoding="utf-8")

    archived = archive_existing_evidence(evidence)

    assert archived is not None
    assert archived.parent == evidence / "archive"
    assert "T" in archived.name and archived.name.endswith("Z")
    assert json.loads((archived / old_report.name).read_text(encoding="utf-8"))["scenario_id"] == "old"
    assert json.loads((archived / old_summary.name).read_text(encoding="utf-8"))["passed"] == 1
    assert not old_report.exists()
    assert not old_summary.exists()


def test_no_evidence_returns_none_and_does_not_create_archive(tmp_path):
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    assert archive_existing_evidence(evidence) is None
    assert not (evidence / "archive").exists()


def test_archives_have_distinct_destinations_for_repeated_runs(tmp_path, monkeypatch):
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    (evidence / "first_evidence.json").write_text("{}", encoding="utf-8")

    first = archive_existing_evidence(evidence)
    (evidence / "second_evidence.json").write_text("{}", encoding="utf-8")
    second = archive_existing_evidence(evidence)

    assert first is not None and second is not None
    assert first != second
    assert (first / "first_evidence.json").exists()
    assert (second / "second_evidence.json").exists()
