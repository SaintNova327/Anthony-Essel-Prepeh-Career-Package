"""
Website Builder
Builds website pages from reusable templates.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

WEBSITE = PROJECT_ROOT / "website"
TEMPLATES = WEBSITE / "templates"


def load_template(filename):
    return (TEMPLATES / filename).read_text(encoding="utf-8")


def save_page(filename, content):
    (WEBSITE / filename).write_text(content, encoding="utf-8")


def build_homepage():

    print("Building homepage...")

    base = load_template("base.html")
    header = load_template("header.html")
    footer = load_template("footer.html")

    content = """
<header class="hero">

<h1>Anthony Essel Prepeh</h1>

<h2>Geological Engineer</h2>

<p>
Mining Technology • Artificial Intelligence • Data Analysis
</p>

<div class="hero-buttons">

<a class="button primary" href="#">Download Resume</a>

<a class="button secondary" href="projects.html">
View Projects
</a>

</div>

</header>

<section>

<h2>Professional Summary</h2>

<p>

Passionate Geological Engineer with interests in
mining technology, orebody evaluation,
artificial intelligence and data-driven decision making.

</p>

</section>

<section>

<h2>Core Competencies</h2>

<div class="skills">

<span>Geological Mapping</span>

<span>Orebody Evaluation</span>

<span>Leapfrog Geo</span>

<span>Python</span>

<span>Artificial Intelligence</span>

</div>

</section>
"""

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