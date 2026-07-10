"""
Projects renderer.
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

        tags = ""

        for tech in project["technologies"]:
            tags += f'<span class="tag">{tech}</span>'

        github = project.get("github", "#")
        demo = project.get("demo", "#")

        card = render_component(
            template,
            {
                 "title": project["title"],
                 "status": project.get("status", "Active"),
                 "description": project["description"],
                 "technologies": tags,
                 "github": github,
                 "demo": demo,
            },
        )

        
        
        if github == "#":
            card = card.replace(
                ">View on GitHub<",
                ">Repository Coming Soon<"
            )

            card = card.replace(
                'href="#"',
                'href="#" class="button primary disabled" aria-disabled="true"'

            )
            
        if demo == "#":
            card = card.replace(
                ">Project Details<",
                ">Coming Soon<"
            )

            card = card.replace(
                'href="#"',
                'href="#" class="button secondary disabled" aria-disabled="true"',
                1
            )     

        html += card

    return f'<div class="cards">{html}</div>'