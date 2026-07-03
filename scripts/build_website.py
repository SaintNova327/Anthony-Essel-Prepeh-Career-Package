"""
Website Builder
Builds website pages from reusable templates.
"""

from pathlib import Path
import markdown

PAGES = [

    {
        "output": "index.html",
        "layout": "home.html",
        "title": "Anthony Essel Prepeh | Portfolio"
    },

]

PROJECT_ROOT = Path(__file__).resolve().parent.parent

WEBSITE = PROJECT_ROOT / "website"
LAYOUTS = WEBSITE / "layouts"
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
    
def load_layout(filename):
    return (LAYOUTS / filename).read_text(
        encoding="utf-8"
    )

def render_template(layout_name, replacements):

    html = load_layout(layout_name)

    for key, value in replacements.items():

        html = html.replace(
            f"{{{{ {key} }}}}",
            value
        )

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

    for page in PAGES:

    build_page(page)

    print()
    print("Website generation complete.")

def build_page(page):

    print(f"Building {page['output']}...")

    base = load_layout("base.html")

    header = load_layout("header.html")

    footer = load_layout("footer.html")

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
        page["layout"],
        {
            "name": "Anthony Essel Prepeh",
            "profession": "Geological Engineer",
            "tagline": "Mining Technology • Artificial Intelligence • Data Analysis",
            "career_summary": summary,
            "skills": skills,
            "projects": projects
        }
    )

    html = base

    html = html.replace(
        "{{ title }}",
        page["title"]
    )

    html = html.replace(
        "{{ header }}",
        header
    )

    html = html.replace(
        "{{ content }}",
        content
    )

    html = html.replace(
        "{{ footer }}",
        footer
    )

    save_page(
        page["output"],
        html
    )

    print(f"✓ {page['output']} generated")

if __name__ == "__main__":
    main()