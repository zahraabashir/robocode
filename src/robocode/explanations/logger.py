"""Experiment Logger: append-only JSONL records for analysis.

``<study_dir>/rounds.jsonl`` has one line per completed round (the analysis
unit). ``events.jsonl`` holds session-level events such as session start,
round start and errors. ``config.json`` records the resolved study config and
the code version.
"""

from __future__ import annotations

import json
import subprocess
import threading
import time
from pathlib import Path
from typing import Any


class ExperimentLogger:
    """Thread-safe JSONL writer for one study directory."""

    def __init__(self, study_dir: str | Path) -> None:
        self.study_dir = Path(study_dir)
        self.study_dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    def write_config(self, config: dict[str, Any]) -> None:
        """Record the study config and provenance (written once per launch)."""
        payload = {
            "config": config,
            "git_commit": _git_commit(),
            "written_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        }
        path = self.study_dir / "config.json"
        if path.exists():  # a relaunch of the same study keeps every config
            path = self.study_dir / f"config_{int(time.time())}.json"
        path.write_text(json.dumps(payload, indent=2, default=str))

    def log_round(self, record: dict[str, Any]) -> None:
        """Append one completed round."""
        self._append("rounds.jsonl", record)

    def log_event(self, event: str, **fields: Any) -> None:
        """Append a session-level event."""
        self._append("events.jsonl", {"event": event, "time": time.time(), **fields})

    def _append(self, name: str, record: dict[str, Any]) -> None:
        line = json.dumps(record, default=str)
        with self._lock, open(self.study_dir / name, "a", encoding="utf-8") as f:
            f.write(line + "\n")


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Load a JSONL file written by :class:`ExperimentLogger`."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return [json.loads(line) for line in lines if line.strip()]


def _git_commit() -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
        )
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
