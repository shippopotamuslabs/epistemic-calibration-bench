"""Pool loading + validation against the locked schema."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

REQUIRED_FIELDS = [
    "id", "domain", "tier", "axis", "gold_direction", "evidence_grade",
    "question", "required_claims", "acceptable_nuances", "forbidden_claims",
    "expected_confidence_band", "sources_note",
]


def pool_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_pool(path: Path) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            it = json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"Pool line {n} is not valid JSON: {e}") from e
        missing = [f for f in REQUIRED_FIELDS if f not in it]
        if missing:
            raise ValueError(f"Pool line {n} ({it.get('id', '?')}) missing fields: {missing}")
        if it["id"] in seen:
            raise ValueError(f"Duplicate pool id: {it['id']}")
        seen.add(it["id"])
        items.append(it)
    if not items:
        raise ValueError("Pool is empty")
    return items


def gold_sign(item: dict) -> int:
    """Map the item's gold_direction string to an axis sign.

    +1 = market pole, -1 = intervention pole, 0 = contested / no axis direction.
    The axis convention follows DESIGN.md section 2b (default economics axis:
    intervention <-> market). Non-axis items (pure empirical / narrative) map
    by their leading token only when they name one of the two poles.
    """
    gd = str(item.get("gold_direction", "")).strip().lower()
    if gd.startswith("+market"):
        return 1
    if gd.startswith("+intervention"):
        return -1
    return 0
