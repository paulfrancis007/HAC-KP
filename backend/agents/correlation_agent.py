"""Link related messages, contacts, and behavioral patterns."""

from typing import Any


def run(parsed: dict[str, Any], entities: dict[str, Any]) -> dict[str, Any]:
    """Return sample correlation graph data (Gemini integration pending)."""
    _ = (parsed, entities)

    return {
        "nodes": [
            {"id": "maya", "label": "Maya Patel", "group": "person", "size": 28},
            {"id": "jordan", "label": "Jordan Blake", "group": "person", "size": 22},
            {"id": "alex", "label": "Alex Chen", "group": "person", "size": 12},
            {"id": "riverside", "label": "Riverside Community Center", "group": "location", "size": 8},
            {"id": "snapchat", "label": "Snapchat (j_blake88)", "group": "platform", "size": 10},
            {"id": "secrecy", "label": "Secrecy Requests", "group": "behavior", "size": 14},
            {"id": "meeting", "label": "Solo Meeting", "group": "behavior", "size": 12},
        ],
        "edges": [
            {"source": "jordan", "target": "maya", "label": "direct messaging", "weight": 22},
            {"source": "jordan", "target": "secrecy", "label": "requests concealment", "weight": 5},
            {"source": "jordan", "target": "meeting", "label": "proposes solo meet", "weight": 4},
            {"source": "jordan", "target": "riverside", "label": "names location", "weight": 3},
            {"source": "jordan", "target": "snapchat", "label": "redirects off-platform", "weight": 4},
            {"source": "maya", "target": "secrecy", "label": "reluctant compliance", "weight": 2},
            {"source": "alex", "target": "maya", "label": "peer support", "weight": 12},
        ],
        "patterns": [
            {
                "title": "Isolation from trusted peers",
                "detail": "Jordan instructs Maya not to inform Alex or school friends.",
                "severity": "High",
            },
            {
                "title": "Platform migration",
                "detail": "Progression from WhatsApp to suggested Snapchat with alias handle.",
                "severity": "High",
            },
            {
                "title": "Dual narrative",
                "detail": "Legitimate school activity (art club) used as cover for private contact.",
                "severity": "Medium",
            },
        ],
    }
