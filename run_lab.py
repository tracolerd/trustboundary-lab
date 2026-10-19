import sys
from pathlib import Path
from src.providers.mock_provider import MockProvider
from src.engine.runner import EvaluationRunner
from src.engine.reporter import Reporter
def main():
    print("Starting TrustBoundary Lab Evaluation...\n")
    provider = MockProvider()
    runner = EvaluationRunner(provider)
    # স্কিমা ফোল্ডার বাদে শুধু scenarios ফোল্ডারের .json ফাইলগুলো লোড করবে
    scenarios = list(Path("scenarios").glob("*.json"))
    if not scenarios:
        print("No scenarios found in the 'scenarios' directory.")
        sys.exit(1)
    for s in scenarios:
        print(f"[*] Running scenario: {s.name}")
        runner.run_scenario(str(s))
    print("\nGenerating Report...")
    reporter = Reporter()
    summary = reporter.generate_summary()
    print("\n=== EVALUATION SUMMARY ===")
    print(f"Total Scenarios : {summary['total_run']}")
    print(f"Passed          : {summary['passed']}")
    print(f"Failed          : {summary['failed']}")
    print(f"Pass Rate       : {summary['pass_rate']}")
    print("==========================\n")
    print("Detailed summary saved to evidence/summary_report.json")
if __name__ == "__main__":
    main()
