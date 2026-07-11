"""
Project Portfolio builder.
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


# ==========================================================
# Portfolio Builder
# ==========================================================

TITLE = (
    "Anthony Essel Prepeh\n"
    "Engineering Project Portfolio"
)

SOURCE = "projects_portfolio.md"

OUTPUT = "Anthony_Essel_Prepeh_Project_Portfolio.docx"


def build():
    """
    Build the engineering project portfolio.
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