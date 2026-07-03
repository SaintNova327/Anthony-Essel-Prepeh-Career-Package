"""
Certificate renderer.
"""

from .shared import load_yaml


def render_certificates():

    data = load_yaml("certificates.yml")

    if not data or "certificates" not in data:
        return """
<div class="cards">
    <p>No certificates available.</p>
</div>
"""

    html = '<div class="cards">'

    for cert in data["certificates"]:

        html += f"""
<div class="card">

    <h3>{cert['title']}</h3>

    <p><strong>Issuer:</strong> {cert['issuer']}</p>

    <p><strong>Year:</strong> {cert['year']}</p>

    <p>{cert['description']}</p>

</div>
"""

    html += "</div>"

    return html