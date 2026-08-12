"""
Rock Slopes in Civil and Mining Engineering renderer.

Builds the specialized Rock Slopes engineering case-study page.
"""

from pathlib import Path
from html import escape

from .shared import load_yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]

WEBSITE = PROJECT_ROOT / "website"

MEDIA = WEBSITE / "media" / "engineering" / "rock_slopes"

def media_url(relative_path):
    """
    Convert a Rock Slopes media path into a website-relative URL.
    """

    return f"media/engineering/rock_slopes/{relative_path}"


def render_presentation_card(filename, title, description):
    """
    Render a PowerPoint presentation card with online viewing
    and direct download options.
    """

    url = media_url(filename)

    # Public GitHub Pages URL for the presentation.
    public_url = (
        "https://saintnova327.github.io/"
        "Anthony-Essel-Prepeh-Career-Package/"
        f"{url}"
    )

    # Encode the public URL for Microsoft Office Online Viewer.
    from urllib.parse import quote

    viewer_url = (
        "https://view.officeapps.live.com/op/view.aspx"
        f"?src={quote(public_url, safe='')}"
    )

    return f"""
    <article class="rock-resource-card presentation-card">

        <div class="resource-icon">
            PPT
        </div>

        <div class="resource-content">

            <h3>
                {escape(title)}
            </h3>

            <p>
                {escape(description)}
            </p>

            <div class="resource-actions">

                <a
                    class="button primary"
                    href="{viewer_url}"
                    target="_blank"
                    rel="noopener noreferrer">

                    View Presentation

                </a>

                <a
                    class="button secondary"
                    href="{url}"
                    download>

                    Download PPTX

                </a>

            </div>

        </div>

    </article>
    """

def render_video_card(filename, title, description):
    """
    Render an HTML5 engineering workflow video.
    """

    url = media_url(filename)

    return f"""
    <article class="rock-video-card">

        <div class="video-container">

            <video
                controls
                preload="metadata"
                playsinline>

                <source
                    src="{url}"
                    type="video/mp4">

                Your browser does not support HTML5 video.

            </video>

        </div>

        <div class="video-content">

            <h3>{escape(title)}</h3>

            <p>
                {escape(description)}
            </p>

        </div>

    </article>
    """


def render_gallery_card(filename, title, description):
    """
    Render an engineering analysis gallery image.
    """

    url = media_url(filename)

    return f"""
    <article class="rock-gallery-card">

        <a
            href="{url}"
            class="rock-gallery-link"
            data-lightbox="rock-slopes">

            <img
                src="{url}"
                alt="{escape(title)}"
                loading="lazy">

        </a>

        <div class="gallery-content">

            <h3>{escape(title)}</h3>

            <p>
                {escape(description)}
            </p>

        </div>

    </article>
    """


def render_pdf_card(filename, title, description):
    """
    Render a technical PDF resource.
    """

    url = media_url(filename)

    return f"""
    <article class="rock-resource-card pdf-card">

        <div class="resource-icon">
            PDF
        </div>

        <div class="resource-content">

            <h3>{escape(title)}</h3>

            <p>
                {escape(description)}
            </p>

            <div class="resource-actions">

                <a
                    class="button primary"
                    href="{url}"
                    target="_blank"
                    rel="noopener">

                    Read PDF

                </a>

                <a
                    class="button secondary"
                    href="{url}"
                    download>

                    Download PDF

                </a>

            </div>

        </div>

    </article>
    """


def render_rock_slopes(project_name="rock_slopes"):
    """
    Render the complete Rock Slopes engineering project.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    project = data.get("project", {})
    metrics = project.get("metrics", {})

    hero_image = project.get(
        "hero_image",
        "media/engineering/rock_slopes/images/hero.jpg",
    )

    html = f"""

<section
    class="project-hero rock-slopes-hero"
    style="background-image:url('{hero_image}')">

    <div class="project-hero-overlay">

        <div class="project-hero-content">

            <span class="project-category">
                {escape(project.get("category", "Engineering Experience"))}
            </span>

            <h1>
                {escape(project.get("title", ""))}
            </h1>

            <p class="hero-subtitle">
                {escape(project.get("subtitle", ""))}
            </p>

            <div class="hero-meta">

                <span>
                    📍 {escape(project.get("location", ""))}
                </span>

                <span>
                    🏢 {escape(project.get("institution", ""))}
                </span>

                <span>
                    📅 {escape(project.get("duration", ""))}
                </span>

            </div>

        </div>

    </div>

</section>


<section class="project-metrics">

    <div class="metric-card">

        <h3>
            {escape(str(metrics.get("duration", "")))}
        </h3>

        <p>
            Project Duration
        </p>

    </div>


    <div class="metric-card">

        <h3>
            {escape(str(metrics.get("software", "")))}
        </h3>

        <p>
            Software
        </p>

    </div>


    <div class="metric-card">

        <h3>
            {escape(str(metrics.get("workflow_steps", "")))}
        </h3>

        <p>
            Workflow
        </p>

    </div>


    <div class="metric-card">

        <h3>
            {escape(str(metrics.get("deliverables", "")))}
        </h3>

        <p>
            Deliverables
        </p>

    </div>

</section>


<section class="project-overview">

    <h2>
        Project Overview
    </h2>

    <p>
        {escape(data.get("overview", ""))}
    </p>

</section>


<section class="rock-section">

    <div class="section-heading">

        <span class="section-label">
            01
        </span>

        <h2>
            Tailings Dams
        </h2>

        <p>
            Technical presentations covering investigation, design,
            construction, monitoring and foundation considerations
            for tailings storage facilities.
        </p>

    </div>


    <div class="rock-resource-grid">

        {render_presentation_card(
            "presentations/tailings/1_Site_Investigations_for_tailings_storage_facilities.pptx",
            "Site Investigations for Tailings Storage Facilities",
            "Engineering considerations involved in investigating and characterizing sites for tailings storage facilities."
        )}

        {render_presentation_card(
            "presentations/tailings/2_Design_of_Tailings_storage_facilities.pptx",
            "Design of Tailings Storage Facilities",
            "Technical study of engineering principles and considerations for tailings storage facility design."
        )}

        {render_presentation_card(
            "presentations/tailings/3_Construction_of_tailings_dam.pptx",
            "Construction of Tailings Dam",
            "Presentation covering construction considerations and engineering practices for tailings dams."
        )}

        {render_presentation_card(
            "presentations/tailings/4_monitoring_tailings_dam.pptx",
            "Monitoring Tailings Dam",
            "Technical overview of monitoring requirements and engineering observations for tailings dams."
        )}

        {render_presentation_card(
            "presentations/tailings/5_foundation_on_rock.pptx",
            "Foundation on Rock",
            "Engineering considerations for foundations constructed on rock in tailings and civil engineering applications."
        )}

    </div>

</section>


<section class="rock-section">

    <div class="section-heading">

        <span class="section-label">
            02
        </span>

        <h2>
            Open-Pit Mine
        </h2>

        <p>
            Engineering studies related to water risks and slope
            failure mechanisms in open-pit mining environments.
        </p>

    </div>


    <div class="rock-resource-grid">

        {render_presentation_card(
            "presentations/open_pit/1_Mine_Water_Risk_Open_Pit_Slope_Stability.pptx",
            "Mine Water Risk and Open-Pit Slope Stability",
            "Study of mine water risks and their relationship with open-pit slope stability."
        )}

        {render_presentation_card(
            "presentations/open_pit/2_slope_failure_mechanism.pptx",
            "Slope Failure Mechanisms",
            "Technical presentation examining common mechanisms responsible for slope failure."
        )}

    </div>

</section>


<section class="rock-section">

    <div class="section-heading">

        <span class="section-label">
            03
        </span>

        <h2>
            Limit Equilibrium and Numerical Modelling of Slopes
        </h2>

        <p>
            Practical modelling workflows using Rocscience DIPS
            and Slide for slope stability assessment.
        </p>

    </div>


    <h3 class="rock-subheading">
        Rocscience DIPS — Workflow Demonstrations
    </h3>


    <div class="rock-video-grid">

        {render_video_card(
            "videos/dips/1_setup.mp4",
            "DIPS Setup",
            "Initial setup and preparation of the DIPS slope stability analysis workflow."
        )}

        {render_video_card(
            "videos/dips/2_Planar_Sliding.mp4",
            "Planar Sliding",
            "Kinematic analysis of potential planar sliding conditions."
        )}

        {render_video_card(
            "videos/dips/3_Wedge_Sliding.mp4",
            "Wedge Sliding",
            "Kinematic analysis of potential wedge sliding conditions."
        )}

    </div>


    <h3 class="rock-subheading">
        DIPS Analysis Gallery
    </h3>


    <div class="rock-gallery-grid">

        {render_gallery_card(
            "gallery/dips/1_planar_failure.jpg",
            "Planar Failure Analysis",
            "DIPS analysis illustrating planar failure conditions."
        )}

        {render_gallery_card(
            "gallery/dips/2_wedge_failure.jpg",
            "Wedge Failure Analysis",
            "DIPS analysis illustrating wedge failure conditions."
        )}

    </div>


    <h3 class="rock-subheading">
        Rocscience Slide — Slope Stability Analysis
    </h3>


    <div class="rock-video-grid">

        {render_video_card(
            "videos/slide/1_Slope_stability_analysis.mp4",
            "Slope Stability Analysis",
            "Slope stability modelling workflow using Rocscience Slide."
        )}

    </div>


    <h3 class="rock-subheading">
        Slide Analysis Gallery
    </h3>


    <div class="rock-gallery-grid">

        {render_gallery_card(
            "gallery/slide/1_factor_of_safety.jpg",
            "Factor of Safety",
            "Slope stability result illustrating the calculated factor of safety."
        )}

        {render_gallery_card(
            "gallery/slide/2_effect_of_groundwater.jpg",
            "Effect of Groundwater",
            "Analysis illustrating the influence of groundwater conditions on slope stability."
        )}

        {render_gallery_card(
            "gallery/slide/3_effect_of_seismic_loading.jpg",
            "Effect of Seismic Loading",
            "Analysis illustrating the influence of seismic loading on slope stability."
        )}

        {render_gallery_card(
            "gallery/slide/4_effect-of_constant-distributed_load.jpg",
            "Effect of Constant Distributed Load",
            "Analysis illustrating the influence of surface loading on slope stability."
        )}

    </div>

</section>


<section class="rock-section">

    <div class="section-heading">

        <span class="section-label">
            04
        </span>

        <h2>
            Technical Reading Materials
        </h2>

        <p>
            Selected technical references and software training
            materials provided for further engineering study.
        </p>

    </div>


    <div class="rock-resource-grid">

        {render_pdf_card(
            "pdfs/Practical-Rock-Engineering.pdf",
            "Practical Rock Engineering",
            "Technical reference material covering practical principles of rock engineering and slope stability."
        )}

        {render_pdf_card(
            "pdfs/Slide_TutorialManual.pdf",
            "Slide Tutorial Manual",
            "Tutorial reference for slope stability modelling using Rocscience Slide."
        )}

    </div>

</section>


<section class="rock-section rock-learning">

    <div class="section-heading">

        <span class="section-label">
            05
        </span>

        <h2>
            Engineering Skills Demonstrated
        </h2>

    </div>


    <div class="rock-skills-grid">

"""

    for skill in project.get("skills", []):

        html += f"""
        <div class="rock-skill">
            {escape(skill)}
        </div>
        """

    html += """

    </div>

</section>

"""

    return html
