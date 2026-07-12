"""
References builder.
"""

from .shared import (
    load_markdown,
    save_document,
)

from .styling import (
    create_document,
)

from .parser import (
    render_markdown,
)

TITLE = (
    "Anthony Essel Prepeh\n"
    "Professional References"
)

SOURCE = "references.md"

OUTPUT = "Anthony_Essel_Prepeh_References.docx"


def build():
    """
    Build the professional references document.
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