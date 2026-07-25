"""
Engineering case study renderer.
"""

from .shared import load_yaml
from .list_renderer import render_list
from .gallery import render_gallery
from .project_sidebar import render_project_sidebar
from .project_timeline import render_project_timeline
from .related_projects import render_related_projects
from .project_navigation import render_project_navigation
from .project_summary import render_project_summary
from .statistical_gallery import render_statistical_gallery
from .spatial_gallery import render_spatial_gallery
from .downloads import render_downloads
from .video_gallery import render_video_gallery


def render_engineering_case_study(project_name):
    """
    Render a complete engineering case study.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    project = data.get("project", {})
    metrics = project.get("metrics", {})

    hero = project.get(
    "hero_image",
    f"media/engineering/{project_name}/images/hero.jpg"
    )

    html = f"""

<section
    class="project-hero"
    style="background-image:url('{hero}')">

    <div class="project-hero-overlay">

        <div class="project-hero-content">

            <span class="project-category">

                {project.get("category","Engineering")}

            </span>

            <h1>

                {project.get("title","")}

            </h1>

            <p class="hero-subtitle">

                {project.get("subtitle","")}

            </p>

            <div class="hero-meta">

                <span>📍 {project.get("location","")}</span>

                <span>🏢 {project.get("institution","")}</span>

                <span>📅 {project.get("duration","")}</span>

            </div>

        </div>

    </div>

</section>


<section class="project-metrics">

    <div class="metric-card">
        <h3>{metrics.get("duration", "")}</h3>
        <p>Project Duration</p>
    </div>

    <div class="metric-card">
        <h3>{metrics.get("software", "")}</h3>
        <p>Software Used</p>
    </div>

    <div class="metric-card">
        <h3>{metrics.get("workflow_steps", "")}</h3>
        <p>Workflow Steps</p>
    </div>

    <div class="metric-card">
        <h3>{metrics.get("deliverables", "")}</h3>
        <p>Deliverable</p>
    </div>

</section>

<section>

    <h2>Project Facts</h2>

    <div class="project-facts">

        <div class="fact">

            <strong>Project Type</strong>

            <span>{project.get("project_type","")}</span>

        </div>

        <div class="fact">

            <strong>Institution</strong>

            <span>{project.get("institution","")}</span>

        </div>

        <div class="fact">

            <strong>Supervisor</strong>

            <span>{project.get("supervisor","")}</span>

        </div>

        <div class="fact">

            <strong>Location</strong>

            <span>{project.get("location","")}</span>

        </div>

        <div class="fact">

            <strong>Laboratory</strong>

            <span>{project.get("laboratory","")}</span>

        </div>

        <div class="fact">

            <strong>Duration</strong>

            <span>{project.get("duration","")}</span>

        </div>

        <div class="fact">

            <strong>Status</strong>

            <span>{project.get("status","")}</span>

        </div>

        <div class="fact">

            <strong>Client</strong>

            <span>{project.get("client","")}</span>

        </div>

    </div>

</section>

<section class="project-layout">

    <div class="project-main">

        <h2>Executive Summary</h2>

        <p>
            {data.get("overview", "")}
        </p>

    </div>

    {render_project_sidebar(project)}

</section>

<section>

    <h2>Project Objectives</h2>

    {render_list(data.get("objectives", []))}

</section>

<section>

    <h2>Study Area</h2>

    <p>
        {data.get("study_area", "")}
    </p>

</section>

<section>

    <h2>Methodology</h2>

    {render_list(data.get("methodology", []))}

</section>

<section>

    <h2>Engineering Workflow</h2>

{render_project_timeline(project_name)}

</section>

<section>

    <h2>Engineering Workflow Gallery</h2>

    {render_gallery(project_name)}

</section>

<section>

    <h2>Results</h2>

    {render_list(data.get("results", []))}

</section>

<section>

    <h2>Lessons Learned</h2>

    {render_list(data.get("lessons", []))}

</section>

<section>

    <h2>Software Used</h2>

    {render_list(project.get("software", []))}

</section>

<section>

    <h2>Technical Skills Demonstrated</h2>

    {render_list(project.get("skills", []))}

</section>

<section>

    <h2>References</h2>

    {render_list(data.get("references", []))}

</section>

<section>

    <h2>Project Report</h2>

    <a
        class="button primary"
        href="assets/downloads/engineering/Leapfrog_Report.pdf"
        download>

        Download Full Project Report

    </a>

</section>
"""

    html += render_statistical_gallery(project_name)

    html += render_spatial_gallery(project_name)

    html += render_project_summary(project)

    html += render_downloads(project_name)

    html += render_related_projects(project_name)

    html += render_project_navigation(project_name)


    html += render_video_gallery(project_name)

    return html