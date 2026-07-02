"""
Career Package Build System
Anthony Essel Prepeh Career Package

This script is the main entry point for generating all career documents.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

TEMPLATE_DIR = PROJECT_ROOT / "templates"

DOCS_DIR = PROJECT_ROOT / "docs"

EXPORTS_DIR = PROJECT_ROOT / "exports"

WEBSITE_DIR = PROJECT_ROOT / "website"


def create_folders():
    """
    Create required folders if they don't exist.
    """

    folders = [
        EXPORTS_DIR,
        EXPORTS_DIR / "pdf",
        EXPORTS_DIR / "docx",
        EXPORTS_DIR / "html",
        WEBSITE_DIR,
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)


def check_project():
    """
    Verify that the project structure exists.
    """

    required = [
        DATA_DIR,
        TEMPLATE_DIR,
        DOCS_DIR,
    ]

    for folder in required:

        if not folder.exists():

            raise FileNotFoundError(
                f"Missing required folder:\n{folder}"
            )


def main():

    print("=" * 60)

    print("Anthony Essel Prepeh Career Package")

    print("Career Build System")

    print("=" * 60)

    check_project()

    create_folders()

    print()

    print("✓ Project structure verified.")

    print("✓ Export folders ready.")

    print()

    print("Next phases will generate:")

    print(" • Resume")

    print(" • ATS Resume")

    print(" • Executive Resume")

    print(" • Academic CV")

    print(" • Cover Letters")

    print(" • Portfolio Website")

    print(" • PDF")

    print(" • DOCX")

    print()

    print("Build completed successfully.")


if __name__ == "__main__":
    main()