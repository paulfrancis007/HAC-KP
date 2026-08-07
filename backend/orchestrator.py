"""Coordinate the multi-agent investigation pipeline."""

import time
from typing import Any, Callable, Generator

from agents import (
    correlation_agent,
    entity_agent,
    summary_agent,
    text_agent,
    timeline_agent,
)

AGENT_STEPS: list[tuple[str, str, str]] = [
    ("text_agent", "Text Agent", "Parsing and normalizing chat export"),
    ("entity_agent", "Entity Agent", "Extracting people, locations, and handles"),
    ("correlation_agent", "Correlation Agent", "Linking behavioral patterns"),
    ("timeline_agent", "Timeline Agent", "Reconstructing event sequence"),
    ("summary_agent", "Summary Agent", "Generating investigation summary"),
]


def run_investigation(
    chat_text: str,
    *,
    simulate_delay: float = 0.6,
) -> Generator[dict[str, Any], None, None]:
    """
    Run every agent in sequence, yielding progress updates after each step.

    Yields dicts with keys: step_id, name, description, status, result (on complete).
    Final yield contains status='done' and the full aggregated results.
    """
    results: dict[str, Any] = {}

    for step_id, name, description in AGENT_STEPS:
        yield {
            "step_id": step_id,
            "name": name,
            "description": description,
            "status": "running",
        }

        if simulate_delay:
            time.sleep(simulate_delay)

        result = _run_agent(step_id, chat_text, results)
        results[step_id] = result

        yield {
            "step_id": step_id,
            "name": name,
            "description": description,
            "status": "complete",
            "result": result,
        }

    yield {
        "status": "done",
        "parsed": results["text_agent"],
        "entities": results["entity_agent"],
        "correlations": results["correlation_agent"],
        "timeline": results["timeline_agent"],
        "summary": results["summary_agent"],
    }


def _run_agent(step_id: str, chat_text: str, results: dict[str, Any]) -> Any:
    dispatch: dict[str, Callable[..., Any]] = {
        "text_agent": lambda: text_agent.run(chat_text),
        "entity_agent": lambda: entity_agent.run(results["text_agent"]),
        "correlation_agent": lambda: correlation_agent.run(
            results["text_agent"], results["entity_agent"]
        ),
        "timeline_agent": lambda: timeline_agent.run(
            results["text_agent"], results["correlation_agent"]
        ),
        "summary_agent": lambda: summary_agent.run(
            results["text_agent"],
            results["entity_agent"],
            results["correlation_agent"],
            results["timeline_agent"],
        ),
    }
    return dispatch[step_id]()
