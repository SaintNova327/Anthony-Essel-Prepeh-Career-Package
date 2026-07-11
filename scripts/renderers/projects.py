"""
Project renderer.
"""

from .shared import (
    load_yaml,
    load_component,
    render_component,
)


def render_projects():

    data = load_yaml("projects.yml")

    if not data or "projects" not in data:
        return "<p>No projects available.</p>"

    template = load_component("project_card.html")

    html = ""

    for project in data["projects"]:

        technologies = ""

        for tech in project["technologies"]:
            technologies += f'<span class="tag">{tech}</span>'

        skills = ""

        for skill in project["skills"]:
            skills += f'<span class="tag">{skill}</span>'

        github = project.get("github", "#")
        demo = project.get("demo", "#")

        card = render_component(

            template,

            {
                "title": project["title"],
                "category": project["category"],
                "status": project["status"],
                "description": project["description"],
                "objective": project["objective"],
                "technologies": technologies,
                "skills": skills,
                "github": github,
                "demo": demo,
                "image": project.get(
                    "image",
                    "assets/images/projects/placeholder.jpg",
                ),
            },

        )

        if github == "#":

            card = card.replace(
                'href="#"',
                'href="#" class="button primary disabled" onclick="return false;"',
                1,
            )

        if demo == "#":

            card = card.replace(
                'href="#"',
                'href="#" class="button secondary disabled" onclick="return false;"',
                1,
            )

        html += card

    return f'<div class="cards">{html}</div>'