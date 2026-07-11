"""
Featured experience renderer.
"""

from .shared import (
    load_yaml,
    load_component,
    render_component,
)


def render_featured_experience():

    data = load_yaml("experience.yml")

    experience = data.get("experience", [])[:2]

    if not experience:
        return "<p>No experience available.</p>"

    template = load_component("timeline_item.html")

    html = '<div class="timeline">'

    for item in experience:

        responsibilities = ""

        for responsibility in item["responsibilities"]:
            responsibilities += (
                f"<li>{responsibility}</li>"
            )

        technologies = ""

        for technology in item["technologies"]:
            technologies += (
                f'<span class="tag">{technology}</span>'
            )

        html += render_component(
            template,
            {
                "period": item["period"],
                "title": item["title"],
                "organization": item["organization"],
                "location": item["location"],
                "type": item["type"],
                "status": item["status"],
                "summary": item["summary"],
                "responsibilities": responsibilities,
                "technologies": technologies,
            },
        )

    html += "</div>"

    return html