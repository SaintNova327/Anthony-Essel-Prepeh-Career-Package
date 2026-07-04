"""
Markdown renderer.
"""

from pathlib import Path
import markdown

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def render_markdown(
    filename,
    remove_sections=None,
):
    """
    Render a Markdown file as HTML.

    Parameters
    ----------
    filename : str
        Markdown file in the data directory.

    remove_sections : list[str], optional
        Section headings to remove before rendering.
    """

    path = PROJECT_ROOT / "data" / filename

    if not path.exists():
        return ""

    text = path.read_text(
        encoding="utf-8"
    )

    if remove_sections:

        lines = text.splitlines()

        filtered = []

        skip = False

        for line in lines:

            if line.startswith("#"):

                heading = line.lstrip("#").strip()

                if heading in remove_sections:
                    skip = True
                    continue

                skip = False

            if not skip:
                filtered.append(line)

        text = "\n".join(filtered)

    return markdown.markdown(
        text,
        extensions=["tables"],
    )