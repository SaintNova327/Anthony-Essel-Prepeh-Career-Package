"""
Resume Builder

Generates the HTML resume from the master resume.
"""

from pathlib import Path
from functools import lru_cache

import markdown
import yaml
import subprocess



PROJECT_ROOT = Path(__file__).resolve().parent.parent

CAREER = PROJECT_ROOT / "career_documents"

WEBSITE = PROJECT_ROOT / "website"

OUTPUT = WEBSITE / "assets" / "downloads"

@lru_cache(maxsize=1)
def load_site_config():
    """
    Load the site configuration.
    """

    config_file = PROJECT_ROOT / "config" / "site_config.md"

    with open(
        config_file,
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)

def build_pdf():

    print("Generating resume.pdf...")

    source = (
        PROJECT_ROOT
        / "career_documents"
        / "master_resume.md"
    )

    output = (
        PROJECT_ROOT
        / "website"
        / "assets"
        / "downloads"
        / "resume.pdf"
    )

    result = subprocess.run(

        [
            "pandoc",
            str(source),
            "-o",
            str(output),
            "--pdf-engine=xelatex",
        ]

    )

    if result.returncode != 0:

        raise RuntimeError(
            "PDF generation failed."
        )

    print("✓ resume.pdf generated")


def main():

    print("=" * 60)
    print("Resume Builder")
    print("=" * 60)

    source = CAREER / "master_resume.md"

    if not source.exists():

        print("✗ master_resume.md not found.")

        return

    config = load_site_config()

    author = config["author"]

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

    build_pdf()

    print(output)
    
   


if __name__ == "__main__":
    main()