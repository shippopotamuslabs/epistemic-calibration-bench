"""Run-directory layout, incremental JSONL stores, and the runs index.

Layout:
  runs/index.json
  runs/<pool_hash[:12]>/<model_slug>/<prompt_version>/
      manifest.json
      answers.jsonl            (one row per item x condition)
      grades.<grader_slug>.jsonl
      scores.json / report.md  (written by the score stage)

Every stage writes incrementally and skips keys already on disk, so any
stage can be interrupted and re-run to resume exactly where it stopped.
"""
from __future__ import annotations

import json
import threading
from pathlib import Path

from .config import slugify


class JsonlStore:
    """Append-only JSONL with an in-memory key set; thread-safe appends."""

    def __init__(self, path: Path, key_fields: tuple[str, ...]):
        self.path = path
        self.key_fields = key_fields
        self._lock = threading.Lock()
        self.rows: dict[tuple, dict] = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                row = json.loads(line)
                self.rows[self._key(row)] = row

    def _key(self, row: dict) -> tuple:
        return tuple(row[f] for f in self.key_fields)

    def has(self, *key) -> bool:
        return tuple(key) in self.rows

    def get(self, *key) -> dict | None:
        return self.rows.get(tuple(key))

    def append(self, row: dict) -> None:
        with self._lock:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                f.flush()
            self.rows[self._key(row)] = row

    def __len__(self) -> int:
        return len(self.rows)


def run_dir(runs_dir: Path, pool_sha: str, model: str, prompt_version: str) -> Path:
    return runs_dir / pool_sha[:12] / slugify(model) / prompt_version


def load_index(runs_dir: Path) -> dict:
    p = runs_dir / "index.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def save_index(runs_dir: Path, index: dict) -> None:
    runs_dir.mkdir(parents=True, exist_ok=True)
    (runs_dir / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def index_key(pool_sha: str, model: str, prompt_version: str) -> str:
    return f"{pool_sha[:12]}:{model}:{prompt_version}"
