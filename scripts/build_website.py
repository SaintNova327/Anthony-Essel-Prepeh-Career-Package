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

def load_data(filename):
    """
    Read a markdown file from the data directory.
    """

    data_dir = PROJECT_ROOT / "data"

    file_path = data_dir / filename

    if not file_path.exists():
        return f"## Missing File\n\n{filename} was not found."

    return file_path.read_text(encoding="utf-8")


def markdown_to_html(markdown_text):
    """
    Convert Markdown text to HTML.
    """

    return markdown.markdown(markdown_text)
    
def load_template(filename):
    return (TEMPLATES / filename).read_text(encoding="utf-8")

def render_template(template_name, replacements):
    """
    Replace placeholders in an HTML template.
    """

    html = load_template(template_name)

    for key, value in replacements.items():

        html = html.replace(f"{{{{ {key} }}}}", value)

    return html


def save_page(filename, content):
    (WEBSITE / filename).write_text(content, encoding="utf-8")


def build_homepage():

    print("Building homepage...")

    base = load_template("base.html")
    header = load_template("header.html")
    footer = load_template("footer.html")
    summary = load_data("career_summary.md")

    summary = markdown_to_html(
        load_data("career_summary.md")
    )

    skills = markdown_to_html(
        load_data("skills.md")
    )

    projects = markdown_to_html(
        load_data("projects.md")
    )
    
    content = render_template(
        "home.html",
    {
        "name": "Anthony Essel Prepeh",
        "profession": "Geological Engineer",
        "tagline": "Mining Technology • Artificial Intelligence • Data Analysis",
        "career_summary": summary,
        "skills": skills,
        "projects": projects
    }
    )

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