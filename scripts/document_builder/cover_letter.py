"""
Cover Letter builder.
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
# Cover Letter Builder
# ==========================================================

TITLE = (
    "Anthony Essel Prepeh\n"
    "Professional Cover Letter"
)

SOURCE = "cover_letter.md"

OUTPUT = "Anthony_Essel_Prepeh_Cover_Letter.docx"


def build():
    """
    Build the professional cover letter.
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