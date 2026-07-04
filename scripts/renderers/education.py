"""
Education renderer.
"""


from .shared import load_yaml, load_component


def render_education():

    data = load_yaml("education.yml")

    template = load_component("timeline_item.html")

    if not data or "education" not in data:
        return """
<div class="timeline">
    <p>No education records available.</p>
</div>
"""

    html = '<div class="timeline">'

    for item in data["education"]:

        card = template

        card = card.replace(
            "{{ date }}",
            item["period"]
        )

        card = card.replace(
            "{{ title }}",
            item["degree"]
        )

        card = card.replace(
            "{{ company }}",
            item["institution"]
        )
        
        card = card.replace(
            "{{ description }}",
            item["description"]
        )
        
        html += card




    html += "</div>"

    return html