"""
Engineering gallery renderer.
"""

from .shared import load_yaml


def render_gallery(project_name):

    data = load_yaml(f"engineering/{project_name}.yml")

    gallery = data.get("gallery", [])

    if not gallery:

        return "<p>No gallery available for this project.</p>"

    html = '<div class="gallery-grid">'

    for image in gallery:

       html += f"""
<div class="gallery-card">

    <a
        href="media/engineering/{project_name}/images/{image.get('image','')}"
        class="lightbox">

        <img
            src="media/engineering/{project_name}/images/{image.get('image','')}"
            alt="{image.get('title','')}"
            class="lightbox-image"
            loading="lazy">

    </a>

    <div class="gallery-content">

        <h3>Step {image.get('step','')}: {image.get('title','')}</h3>

        <p>{image.get('caption','')}</p>

    </div>

</div>
"""
    html += "</div>"

    return html