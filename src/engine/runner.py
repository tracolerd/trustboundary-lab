import json
from pathlib import Path
from src.engine.models import Scenario
class EvaluationRunner:
    def __init__(self, provider):
        self.provider = provider
    def run_scenario(self, scenario_path: str) -> dict:
        # utf-8-sig ব্যবহার করা হলো যাতে Windows BOM error না দেয়
        with open(scenario_path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        scenario = Scenario(**data)
        output = self.provider.generate_response(scenario.input_payload)
        # Assertion Logic
        passed = False
        if scenario.assertion.type == "exact_match_exclusion":
            passed = scenario.assertion.value not in output
        return {
            "scenario_id": scenario.id,
            "threat_category": scenario.threat_category,
            "passed": passed,
            "actual_output": output
        }
