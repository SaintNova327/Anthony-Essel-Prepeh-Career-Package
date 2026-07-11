"""
Experience renderer.
"""

from .shared import (
    load_yaml,
    load_component,
    render_component,
)


def render_experience():

    data = load_yaml("experience.yml")

    if not data or "experience" not in data:
        return """
<div class="timeline">
    <p>No experience has been added yet.</p>
</div>
"""

    template = load_component("timeline_item.html")

    html = '<div class="timeline">'

    for item in data["experience"]:

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

        card = render_component(
            template,
            {
                "title": item["title"],
                "organization": item["organization"],
                "location": item["location"],
                "period": item["period"],
                "type": item["type"],
                "status": item["status"],
                "summary": item["summary"],
                "responsibilities": responsibilities,
                "technologies": technologies,
            },
        )

        html += card

    html += "</div>"

    return html