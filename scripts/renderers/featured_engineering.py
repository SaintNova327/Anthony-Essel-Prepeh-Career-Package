"""
Featured engineering renderer.
"""

from .shared import load_yaml


PROJECTS = [
    "leapfrog",
    "internship",
    "groundwater",
    "field_mapping",
]


def render_featured_engineering():

    html = '<div class="cards">'

    for project in PROJECTS:

        try:
            data = load_yaml(f"engineering/{project}.yml")
        except FileNotFoundError:
            continue

        item = data.get("project", {})

        html += f"""
<div class="card engineering-card">

    <img
        class="engineering-image"
        src="{item.get('hero_image', 'assets/images/placeholder.jpg')}"
        alt="{item.get('title', 'Engineering Project')}">

    <div class="engineering-content">

        <span class="project-status">

            {item.get("status","Completed")}

        </span>

        <h3>

            {item.get("title","Engineering Project")}

        </h3>

        <p>

            {item.get("overview","")[:170]}...

        </p>

        <div class="project-tags">

            <span class="tag">

                {item.get("category","Engineering")}

            </span>

        </div>

        <a
            class="button primary"
            href="{project}.html">

            View Case Study →

        </a>

    </div>

</div>
"""

    html += "</div>"

    return html