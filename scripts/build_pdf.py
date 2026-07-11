"""
PDF Builder

Converts all generated DOCX documents into PDF files.
"""

from pathlib import Path
import sys

try:
    from docx2pdf import convert
except ImportError:
    print("\nERROR: docx2pdf is not installed.")
    print("Install it with:\n")
    print("    pip install docx2pdf\n")
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOCX_DIR = PROJECT_ROOT / "exports" / "docx"
PDF_DIR = PROJECT_ROOT / "exports" / "pdf"


def ensure_directories():
    """Create the PDF output directory."""

    PDF_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


def convert_documents():

    files = sorted(DOCX_DIR.glob("*.docx"))

    if not files:

        print("\nNo DOCX files found.")
        return

    print("=" * 60)
    print("PDF Builder")
    print("=" * 60)
    print()

    for file in files:

        output = PDF_DIR / f"{file.stem}.pdf"

        print(f"Converting {file.name}")

        try:

            convert(
                str(file),
                str(output),
            )

            print(f"✓ {output.name}")

        except Exception as e:

            print(f"✗ Failed: {file.name}")
            print(e)

    print()
    print("PDF generation complete.")


def main():

    ensure_directories()
    convert_documents()


if __name__ == "__main__":
    main()