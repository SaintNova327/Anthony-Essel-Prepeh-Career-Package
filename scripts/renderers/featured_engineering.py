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
    Render engineering project cards.
    """

    html = '<div class="cards">'

    for project in PROJECTS:

        data = load_yaml(f"engineering/{project}.yml")

        item = data.get("project", {})

        html += f"""
<div class="card">

    <h3>{item.get('title', '')}</h3>

    <p>{item.get('overview', '')}</p>

    <a class="button primary" href="{project}.html">

        View Case Study

    </a>

</div>
"""

    html += "</div>"

    return html