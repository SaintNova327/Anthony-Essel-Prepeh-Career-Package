"""
Career Package Build System

Builds the complete career package:

1. Portfolio Website
2. DOCX Documents
3. PDF Documents
"""

from pathlib import Path
import subprocess
import sys

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = PROJECT_ROOT / "scripts"

BUILDERS = [
    "build_website.py",
    "build_docx.py",
    "build_pdf.py",
]


# ==========================================================
# Helpers
# ==========================================================

def print_banner():

    print("=" * 60)
    print("Anthony Essel Prepeh Career Package")
    print("Career Build System")
    print("=" * 60)


def verify_project():

    required = [
        PROJECT_ROOT / "career_documents",
        PROJECT_ROOT / "website",
        PROJECT_ROOT / "scripts",
        PROJECT_ROOT / "exports",
    ]

    print("\nChecking project structure...\n")

    missing = []

    for path in required:

        if path.exists():
            print(f"✓ {path.name}")
        else:
            print(f"✗ {path.name}")
            missing.append(path.name)

    if missing:

        print("\nMissing required directories:")

        for item in missing:
            print(f"  - {item}")

        return False

    return True


def ensure_output_directories():

    directories = [
        PROJECT_ROOT / "exports",
        PROJECT_ROOT / "exports" / "docx",
        PROJECT_ROOT / "exports" / "pdf",
    ]

    for directory in directories:

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    print("\n✓ Export directories ready.")


def run_builder(script):

    script_path = SCRIPTS / script

    print("\n" + "-" * 60)
    print(f"Running {script}")
    print("-" * 60 + "\n")

    result = subprocess.run(
        [sys.executable, str(script_path)]
    )

    if result.returncode != 0:

        raise RuntimeError(
            f"{script} failed."
        )

    print(f"\n✓ {script} completed successfully.")


# ==========================================================
# Main
# ==========================================================

def main():

    print_banner()

    if not verify_project():

        print("\nBuild cancelled.")

        return

    ensure_output_directories()

    print("\nStarting build pipeline...")

    try:

        for builder in BUILDERS:

            run_builder(builder)

    except Exception as error:

        print("\n" + "=" * 60)
        print("BUILD FAILED")
        print("=" * 60)
        print(error)

        sys.exit(1)

    print("\n" + "=" * 60)
    print("Career Package Build Completed Successfully")
    print("=" * 60)

    print("\nGenerated outputs:")

    print("\nWebsite")
    print("  website/")

    print("\nDOCX")
    print("  exports/docx/")

    print("\nPDF")
    print("  exports/pdf/")

    print("\nReady for applications.\n")


if __name__ == "__main__":
    main()