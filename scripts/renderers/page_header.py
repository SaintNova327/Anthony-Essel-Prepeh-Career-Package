"""
Page header renderer.
"""

from .shared import (
    load_component,
    render_component,
)


def render_page_header(title, subtitle):

    template = load_component(
        "page_header.html"
    )

    return render_component(
        template,
        {
            "title": title,
            "subtitle": subtitle,
        },
    )