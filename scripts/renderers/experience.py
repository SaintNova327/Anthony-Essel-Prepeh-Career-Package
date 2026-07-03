"""
Experience renderer.
"""

from .shared import load_yaml


def render_experience():

    data = load_yaml("experience.yml")

    if not data or "experience" not in data:
        return """
<div class="timeline">
    <p>No experience has been added yet.</p>
</div>
"""

    html = '<div class="timeline">'

    for item in data["experience"]:

        html += f"""
<div class="timeline-item">

    <div class="timeline-date">
        {item['period']}
    </div>

    <h3 class="timeline-title">
        {item['title']}
    </h3>

    <div class="timeline-company">
        {item['company']}
    </div>

    <p>
        {item['description']}
    </p>

</div>
"""

    html += "</div>"

    return html