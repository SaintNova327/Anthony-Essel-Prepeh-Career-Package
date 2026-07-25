"""
Spatial distribution maps renderer.
"""

from .shared import load_yaml


def render_spatial_gallery(project_name):
    """
    Render spatial distribution maps.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    maps = data.get("spatial_maps", [])

    if not maps:
        return ""

    html = """
<section>

    <h2>Spatial Distribution Maps</h2>

    <p class="section-intro">

        Spatial interpolation maps showing the distribution of heavy
        metals and pollution indices across the study area.

    </p>

    <div class="workflow-gallery">
"""

    for item in maps:

        image = (
            f"media/engineering/"
            f"{project_name}/maps/"
            f"{item.get('image','')}"
        )

        html += f"""
<div class="gallery-card">

    <a
        href="{image}"
        class="lightbox"
        title="{item.get('title','')}">

        <img
            src="{image}"
            alt="{item.get('title','')}"
            loading="lazy">

    </a>

    <div class="engineering-content">

        <h3>{item.get('title','')}</h3>

        <p>{item.get('caption','')}</p>

    </div>

</div>
"""

    html += """
    </div>

</section>
"""

    return html