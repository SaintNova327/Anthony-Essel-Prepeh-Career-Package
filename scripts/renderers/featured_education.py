"""
Featured education renderer.
"""

from .shared import load_yaml, load_component, render_component


def render_featured_education():

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
                "date": item["period"],
                "title": item["degree"],
                "company": item["institution"],
                "description": item["description"],
            },
        )

    html += "</div>"

    return html