"""
Statistical analysis gallery renderer.
"""

from .shared import load_yaml


def render_statistical_gallery(project_name):
    """
    Render statistical analysis figures.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    figures = data.get("statistical_figures", [])

    if not figures:
        return ""

    html = """
<section>

    <h2>Statistical Analysis</h2>

    <div class="workflow-gallery">
"""

    for fig in figures:

        image = (
            f"media/engineering/"
            f"{project_name}/figures/"
            f"{fig.get('image', '')}"
        )

        html += f"""
<div class="gallery-card">

    <a
        href="{image}"
        class="lightbox"
        title="{fig.get('title','')}">

        <img
            src="{image}"
            alt="{fig.get('title','')}"
            loading="lazy">

    </a>

    <div class="engineering-content">

        <h3>{fig.get('title','')}</h3>

        <p>{fig.get('caption','')}</p>

    </div>

</div>
"""

    html += """
    </div>

</section>
"""

    return html