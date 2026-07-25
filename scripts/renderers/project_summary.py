"""
Engineering project summary renderer.
"""


def render_project_summary(project):

    software = project.get("software", [])
    skills = project.get("skills", [])

    html = """
<section class="project-summary">

    <div class="summary-column">

        <h2>Software Used</h2>

        <div class="project-tags">
"""

    for item in software:

        html += f"""
<span class="tag">{item}</span>
"""

    html += """
        </div>

    </div>

    <div class="summary-column">

        <h2>Technical Skills</h2>

        <div class="project-tags">
"""

    for item in skills:

        html += f"""
<span class="tag">{item}</span>
"""

    html += """
        </div>

    </div>

</section>
"""

    return html