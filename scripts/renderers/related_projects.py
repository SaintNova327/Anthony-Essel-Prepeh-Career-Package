"""
Related engineering projects renderer.
"""


def render_related_projects(current_project):

    projects = [
        {
            "name": "Leapfrog Geo Orebody Modelling",
            "page": "leapfrog.html",
            "image": "media/engineering/leapfrog/images/hero.jpg",
            "description": "3D geological modelling using Leapfrog Geo."
        },
        {
            "name": "Groundwater Assessment",
            "page": "groundwater.html",
            "image": "media/engineering/groundwater/images/hero.jpg",
            "description": "Heavy metal pollution assessment using Python and GIS."
        },
        {
            "name": "Industrial Internship",
            "page": "internship.html",
            "image": "media/engineering/internship/images/hero.jpg",
            "description": "Professional mining engineering experience."
        },
        {
            "name": "Field Geological Mapping",
            "page": "field_mapping.html",
            "image": "media/engineering/field_mapping/images/hero.jpg",
            "description": "Field mapping and structural geological interpretation."
        }
    ]

    html = """
<section>

    <h2>Related Engineering Projects</h2>

    <div class="related-projects-grid">
"""

    for project in projects:

        if project["page"] == f"{current_project}.html":
            continue

        html += f"""
<div class="related-card">

    <img
        src="{project['image']}"
        alt="{project['name']}">

    <div class="engineering-content">

        <h3>{project['name']}</h3>

        <p>{project['description']}</p>

        <a
            class="button secondary"
            href="{project['page']}">

            View Project

        </a>

    </div>

</div>
"""

    html += """
    </div>

</section>
"""

    return html