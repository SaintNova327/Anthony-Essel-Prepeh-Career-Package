"""
Resume Builder

Generates the HTML resume from the master resume.
"""

from pathlib import Path

import markdown
import yaml
from functools import lru_cache
PROJECT_ROOT = Path(__file__).resolve().parent.parent

CAREER = PROJECT_ROOT / "career_documents"

WEBSITE = PROJECT_ROOT / "website"

OUTPUT = WEBSITE / "assets" / "downloads"


def main():

    print("=" * 60)
    print("Resume Builder")
    print("=" * 60)

    source = CAREER / "master_resume.md"

    if not source.exists():

        print("✗ master_resume.md not found.")

        return

    template = (
        WEBSITE
        / "layouts"
        / "resume.html"
    ).read_text(
        encoding="utf-8"
    )

    markdown_text = source.read_text(
        encoding="utf-8"
    )

    resume_html = markdown.markdown(
        markdown_text,
        extensions=["tables"]
    )

    template = template.replace(
        "{{ name }}",
        author["name"]
    )
    
    template = template.replace(
        "{{ profession }}",
        author["profession"]
    )

    template = template.replace(
        "{{ resume }}",
        resume_html
    )

    OUTPUT.mkdir(
        parents=True,
        exist_ok=True
    )

    output = OUTPUT / "resume.html"

    output.write_text(
        template,
        encoding="utf-8"
    )

    print("✓ resume.html generated")

    print(output)


if __name__ == "__main__":
    main()