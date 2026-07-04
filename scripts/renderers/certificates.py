"""
Certificate renderer.
"""



from .shared import load_yaml, load_component


def render_certificates():

    data = load_yaml("certificates.yml")

    template = load_component("certificate_card.html")

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

        card = template

        card = card.replace(
            "{{ title }}",
            cert["title"]
        )

        card = card.replace(
            "{{ issuer }}",
            cert["issuer"]
        )

        card = card.replace(
            "{{ year }}",
            str(cert["year"])
        )

        card = card.replace(
            "{{ description }}",
            cert["description"]
        )
        
        html += card

    html += "</div>"

    return html