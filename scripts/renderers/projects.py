"""
Projects renderer.
"""

from .shared import load_yaml, load_component


def render_projects():

    data = load_yaml("projects.yml")

    if not data or "projects" not in data:
        return "<p>No projects available.</p>"

    template = load_component("project_card.html")

    html = ""

    for project in data["projects"]:

        tags = ""

        for tech in project["technologies"]:
            tags += f'<span class="tag">{tech}</span>'

        card = template

        card = card.replace(
            "{{ title }}",
            project["title"]
        )

        card = card.replace(
            "{{ description }}",
            project["description"]
        )

        card = card.replace(
            "{{ technologies }}",
            tags
        )

        card = card.replace(
            "{{ github }}",
            project["github"]
        )

        card = card.replace(
            "{{ demo }}",
            project["demo"]
        )

        html += card

    return html