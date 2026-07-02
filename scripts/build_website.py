"""
Website Builder
Builds website pages from reusable templates.
"""

from pathlib import Path
import markdown

PROJECT_ROOT = Path(__file__).resolve().parent.parent

WEBSITE = PROJECT_ROOT / "website"
TEMPLATES = WEBSITE / "templates"
CONTENT = WEBSITE / "content"

def load_content(filename):

    text = (CONTENT / filename).read_text(
        encoding="utf-8"
    )

    return markdown.markdown(text)

def load_template(filename):
    return (TEMPLATES / filename).read_text(encoding="utf-8")


def save_page(filename, content):
    (WEBSITE / filename).write_text(content, encoding="utf-8")


def build_homepage():

    print("Building homepage...")

    base = load_template("base.html")
    header = load_template("header.html")
    footer = load_template("footer.html")
    content = load_content("home.md")

    page = base

    page = page.replace("{{ title }}",
                        "Anthony Essel Prepeh | Portfolio")

    page = page.replace("{{ header }}",
                        header)

    page = page.replace("{{ content }}",
                        content)

    page = page.replace("{{ footer }}",
                        footer)

    save_page("index.html", page)

    print("✓ Homepage generated")


def main():

    print("=" * 50)
    print("Website Generator")
    print("=" * 50)

    build_homepage()

    print()
    print("Website generation complete.")


if __name__ == "__main__":
    main()