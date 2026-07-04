"""
Navigation renderer.
"""

from .shared import load_config


def render_navigation(current_page="index.html"):
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

        css_class = ""

        if href == current_page:
            css_class = ' class="active"'

        html += (
            f'<li><a href="{href}"{css_class}>{item}</a></li>'
        )

    html += "</ul>"

    return html