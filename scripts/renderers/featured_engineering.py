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
    """
    Render featured engineering project cards.
    """

    html = '<div class="cards">'

    for project in PROJECTS:

        try:
            data = load_yaml(f"engineering/{project}.yml")
        except FileNotFoundError:
            continue

        item = data.get("project", {})

        image = item.get(
            "hero_image",
            f"media/engineering/{project}/images/hero.jpg"
        )

        html += f"""
<div class="card engineering-card">

    <img
        class="engineering-image"
        src="{image}"
        alt="{item.get('title', 'Engineering Project')}">

    <div class="engineering-content">

        <span class="project-status">
            {item.get('status', 'Completed')}
        </span>

        <div class="project-status">

            {item.get("status","Completed")}

        </div>

        <h3>{item.get('title', 'Untitled Project')}</h3>

        <p>
        {item.get('overview', 'Project description coming soon.')[:170]}...
        </p>

        <div class="project-tags">

            <span class="tag">
            {item.get('category','Engineering')}
            </span>

            <span class="tag">
            {item.get('project_type','Engineering')}
            </span>

            </div>

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