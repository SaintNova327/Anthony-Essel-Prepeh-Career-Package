"""
ATS Resume builder.
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
# Resume Builder
# ==========================================================

TITLE = (
    "Anthony Essel Prepeh\n"
    "Professional Resume"
)

SOURCE = "resume_ats.md"

OUTPUT = "Anthony_Essel_Prepeh_Resume.docx"


def build():
    """
    Build the professional ATS resume.
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