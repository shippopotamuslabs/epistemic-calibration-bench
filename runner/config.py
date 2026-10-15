"""Configuration loading: config.json for settings, .env / environment for the API key.

The API key is NEVER read from config.json and never logged. Resolution order:
  1. OPENROUTER_API_KEY environment variable
  2. OPENROUTER_API_KEY in runner/.env (gitignored)
"""
from __future__ import annotations

import json
import os
from pathlib import Path

RUNNER_DIR = Path(__file__).resolve().parent
BENCH_DIR = RUNNER_DIR.parent
DEFAULT_POOL = BENCH_DIR / "seed_questions.jsonl"
DEFAULT_RUNS = BENCH_DIR / "runs"


def _load_dotenv(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


class Config:
    def __init__(self, raw: dict):
        self.raw = raw
        self.base_url: str = raw.get("base_url", "https://openrouter.ai/api/v1")
        self.models_under_test: list[str] = raw.get("models_under_test", [])
        self.grader_models: list[str] = raw.get("grader_models", [])
        self.concurrency: int = int(raw.get("concurrency", 16))
        self.temperature: float = float(raw.get("temperature", 0))
        self.subject_max_tokens: int = int(raw.get("subject_max_tokens", 1200))
        self.grader_max_tokens: int = int(raw.get("grader_max_tokens", 900))
        # OpenRouter reasoning effort for grader calls ("xhigh" = extra high).
        # None / "" disables. If the provider rejects it (HTTP 400), the
        # client retries without reasoning rather than failing the grade.
        self.grader_reasoning_effort: str | None = raw.get("grader_reasoning_effort") or None
        self.request_timeout_s: float = float(raw.get("request_timeout_s", 180))
        self.max_attempts: int = int(raw.get("max_attempts", 4))
        # DESIGN.md section 6: pilot default is the neutral+confidence condition;
        # left/right audience conditions exist for the flip-rate metric.
        self.conditions: list[str] = raw.get("conditions", ["neutral_conf"])
        self.pool_path: Path = Path(raw.get("pool_path", str(DEFAULT_POOL)))
        self.runs_dir: Path = Path(raw.get("runs_dir", str(DEFAULT_RUNS)))

    def api_key(self) -> str:
        key = os.environ.get("OPENROUTER_API_KEY")
        if key:
            return key
        key = _load_dotenv(RUNNER_DIR / ".env").get("OPENROUTER_API_KEY")
        if key:
            return key
        raise RuntimeError(
            "OPENROUTER_API_KEY not found. Set it as an environment variable or "
            "put OPENROUTER_API_KEY=... in runner/.env (see .env.example)."
        )


def load_config(path: Path | None = None) -> Config:
    cfg_path = path or (RUNNER_DIR / "config.json")
    if not cfg_path.exists():
        raise RuntimeError(f"Config file missing: {cfg_path}")
    return Config(json.loads(cfg_path.read_text(encoding="utf-8")))


def slugify(model: str) -> str:
    return model.replace("/", "__").replace(":", "-")
