"""
Universal list renderer.

Renders any YAML list as an HTML unordered list.
"""


def render_list(items):

    if not items:
        return ""

    html = '<ul class="engineering-list">'

    for item in items:

        html += f"<li>{item}</li>"

    html += "</ul>"

    return html