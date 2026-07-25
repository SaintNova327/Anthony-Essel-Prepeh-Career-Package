"""
Downloads renderer.
"""

from pathlib import Path

from .shared import load_yaml


def file_icon(filename):

    ext = Path(filename).suffix.lower()

    icons = {
        ".pdf": "📄",
        ".xlsx": "📊",
        ".xls": "📊",
        ".csv": "📈",
        ".ppt": "📽️",
        ".pptx": "📽️",
        ".jpg": "🖼️",
        ".jpeg": "🖼️",
        ".png": "🖼️",
        ".mp4": "🎥",
        ".zip": "🗜️",
    }

    return icons.get(ext, "📁")


"""
Downloads renderer.
"""

from .shared import load_yaml


def render_downloads(project_name):
    """
    Render downloadable project resources.
    """

    data = load_yaml(f"engineering/{project_name}.yml")

    downloads = data.get("downloads", [])

    if not downloads:
        return ""

    html = """
<section>

    <h2>Project Downloads</h2>

    <p class="section-intro">

        Download reports, datasets, presentations and project resources.

    </p>

    <div class="downloads-grid">
"""

    icons = {
        "pdf": "📄",
        "ppt": "📊",
        "pptx": "📊",
        "xlsx": "📈",
        "xls": "📈",
        "csv": "📋",
        "zip": "🗜️",
        "jpg": "🖼️",
        "jpeg": "🖼️",
        "png": "🖼️",
        "mp4": "🎥",
        "doc": "📝",
        "docx": "📝"
    }

    for item in downloads:

        file = item.get("file", "")

        extension = file.split(".")[-1].lower()

        icon = icons.get(extension, "📁")

        html += f"""
<div class="download-card">

    <div class="download-icon">

        {icon}

    </div>

    <h3>{item.get('title','')}</h3>

    <p>{item.get('description','')}</p>

    <a
        class="button primary"
        href="{file}"
        download>

        Download

    </a>

</div>
"""

    html += """
    </div>

</section>
"""

    return html