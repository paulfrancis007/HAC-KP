"""Safe parsing and repair of LLM JSON responses."""

import json
import re
from typing import Any

ENTITY_SCHEMA_KEYS = (
    "people",
    "locations",
    "dates",
    "phones",
    "emails",
    "objects",
    "events",
)

EMPTY_ENTITY_RESULT: dict[str, list] = {key: [] for key in ENTITY_SCHEMA_KEYS}


def parse_entity_json(raw_text: str) -> dict[str, Any]:
    """Parse Gemini output into the strict entity JSON schema."""
    if not raw_text or not raw_text.strip():
        return dict(EMPTY_ENTITY_RESULT)

    candidates = [
        raw_text.strip(),
        _extract_fenced_json(raw_text),
        _extract_object_json(raw_text),
    ]

    for candidate in candidates:
        if not candidate:
            continue
        for attempt in (candidate, _repair_json(candidate)):
            try:
                parsed = json.loads(attempt)
                if isinstance(parsed, dict):
                    return _normalize_entity_schema(parsed)
            except json.JSONDecodeError:
                continue

    return dict(EMPTY_ENTITY_RESULT)


def _extract_fenced_json(text: str) -> str:
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def _extract_object_json(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return ""
    return text[start : end + 1].strip()


def _repair_json(text: str) -> str:
    repaired = text.strip()
    repaired = repaired.replace("“", '"').replace("”", '"').replace("'", '"')
    repaired = re.sub(r",\s*([}\]])", r"\1", repaired)
    repaired = re.sub(r"\bNone\b", "null", repaired)
    repaired = re.sub(r"\bTrue\b", "true", repaired)
    repaired = re.sub(r"\bFalse\b", "false", repaired)
    return repaired


def _normalize_entity_schema(data: dict[str, Any]) -> dict[str, list]:
    normalized: dict[str, list] = {}
    for key in ENTITY_SCHEMA_KEYS:
        value = data.get(key, [])
        if not isinstance(value, list):
            value = [value] if value else []
        normalized[key] = [_stringify_item(item) for item in value if _stringify_item(item)]
    return normalized


def _stringify_item(item: Any) -> str:
    if isinstance(item, str):
        return item.strip()
    if isinstance(item, dict):
        for field in ("name", "value", "text", "label", "title", "event"):
            if field in item and str(item[field]).strip():
                return str(item[field]).strip()
        return json.dumps(item, ensure_ascii=False)
    if item is None:
        return ""
    return str(item).strip()
