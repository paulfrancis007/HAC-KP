"""Read uploaded chat text and return its raw content."""

from typing import Any


def run(chat_text: str) -> dict[str, Any]:
    """Return the full text content of the uploaded file."""
    return {"content": chat_text}
