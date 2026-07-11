"""
Shared utilities for the DOCX document builder.
"""

from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

ROOT = Path(__file__).resolve().parents[2]

CAREER_DOCUMENTS = ROOT / "career_documents"

EXPORTS = ROOT / "exports"

DOCX_EXPORT = EXPORTS / "docx"

DOCX_EXPORT.mkdir(
    parents=True,
    exist_ok=True,
)


# ==========================================================
# Markdown
# ==========================================================

def load_markdown(filename):
    """
    Load a Markdown document.
    """

    path = CAREER_DOCUMENTS / filename

    if not path.exists():
        raise FileNotFoundError(
            f"Markdown file not found:\n{path}"
        )

    return path.read_text(
        encoding="utf-8"
    )


# ==========================================================
# Saving
# ==========================================================

def save_document(document, filename):
    """
    Save a DOCX document.
    """

    output = DOCX_EXPORT / filename

    document.save(output)

    print(f"✓ {filename} created")