"""
Cover Page builder.
"""

from .shared import (
    load_markdown,
    save_document,
)

from .styling import create_document

from .parser import render_markdown


TITLE = "Career Portfolio"

SOURCE = "cover_page.md"

OUTPUT = "Anthony_Essel_Prepeh_Cover_Page.docx"


def build():
    """
    Build the professional cover page.
    """

    document = create_document(TITLE)

    markdown = load_markdown(SOURCE)

    render_markdown(
        document,
        markdown,
    )

    save_document(
        document,
        OUTPUT,
    )