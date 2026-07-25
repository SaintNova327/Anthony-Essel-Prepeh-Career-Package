"""
Website Builder
Generates the portfolio website from layouts and career data.
"""

from pathlib import Path
from functools import lru_cache
from renderers import (
    render_experience,
    render_education,
    render_certificates,
    render_projects,
    render_featured_projects,
    render_navigation,
    render_markdown,
    render_career_summary,
    render_skills,
    render_page_header,
    render_software,
    render_featured_experience,
    render_featured_education,
    render_footer,
)

from renderers.featured_engineering import (
    render_featured_engineering,
)

from renderers.featured_photography import (
    render_featured_photography,
)

from renderers.value_proposition import (
    render_value_proposition,
)

from renderers.engineering_case_study import (
    render_engineering_case_study,
)

import markdown
import yaml
from functools import lru_cache
from renderers.hero import render_hero
import shutil

# ==========================================================
# Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

WEBSITE = PROJECT_ROOT / "website"
LAYOUTS = WEBSITE / "layouts"

DATA = PROJECT_ROOT / "data"

CONFIG = PROJECT_ROOT / "config"

REQUIRED_DATA_FILES = [
    "career_summary.md",
    "skills.md",
    "projects.md",
    "experience.md",
    "education.md",
    "certificates.md",
    "software.md",
]

@lru_cache(maxsize=1)
def load_site_config():

    config_file = PROJECT_ROOT / "config" / "site_config.md"

    with open(
        config_file,
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)

# ==========================================================
# Pages
# ==========================================================

PAGES = [

    {
        "output": "index.html",
        "layout": "home.html",
        "title": "Anthony Essel Prepeh | Portfolio",
        "subtitle": "Geological Engineer • Mining Technology • Artificial Intelligence",
    },

    {
        "output": "about.html",
        "layout": "about.html",
        "title": "About | Anthony Essel Prepeh",
        "subtitle": "Learn more about my background and career goals",
    },

    {
        "output": "projects.html",
        "layout": "projects.html",
        "title": "Projects | Anthony Essel Prepeh",
        "subtitle": "Academic, engineering and software projects",
    },

    {
        "output": "engineering.html",
        "layout": "engineering.html",
        "title": "Engineering | Anthony Essel Prepeh",
        "subtitle": "Geological Engineering Portfolio",
    },

    {
        "output": "leapfrog.html",
        "layout": "engineering_project.html",
        "title": "Orebody Modelling using Leapfrog Geo",
        "subtitle": "Engineering Case Study",
    },

    {
        "output": "groundwater.html",
        "layout": "engineering_project.html",
        "title": "Groundwater Heavy Metal Analysis",
        "subtitle": "Engineering Case Study",
    },

    {
        "output": "internship.html",
        "layout": "engineering_project.html",
        "title": "Industrial Internship",
        "subtitle": "Engineering Case Study",
    }, 

    {
        "output": "field_mapping.html",
        "layout": "engineering_project.html",
        "title": "Field Mapping",
        "subtitle": "Engineering Case Study",
    },

    {
        "output": "experience.html",
        "layout": "experience.html",
        "title": "Experience | Anthony Essel Prepeh",
        "subtitle": "Professional and practical experience",
    },

    {
        "output": "education.html",
        "layout": "education.html",
        "title": "Education | Anthony Essel Prepeh",
        "subtitle": "Academic background and qualifications",
    },

    {
        "output": "certificates.html",
        "layout": "certificates.html",
        "title": "Certificates | Anthony Essel Prepeh",
        "subtitle": "Professional certifications and continuous learning",
    },
    
    {
        "output": "contact.html",
        "layout": "contact.html",
        "title": "Contact | Anthony Essel Prepeh",
        "subtitle": "Let's connect",
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
# Copy Engineering Media
# ==========================================================

def copy_engineering_media():
    """
    Copy engineering media from the media folder into the website assets folder.
    """

    source = PROJECT_ROOT / "media" / "engineering"

    destination = (
        WEBSITE
        / "assets"
        / "images"
        / "engineering"
    )

    if not source.exists():

        print("No engineering media folder found.")

        return

    destination.mkdir(
        parents=True,
        exist_ok=True,
    )

    projects = [

        "leapfrog",
        "internship",
        "groundwater",
        "field_mapping",

    ]

    for project in projects:

        source_images = source / project / "images"

        destination_images = destination / project

        if not source_images.exists():

            continue

        destination_images.mkdir(
            parents=True,
            exist_ok=True,
        )

        for image in source_images.iterdir():

            if image.is_file():

                shutil.copy2(
                    image,
                    destination_images / image.name,
                )

    print("✓ Engineering media copied")

def validate_build():
    """
    Validate that all required data files exist.
    """

    print("\nChecking project files...")

    data_dir = PROJECT_ROOT / "data"

    missing = []

    for filename in REQUIRED_DATA_FILES:

        path = data_dir / filename

        if path.exists():
            print(f"  ✓ {filename}")
        else:
            print(f"  ✗ {filename}")
            missing.append(filename)

    if missing:

        print("\nBuild cancelled.")
        print("Missing required files:")

        for filename in missing:
            print(f" - {filename}")

        return False

    print("All required files found.\n")

    return True

# ==========================================================
# Builder
# ==========================================================

def build_context():
    """
    Build the shared template context for all website pages.
    """

    config = load_site_config()

    author = config["author"]
    site = config["site"]

    career = load_career_database()

    return {

        "name": author["name"],
        "profession": author["profession"],
        "tagline": site["tagline"],

        "email": author["email"],
        "phone": author["phone"],
        "location": author["location"],
        "github": author["github"],
        "linkedin": author["linkedin"],
        "portfolio_video": author["portfolio_video"],

        "career_summary": render_career_summary(),
        "skills": render_skills(),
        "software": render_software(),

        "experience": render_experience(),
        "education": render_education(),
        "certificates": render_certificates(),
        "projects": render_projects(),
        "featured_projects": render_featured_projects(),
        "engineering_projects": render_featured_engineering(),
       
    
        "page_header": render_page_header(
            "Welcome",
            "Professional Geological Engineering Portfolio",
        ),
        "featured_experience": render_featured_experience(),
        "featured_education": render_featured_education(),
        "footer": render_footer(),
        "hero": render_hero(),
        "value_proposition": render_value_proposition(),

        "featured_photography": render_featured_photography(),

    }

def build_page(page):

    print(f"Building {page['output']}...")

    # Build the page context first
    context = build_context()
    context["current_page"] = page["output"]

    # Create a page-specific header
    context["page_header"] = render_page_header(
        page["title"].split("|")[0].strip(),
        page["subtitle"],
    )

    context["navigation"] = render_navigation(
        page["output"]
    )

    context["current_page"] = page["output"]

    context["navigation"] = render_navigation(
        page["output"]
    )

    # Check that the page layout exists
    layout_path = LAYOUTS / page["layout"]

    if not layout_path.exists():
        print(f"✗ Missing layout: {page['layout']}")
        return

    # Load base template
    base = load_layout("base.html")

    # Render header and footer with context
    header = render_layout(
        "header.html",
        context,
    )

    footer = render_layout(
        "footer.html",
        context,
    )

    # Render page body
    body = render_layout(
        page["layout"],
        context,
    )

    if page["output"] == "leapfrog.html":

        body = body.replace(
            "{{ project_content }}",
            render_engineering_case_study("leapfrog"),
        )

    elif page["output"] == "groundwater.html":

        body = body.replace(
            "{{ project_content }}",
            render_engineering_case_study("groundwater"),
        )

    elif page["output"] == "internship.html":

        body = body.replace(
            "{{ project_content }}",
            render_engineering_case_study("internship"),
        )

    elif page["output"] == "field_mapping.html":

        body = body.replace(
            "{{ project_content }}",
            render_engineering_case_study("field_mapping"),
        )

    # Assemble the final HTML
    page_html = base

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

    config = load_site_config()
    
    author = config["author"]

    print("=" * 60)
    print("Career Website Generator")
    print("=" * 60)

    if not validate_build():
        return

    print("Starting website generation...\n")

    copy_engineering_media()

    for page in PAGES:
        build_page(page)

    print("\nWebsite generation complete.")


if __name__ == "__main__":
    main()