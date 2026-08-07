"""Produce an investigator-ready narrative summary."""

from typing import Any


def run(
    parsed: dict[str, Any],
    entities: dict[str, Any],
    correlations: dict[str, Any],
    timeline: list[dict[str, Any]],
) -> dict[str, Any]:
    """Return sample investigation summary (Gemini integration pending)."""
    _ = (parsed, entities, correlations, timeline)

    return {
        "risk_level": "High",
        "confidence": "Sample output — pending Gemini integration",
        "summary": (
            "Analysis of the exported WhatsApp conversation identifies a pattern of "
            "concerning contact between Maya Patel (minor) and Jordan Blake (unverified "
            "identity). Over a four-day period, Blake escalates from a purported school "
            "club invitation to requests for secrecy, message deletion, off-platform "
            "communication via Snapchat, and a proposed in-person meeting at Riverside "
            "Community Center. Peer contact with Alex Chen appears benign and contrasts "
            "sharply with Blake's behavior."
        ),
        "key_findings": [
            "Repeated instructions to conceal communication from parents and peers",
            "Suggestion to migrate to Snapchat under alias j_blake88",
            "Proposed solo in-person meeting with specific location and identification cue (blue backpack)",
            "Emotional grooming language ('I look out for people who get me')",
            "Maya shows hesitation but has not fully disengaged",
        ],
        "recommended_actions": [
            "Verify Jordan Blake's identity and connection to school art club",
            "Preserve full chat export and metadata before any deletion",
            "Interview Maya in a supportive, non-leading manner",
            "Check for Snapchat account j_blake88 and cross-reference handles",
            "Coordinate with school regarding Mr. Ellis reference",
        ],
    }
