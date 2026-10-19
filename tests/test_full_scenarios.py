import pytest
from pathlib import Path
from src.engine.runner import EvaluationRunner
from src.providers.mock_provider import MockProvider
# Load all JSON files in the scenarios directory (ignoring the schema folder)
scenario_files = list(Path("scenarios").glob("*.json"))
@pytest.mark.parametrize("scenario_path", scenario_files, ids=[p.stem for p in scenario_files])
def test_all_scenarios_validity(scenario_path, tmp_path):
    # tmp_path ensures we don't litter the real evidence folder during unit testing
    runner = EvaluationRunner(MockProvider(), evidence_dir=tmp_path)
    result = runner.run_scenario(str(scenario_path))
    # Verify the scenario was parsed and executed correctly
    assert "passed" in result
    assert "scenario_id" in result
    assert result["threat_category"] in ["direct_injection", "indirect_injection", "unauthorized_tool", "canary_leak"]
