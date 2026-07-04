"""
Featured experience renderer.
"""

from .shared import load_yaml, load_component, render_component


def render_featured_experience():

    data = load_yaml("experience.yml")

    experience = data.get("experience", [])[:2]

    if not experience:
        return "<p>No experience available.</p>"

    template = load_component("timeline_item.html")

    html = '<div class="timeline">'

    for item in experience:

        html += render_component(
            template,
            {
                "date": item["period"],
                "title": item["title"],
                "company": item["company"],
                "description": item["description"],
            },
        )

    html += "</div>"

    return html