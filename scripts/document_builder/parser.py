"""
Markdown parser for DOCX documents.
"""

import re

from .styling import (
    add_bullet,
    add_divider,
    add_heading,
    add_paragraph,
)


# ==========================================================
# Helpers
# ==========================================================

def clean_inline(text):
    """
    Remove simple Markdown formatting.
    """

    text = text.replace("**", "")
    text = text.replace("__", "")
    text = text.replace("*", "")
    text = text.replace("_", "")
    text = text.replace("`", "")

    return text


def is_numbered(line):
    """
    Check if a line starts with a numbered list.
    """

    return re.match(r"^\d+\.\s", line) is not None


# ==========================================================
# Markdown Renderer
# ==========================================================

def render_markdown(document, markdown):
    """
    Render Markdown into a DOCX document.
    """

    lines = markdown.splitlines()

    in_code = False

    for line in lines:

        line = line.rstrip()

        # --------------------------------------------------
        # Blank line
        # --------------------------------------------------

        if not line.strip():

            continue

        # --------------------------------------------------
        # Code blocks
        # --------------------------------------------------

        if line.startswith("```"):

            in_code = not in_code

            continue

        if in_code:

            add_paragraph(
                document,
                line,
            )

            continue

        line = line.strip()

        # --------------------------------------------------
        # Horizontal Rule
        # --------------------------------------------------

        if line in (
            "---",
            "***",
            "___",
        ):

            add_divider(document)

            continue

        # --------------------------------------------------
        # Heading 1
        # --------------------------------------------------

        if line.startswith("# "):

            add_heading(
                document,
                clean_inline(line[2:]),
                level=1,
            )

            continue

        # --------------------------------------------------
        # Heading 2
        # --------------------------------------------------

        if line.startswith("## "):

            add_heading(
                document,
                clean_inline(line[3:]),
                level=2,
            )

            continue

        # --------------------------------------------------
        # Heading 3
        # --------------------------------------------------

        if line.startswith("### "):

            add_heading(
                document,
                clean_inline(line[4:]),
                level=3,
            )

            continue

        # --------------------------------------------------
        # Heading 4
        # --------------------------------------------------

        if line.startswith("#### "):

            add_heading(
                document,
                clean_inline(line[5:]),
                level=3,
            )

            continue

        # --------------------------------------------------
        # Bullet Lists
        # --------------------------------------------------

        if line.startswith("- "):

            add_bullet(
                document,
                clean_inline(line[2:]),
            )

            continue

        # --------------------------------------------------
        # Alternate Bullet
        # --------------------------------------------------

        if line.startswith("* "):

            add_bullet(
                document,
                clean_inline(line[2:]),
            )

            continue

        # --------------------------------------------------
        # Numbered Lists
        # --------------------------------------------------

        if is_numbered(line):

            text = re.sub(
                r"^\d+\.\s",
                "",
                line,
            )

            paragraph = document.add_paragraph(
                style="List Number"
            )

            paragraph.add_run(
                clean_inline(text)
            )

            continue

        # --------------------------------------------------
        # Block Quotes
        # --------------------------------------------------

        if line.startswith(">"):

            add_paragraph(
                document,
                clean_inline(
                    line[1:].strip()
                ),
            )

            continue

        # --------------------------------------------------
        # Standalone Bold Heading
        # --------------------------------------------------

        if (
            line.startswith("**")
            and line.endswith("**")
            and line.count("**") == 2
        ):

            add_heading(
                document,
                clean_inline(line),
                level=2,
            )

            continue

        # --------------------------------------------------
        # Markdown Links
        # --------------------------------------------------

        line = re.sub(
            r"\[(.*?)\]\((.*?)\)",
            r"\1 (\2)",
            line,
        )

        # --------------------------------------------------
        # Normal Paragraph
        # --------------------------------------------------

        add_paragraph(
            document,
            clean_inline(line),
        )