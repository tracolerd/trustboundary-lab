import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv
from src.providers.mock_provider import MockProvider
from src.engine.runner import EvaluationRunner
from src.engine.reporter import Reporter
from src.engine.evidence_archive import archive_existing_evidence
def main():
    # Load environment variables from .env
    load_dotenv()
    parser = argparse.ArgumentParser(description="TrustBoundary Lab Runner")
    parser.add_argument("--provider", type=str, choices=["mock", "gemini"], default="mock", help="Provider to use for evaluation")
    args = parser.parse_args()
    print(f"Starting TrustBoundary Lab Evaluation (Provider: {args.provider.upper()})...\n")
    # Preserve prior results before writing new evidence.
    evidence_dir = Path("evidence")
    archived = archive_existing_evidence(evidence_dir)
    if archived:
        print(f"Archived previous evidence to {archived}")
    # Provider Selection
    if args.provider == "gemini":
        from src.providers.gemini_provider import GeminiProvider
        try:
            provider = GeminiProvider()
        except ValueError as e:
            print(f"Error: {e}\nPlease add your API key to the .env file.")
            sys.exit(1)
    else:
        provider = MockProvider()
    runner = EvaluationRunner(provider)
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
