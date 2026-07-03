from .shared import load_yaml


def render_featured_projects():

    data = load_yaml("projects.yml")

    projects = data.get("projects", [])

    featured = [p for p in projects if p.get("featured")]

    if not featured:
        return "<p>No featured projects yet.</p>"

    html = '<div class="cards">'

    for project in featured:

        tech = ""

        for t in project.get("technologies", []):
            tech += f'<span class="tag">{t}</span>'

        html += f"""
<div class="card">

    <h3>{project['title']}</h3>

    <p>{project['description']}</p>

    <div>{tech}</div>

</div>
"""

    html += "</div>"

    return html