"""
Education renderer.
"""

from .shared import (
    load_yaml,
    load_component,
    render_component,
)


def render_education():

    data = load_yaml("education.yml")

    if not data or "education" not in data:
        return """
<div class="timeline">
    <p>No education records available.</p>
</div>
"""

    template = load_component("education_card.html")

    html = '<div class="timeline">'

    for item in data["education"]:

        highlights = ""

        for highlight in item["highlights"]:
            highlights += f"<li>{highlight}</li>"

        projects = ""

        for project in item["projects"]:
            projects += f"<li>{project}</li>"

        software = ""

        for tool in item["software"]:
            software += f'<span class="tag">{tool}</span>'

        memberships = ""

        for membership in item["memberships"]:
            memberships += f"<li>{membership}</li>"

        card = render_component(
            template,
            {
                "period": item["period"],
                "title": item["degree"],
                "organization": item["institution"],
                "location": item["location"],
                "type": item["level"],
                "status": item["status"],
                "summary": item["description"],
                "responsibilities": highlights,
                "technologies": software,
                "projects": projects,
                "memberships": memberships,
            },
        )

        html += card

    html += "</div>"

    return html