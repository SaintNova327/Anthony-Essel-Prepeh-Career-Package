"""
Certificate renderer.
"""

from .shared import (
    load_yaml,
    load_component,
    render_component,
)


def render_certificates():

    data = load_yaml("certificates.yml")

    certificates = data.get("certificates", [])

    if not certificates:

        return """
<div class="cards">
    <p>No certificates available.</p>
</div>
"""

    template = load_component(
        "certificate_card.html"
    )

    html = ""

    for cert in certificates:

        card = render_component(
            template,
            {
                "title": cert["title"],
                "provider": cert["provider"],
                "year": str(cert["year"]),
                "category": cert["category"],
                "status": cert["status"],
                "credential": cert["credential"],
            },
        )

        html += card

    return f'<div class="cards">{html}</div>'