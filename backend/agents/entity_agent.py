"""Extract structured entities from chat content using Google Gemini."""

from typing import Any

import google.generativeai as genai

from config import GEMINI_MODEL, require_gemini_api_key
from utils.json_repair import EMPTY_ENTITY_RESULT, parse_entity_json

ENTITY_PROMPT = """You are an investigative entity extraction assistant.

Extract entities from the chat transcript below.

Return ONLY valid JSON with exactly these keys:
- people
- locations
- dates
- phones
- emails
- objects
- events

Rules:
- Each value must be a JSON array of strings.
- Use empty arrays when nothing is found.
- Do not include markdown, code fences, or explanation.
- Extract only what is explicitly present or clearly implied in the text.

Example format:
{
  "people": ["Jane Doe"],
  "locations": ["Central Library"],
  "dates": ["12/03/2026"],
  "phones": [],
  "emails": [],
  "objects": ["blue backpack"],
  "events": ["Proposed meeting at community center"]
}

Chat transcript:
{chat_text}
"""


def run(parsed: dict[str, Any]) -> dict[str, Any]:
    """Extract entities via Gemini and return strict JSON-compatible data."""
    chat_text = parsed.get("content", "")
    if not chat_text.strip():
        return _ui_compatible_entities(dict(EMPTY_ENTITY_RESULT))

    api_key = require_gemini_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(GEMINI_MODEL)

    prompt = ENTITY_PROMPT.format(chat_text=chat_text)
    response = model.generate_content(prompt)
    raw_text = getattr(response, "text", "") or ""
    entities = parse_entity_json(raw_text)
    return _ui_compatible_entities(entities)


def _ui_compatible_entities(entities: dict[str, list[str]]) -> dict[str, Any]:
    """
    Keep the strict entity schema while shaping people/locations
    for the existing Streamlit UI (unchanged).
    """
    return {
        "people": [
            {"name": name, "role": "Extracted", "mentions": 0}
            for name in entities.get("people", [])
        ],
        "locations": [
            {"name": name, "context": "Extracted from chat"}
            for name in entities.get("locations", [])
        ],
        "dates": entities.get("dates", []),
        "phones": entities.get("phones", []),
        "emails": entities.get("emails", []),
        "objects": entities.get("objects", []),
        "events": entities.get("events", []),
        "platforms": [],
        "handles": [],
        "behavioral_flags": [],
    }
