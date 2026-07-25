"""
Engineering project sidebar.
"""


def render_project_sidebar(project):

    return f"""
<aside class="project-sidebar">

    <h3>Project Details</h3>

    <ul>

        <li><strong>Project</strong><br>{project.get("project_type","")}</li>

        <li><strong>Institution</strong><br>{project.get("institution","")}</li>

        <li><strong>Location</strong><br>{project.get("location","")}</li>

        <li><strong>Laboratory</strong><br>{project.get("laboratory","")}</li>

        <li><strong>Supervisor</strong><br>{project.get("supervisor","")}</li>

        <li><strong>Duration</strong><br>{project.get("duration","")}</li>

        <li><strong>Status</strong><br>{project.get("status","")}</li>

    </ul>

</aside>
"""