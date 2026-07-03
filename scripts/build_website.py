"""
Website Builder
Generates the portfolio website from layouts and career data.
"""

from pathlib import Path
from functools import lru_cache
from renderers import render_experience
from renderers import (
    render_experience,
    render_education,
    render_certificates,
    render_projects,
    render_featured_projects
)

import markdown
import yaml

# ==========================================================
# Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

WEBSITE = PROJECT_ROOT / "website"
LAYOUTS = WEBSITE / "layouts"

DATA = PROJECT_ROOT / "data"

CONFIG = PROJECT_ROOT / "config"

# ==========================================================
# Pages
# ==========================================================

PAGES = [

    {
        "output": "index.html",
        "layout": "home.html",
        "title": "Anthony Essel Prepeh | Portfolio"
    },

    {
        "output": "about.html",
        "layout": "about.html",
        "title": "About | Anthony Essel Prepeh"
    },

    {
        "output": "projects.html",
        "layout": "projects.html",
        "title": "Projects | Anthony Essel Prepeh"
    },

    {
        "output": "experience.html",
        "layout": "experience.html",
        "title": "Experience | Anthony Essel Prepeh"
    },

    {
        "output": "education.html",
        "layout": "education.html",
        "title": "Education | Anthony Essel Prepeh"
    },

    {
        "output": "certificates.html",
        "layout": "certificates.html",
        "title": "Certificates | Anthony Essel Prepeh"
    },


]






# ==========================================================
# Configuration
# ==========================================================

@lru_cache(maxsize=1)
def load_site_config():

    config_file = CONFIG / "site_config.md"

    with open(config_file, "r", encoding="utf-8") as f:

        return yaml.safe_load(f)

# ==========================================================
# Helpers
# ==========================================================

def load_layout(filename):

    return (LAYOUTS / filename).read_text(
        encoding="utf-8"
    )

def load_component(filename):
    """
    Load a reusable HTML component.
    """

    components = WEBSITE / "components"

    return (components / filename).read_text(
        encoding="utf-8"
    )

def load_career_database():
    """
    Load all Markdown files from the data directory.
    Returns a dictionary where the filename (without .md)
    becomes the key.
    """

    database = {}

    for file in DATA.glob("*.md"):

        key = file.stem

        markdown_text = file.read_text(
            encoding="utf-8"
        )

        database[key] = markdown.markdown(
            markdown_text
        )

    return database

def load_data(filename):

    file = DATA / filename

    if not file.exists():

        return f"# Missing File\n\n{filename} was not found."

    return file.read_text(
        encoding="utf-8"
    )


def markdown_to_html(text):

    return markdown.markdown(text)


def render_layout(layout_name, replacements):

    html = load_layout(layout_name)

    for key, value in replacements.items():

        html = html.replace(
            "{{ " + key + " }}",
            value
        )

    return html


def save_page(filename, html):

    (WEBSITE / filename).write_text(
        html,
        encoding="utf-8"
    )

# ==========================================================
# Builder
# ==========================================================

def build_page(page):

    print(f"Building {page['output']}...")

    config = load_site_config()

    author = config["author"]

    site = config["site"]

    career = load_career_database()

    header = load_layout("header.html")

    footer = load_layout("footer.html")

    body = render_layout(
    page["layout"],
    {
        "name": author["name"],
        "profession": author["profession"],
        "tagline": site["tagline"],
        "career_summary": career["career_summary"],
        "skills": career["skills"],
        "projects": career["projects"],
        "experience": render_experience(),
        "education": render_education(),
        "certificates": render_certificates(),
        "projects": render_projects(),
        "featured_projects": render_featured_projects(),
    }
)

    page_html = load_layout("base.html")

    page_html = page_html.replace(
        "{{ title }}",
        page["title"],
    )

    page_html = page_html.replace(
        "{{ header }}",
        header,
    )

    page_html = page_html.replace(
        "{{ content }}",
        body,
    )

    page_html = page_html.replace(
        "{{ footer }}",
        footer,
    )

    save_page(
        page["output"],
        page_html,
    )

    print(f"✓ {page['output']} generated")

# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("Career Website Generator")
    print("=" * 60)

    for page in PAGES:

        build_page(page)

    print()
    print("Website generation complete.")


if __name__ == "__main__":
    main()