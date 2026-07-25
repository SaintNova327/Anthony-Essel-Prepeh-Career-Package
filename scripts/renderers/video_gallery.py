"""
Engineering video gallery renderer.
"""

from .shared import load_yaml


def render_video_gallery(project_name):
    """
    Render project videos.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    videos = data.get("videos", [])

    if not videos:
        return ""

    html = """
<section>

    <h2>Project Videos</h2>

    <div class="video-gallery">
"""

    for video in videos:

        path = (
            f"media/engineering/"
            f"{project_name}/videos/"
            f"{video.get('file','')}"
        )

        html += f"""
<div class="video-card">

    <video
        controls
        preload="metadata"
        class="project-video">

        <source
            src="{path}"
            type="video/mp4">

        Your browser does not support HTML5 video.

    </video>

    <div class="gallery-content">

        <h3>{video.get('title','')}</h3>

        <p>{video.get('caption','')}</p>

    </div>

</div>
"""

    html += """
    </div>

</section>
"""

    return html