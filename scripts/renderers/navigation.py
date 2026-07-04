"""
Navigation renderer.
"""

from .shared import load_config


def render_navigation(current_page="index.html"):
    """
    Generate the navigation menu and highlight
    the current page.
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

        css = ""

        if href == current_page:
            css = ' class="active"'

        html += (
            f'<li><a{css} href="{href}">{item}</a></li>'
        )

    html += "</ul>"

    return html