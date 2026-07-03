"""
Navigation renderer.
"""

from .shared import load_config


def render_navigation():
    """
    Generate the navigation menu from site_config.md.
    """

    config = load_config("site_config.md")

    navigation = config.get("navigation", [])

    html = "<ul>"

    for item in navigation:

        page = item.lower().replace(" ", "_")

        href = (
            "index.html"
            if page == "home"
            else f"{page}.html"
        )

        html += (
            f'<li><a href="{href}">{item}</a></li>'
        )

    html += "</ul>"

    return html