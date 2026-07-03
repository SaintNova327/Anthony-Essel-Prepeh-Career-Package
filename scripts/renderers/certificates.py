"""
Certificate renderer.
"""

from .shared import load_yaml


def render_certificates():

    data = load_yaml("certificates.yml")

    certificates = data.get("certificates", [])

    if not certificates:
        return """
<div class="cards">
    <h2>Professional Certificates</h2>
    <p>
        Certificates will be added here as they are earned.
        Current focus areas include Python, GIS, Remote Sensing,
        SQL, and Geological Engineering.
    </p>
</div>
"""

    html = '<div class="cards">'

    for cert in certificates:

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