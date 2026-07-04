"""
Experience renderer.
"""

from .shared import load_yaml, load_component


def render_experience():

    data = load_yaml("experience.yml")
    
    template = load_component("timeline_item.html")

    if not data or "experience" not in data:
        return """
<div class="timeline">
    <p>No experience has been added yet.</p>
</div>
"""

    html = '<div class="timeline">'

    for item in data["experience"]:

      card = template
      
      card = card.replace(
        "{{ date }}",
        item["period"]
    )
    
      card = card.replace(
        "{{ title }}",
        item["title"]
    )
    
      card = card.replace(
        "{{ company }}",
        item["company"]
    )
    
      card = card.replace(
        "{{ description }}",
        item["description"]
    )
    
    html += card

    html += "</div>"

    return html