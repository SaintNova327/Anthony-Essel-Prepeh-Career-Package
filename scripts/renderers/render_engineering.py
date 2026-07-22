"""
Engineering project renderer.
"""

from .shared import load_yaml


def render_engineering(project_name):
    """
    Load an engineering project.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    return data.get("project", {})