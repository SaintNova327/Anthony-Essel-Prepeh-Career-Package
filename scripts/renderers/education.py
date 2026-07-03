"""
Education renderer.
"""

from .shared import load_yaml


def render_education():

    data = load_yaml("education.yml")

    if not data or "education" not in data:
        return """
<div class="timeline">
    <p>No education records available.</p>
</div>
"""

    html = '<div class="timeline">'

    for item in data["education"]:

        html += f"""
<div class="timeline-item">

    <div class="timeline-date">
        {item["period"]}
    </div>

    <h3 class="timeline-title">
        {item["degree"]}
    </h3>

    <div class="timeline-company">
        {item["institution"]}
    </div>

    <p>
        {item["description"]}
    </p>

</div>
"""

    html += "</div>"

    return html