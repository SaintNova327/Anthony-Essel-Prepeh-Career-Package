"""
Curriculum Vitae builder.
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
    "Curriculum Vitae"
)

SOURCE = "curriculum_vitae.md"

OUTPUT = "Anthony_Essel_Prepeh_CV.docx"


def build():
    """
    Build the Curriculum Vitae.
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