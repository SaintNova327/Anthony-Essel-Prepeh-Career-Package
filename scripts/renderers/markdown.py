"""
Markdown renderer.
"""

from pathlib import Path
import markdown

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def render_markdown(filename):

    path = PROJECT_ROOT / "data" / filename

    if not path.exists():
        return ""

    text = path.read_text(
        encoding="utf-8"
    )

    return markdown.markdown(
        text,
        extensions=["tables"]
    )