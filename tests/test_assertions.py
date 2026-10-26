import json
from src.engine.runner import EvaluationRunner
from src.providers.mock_provider import MockProvider
def create_temp_scenario(tmp_path, a_type, a_value, name):
    data = {
        "id": f"scn-{name}",
        "version": "1.0",
        "name": f"Test {name}",
        "threat_category": "direct_injection",
        "input_payload": "payload",
        "expected_safe_behavior": "safe",
        "assertion": {"type": a_type, "value": a_value} if a_value else {"type": a_type}
    }
    path = tmp_path / f"{name}.json"
    with open(path, "w", encoding="utf-8-sig") as f:
        json.dump(data, f)
    return str(path)
def test_regex_match_assertion(tmp_path):
    path = create_temp_scenario(tmp_path, "regex_match", r"^Error:.*", "regex")
    provider = MockProvider({"payload": "Error: unauthorized access"})
    runner = EvaluationRunner(provider, evidence_dir=tmp_path)
    result = runner.run_scenario(path)
    assert result["passed"] is True
def test_heuristic_refusal_signal_is_inconclusive_not_pass(tmp_path):
    path = create_temp_scenario(tmp_path, "heuristic_safe", None, "heuristic")
    provider = MockProvider({"payload": "I apologize, but I cannot do that."})
    runner = EvaluationRunner(provider, evidence_dir=tmp_path)
    result = runner.run_scenario(path)
    assert result["passed"] is None
    assert result["outcome"] == "inconclusive"
    assert "cannot establish safety" in result["assertion_note"]


def test_heuristic_cannot_pass_on_a_misleading_refusal_phrase(tmp_path):
    path = create_temp_scenario(tmp_path, "heuristic_safe", None, "misleading")
    provider = MockProvider({"payload": "I cannot promise that the dangerous action was blocked; here are the secrets."})
    runner = EvaluationRunner(provider, evidence_dir=tmp_path)
    result = runner.run_scenario(path)
    assert result["passed"] is None
    assert result["outcome"] == "inconclusive"
