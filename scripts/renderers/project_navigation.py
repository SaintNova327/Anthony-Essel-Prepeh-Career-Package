"""
Engineering project navigation renderer.
"""


def render_project_navigation(current_project):

    projects = [

        {
            "name": "leapfrog",
            "title": "Orebody Modelling using Leapfrog Geo",
            "page": "leapfrog.html"
        },

        {
            "name": "groundwater",
            "title": "Groundwater Quality Assessment",
            "page": "groundwater.html"
        },

        {
            "name": "internship",
            "title": "Industrial Internship",
            "page": "internship.html"
        },

        {
            "name": "field_mapping",
            "title": "Geological Field Mapping",
            "page": "field_mapping.html"
        }

    ]

    current_index = 0

    for i, project in enumerate(projects):
        if project["name"] == current_project:
            current_index = i
            break

    previous_project = (
        projects[current_index - 1]
        if current_index > 0
        else None
    )

    next_project = (
        projects[current_index + 1]
        if current_index < len(projects) - 1
        else None
    )

    html = """
<section class="project-navigation">
"""

    if previous_project:

        html += f"""
<a class="nav-card" href="{previous_project['page']}">

    <small>← Previous Project</small>

    <h3>{previous_project['title']}</h3>

</a>
"""

    else:

        html += "<div></div>"

    if next_project:

        html += f"""
<a class="nav-card nav-right" href="{next_project['page']}">

    <small>Next Project →</small>

    <h3>{next_project['title']}</h3>

</a>
"""

    else:

        html += "<div></div>"

    html += """
</section>
"""

    return html