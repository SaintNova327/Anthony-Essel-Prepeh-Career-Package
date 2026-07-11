"""
Hero renderer.
"""

from .shared import load_component


def render_hero():
    """
    Render the homepage hero section.
    """

    return load_component("hero.html")