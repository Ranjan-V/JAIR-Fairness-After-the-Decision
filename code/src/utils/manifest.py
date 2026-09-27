"""Atomic, resumable run-manifest management."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class RunManifest:
    def __init__(self, path: Path):
        self.path = path
        if path.exists():
            self.data = json.loads(path.read_text(encoding="utf-8"))
        else:
            self.data = {"schema_version": 1, "runs": {}}

    def is_complete(self, run_id: str, config_hash: str) -> bool:
        item = self.data["runs"].get(run_id, {})
        return item.get("status") == "COMPLETE" and item.get("config_hash") == config_hash

    def start(self, run_id: str, metadata: dict) -> None:
        self.data["runs"][run_id] = {**metadata, "status": "RUNNING", "started_at": utc_now(), "completed_at": None, "error": None}
        self._write()

    def finish(self, run_id: str, outputs: list[str]) -> None:
        item = self.data["runs"][run_id]
        item.update(status="COMPLETE", completed_at=utc_now(), output_filenames=outputs)
        self._write()

    def fail(self, run_id: str, error: str) -> None:
        item = self.data["runs"][run_id]
        item.update(status="FAILED", completed_at=utc_now(), error=error)
        self._write()

    def skip(self, run_id: str, metadata: dict, reason: str) -> None:
        self.data["runs"][run_id] = {**metadata, "status": "SKIPPED", "started_at": None, "completed_at": None, "error": reason, "output_filenames": []}
        self._write()

    def _write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(json.dumps(self.data, indent=2, sort_keys=True), encoding="utf-8")
        temporary.replace(self.path)

