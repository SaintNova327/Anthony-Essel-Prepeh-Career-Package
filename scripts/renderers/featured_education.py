"""
Featured education renderer.
"""

from .shared import load_yaml, load_component, render_component


"""
Featured education renderer.
"""

from .shared import (
    load_yaml,
    load_component,
    render_component,
)


def render_featured_education():
    """
    Render the featured education section
    for the homepage.
    """

    data = load_yaml("education.yml")

    education = data.get("education", [])[:2]

    if not education:
        return "<p>No education records available.</p>"

    template = load_component("timeline_item.html")

    html = '<div class="timeline">'

    for item in education:

        html += render_component(
            template,
            {
                "period": item.get("period", ""),
                "title": item.get("degree", ""),
                "organization": item.get("institution", ""),
                "location": item.get("location", ""),
                "type": "Education",
                "status": item.get("status", ""),
                "summary": item.get("description", ""),
                "responsibilities": "",
                "technologies": "",
            },
        )

    html += "</div>"

    return html