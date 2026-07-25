"""
Featured photography renderer.
"""

from .shared import load_yaml


def render_featured_photography():

    data = load_yaml("photography.yml")

    items = data.get("photography", [])

    html = '<div class="cards">'

    for item in items:

        html += f"""
<div class="card">

    <h3>{item['title']}</h3>

    <p>{item['category']}</p>

</div>
"""

    html += "</div>"

    return html