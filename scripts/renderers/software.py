"""
Software renderer.
"""

from .markdown import render_markdown


def render_software():
    """
    Render software.md as HTML.
    """
    return render_markdown("software.md")