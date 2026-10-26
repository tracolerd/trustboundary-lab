"""Archive prior evaluation evidence instead of deleting it."""

from datetime import datetime, timezone
from pathlib import Path
import shutil


def archive_existing_evidence(evidence_dir: str | Path) -> Path | None:
    """Move top-level JSON evidence and summary reports into a UTC-stamped archive.

    Only direct children are moved. Existing archives are never included in later
    runs, so a summary only aggregates the current run's evidence.
    """
    root = Path(evidence_dir)
    if not root.exists():
        return None

    files = sorted(path for path in root.glob("*.json") if path.is_file())
    if not files:
        return None

    archive_root = root / "archive"
    archive_root.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    destination = archive_root / stamp
    suffix = 1
    while destination.exists():
        destination = archive_root / f"{stamp}-{suffix}"
        suffix += 1
    destination.mkdir(parents=False, exist_ok=False)

    for source in files:
        shutil.move(str(source), str(destination / source.name))

    return destination
