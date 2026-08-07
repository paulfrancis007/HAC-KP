"""Reconstruct a chronological event sequence from chat analysis."""

from typing import Any


def run(parsed: dict[str, Any], correlations: dict[str, Any]) -> list[dict[str, Any]]:
    """Return sample timeline events (Gemini integration pending)."""
    _ = (parsed, correlations)

    return [
        {
            "date": "12/03/2026",
            "time": "16:41",
            "event": "Unknown contact Jordan Blake initiates conversation with Maya",
            "actor": "Jordan Blake",
            "severity": "Medium",
        },
        {
            "date": "12/03/2026",
            "time": "16:46",
            "event": "Jordan asks Maya not to tell parents about meetings",
            "actor": "Jordan Blake",
            "severity": "High",
        },
        {
            "date": "13/03/2026",
            "time": "09:07",
            "event": "Jordan requests message deletion after reading",
            "actor": "Jordan Blake",
            "severity": "High",
        },
        {
            "date": "13/03/2026",
            "time": "21:35",
            "event": "Jordan requests photo from Maya; Maya deflects",
            "actor": "Jordan Blake",
            "severity": "Medium",
        },
        {
            "date": "14/03/2026",
            "time": "08:25",
            "event": "Jordan proposes solo coffee meetup near Oak Street",
            "actor": "Jordan Blake",
            "severity": "High",
        },
        {
            "date": "14/03/2026",
            "time": "19:50",
            "event": "Jordan suggests Snapchat and provides handle j_blake88",
            "actor": "Jordan Blake",
            "severity": "High",
        },
        {
            "date": "15/03/2026",
            "time": "10:03",
            "event": "Meeting confirmed at Riverside Community Center back entrance",
            "actor": "Jordan Blake",
            "severity": "Critical",
        },
    ]
