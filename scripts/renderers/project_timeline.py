"""
Engineering project timeline renderer.
"""

from .shared import load_yaml


def render_project_timeline(project_name):
    """
    Render the engineering workflow as a professional timeline.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    workflow = data.get("workflow", [])

    if not workflow:
        return """
<div class="timeline-empty">

    <p>No workflow available.</p>

</div>
"""

    html = """
<div class="project-timeline">
"""

    for number, step in enumerate(workflow, start=1):

        html += f"""
<div class="timeline-step">

    <div class="timeline-number">

        {number}

    </div>

    <div class="timeline-content">

        <h3>Step {number}</h3>

        <p>{step}</p>

    </div>

</div>
"""

    html += """
</div>
"""

    return html