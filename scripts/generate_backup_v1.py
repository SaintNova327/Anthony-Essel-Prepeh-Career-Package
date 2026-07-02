"""
Career Package Document Generator
Anthony Essel Prepeh Career Package
"""

from pathlib import Path
from text_utils import remove_emojis

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"


def read_markdown(filename):
    """Read a markdown file from the data folder."""
    file_path = DATA_DIR / filename

    if not file_path.exists():
        print(f"⚠ Missing: {filename}")
        return ""

    return file_path.read_text(encoding="utf-8")


def write_markdown(filename, content):
    """Write a markdown file into docs."""
    output = DOCS_DIR / filename
    output.write_text(content, encoding="utf-8")


def generate_resume():

    print("Generating Resume...")

    sections = [
        "career_summary.md",
        "skills.md",
        "experience.md",
        "projects.md",
        "education.md",
        "certificates.md",
        "software.md",
        "memberships.md",
    ]

    resume = "# Anthony Essel Prepeh\n\n"

    for section in sections:

        text = read_markdown(section)

        text = remove_emojis(text)

        resume += text + "\n\n"

    write_markdown("resume.md", resume)

    print("✓ resume.md created")


def main():

    print("=" * 50)

    print("Career Package Generator")

    print("=" * 50)

    generate_resume()

    print()

    print("Generation complete.")


if __name__ == "__main__":
    main()