"""
Career Package Build System
Anthony Essel Prepeh Career Package

This script is the main entry point for generating all career documents.
"""

from pathlib import Path
import subprocess
import sys


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

def run_builder(script):
    """
    Run a build script and stop if it fails.
    """

    print("-" * 60)
    print(f"Running {script}")
    print("-" * 60)

    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / script)]
    )

    if result.returncode != 0:

        raise RuntimeError(
            f"{script} failed."
        )

    print(f"✓ {script} completed.\n")

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

    print("Starting build pipeline...\n")

    run_builder("build_website.py")

    # Resume builder will be enabled next
    run_builder("build_resume.py")

    print("=" * 60)

    print("Career Package Complete")

    print("=" * 60)


if __name__ == "__main__":
    main()

