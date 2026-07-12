"""
Featured projects renderer.
"""

from .shared import load_yaml


def render_featured_projects():
    """
    Render featured projects for the homepage.
    """

    data = load_yaml("projects.yml")

    projects = data.get("projects", [])

    featured = [p for p in projects if p.get("featured")]

    if not featured:
        return "<p>No featured projects yet.</p>"

    html = '<div class="cards">'

    for project in featured:

        technologies = ""

        # Limit homepage to first 5 technologies
        for tech in project.get("technologies", [])[:5]:
            technologies += f'<span class="tag">{tech}</span>'

        html += f"""
<div class="card">

    <h3>📌 {project['title']}</h3>

    <p>{project['description']}</p>

    <div class="project-tags">
        {technologies}
    </div>

</div>
"""

    html += "</div>"

    return html