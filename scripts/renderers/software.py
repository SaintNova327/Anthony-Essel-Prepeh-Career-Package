"""
Software renderer.
"""


def render_software():

    software = {

        "Programming": [
            "Python",
            "HTML",
            "CSS",
            "JavaScript",
            "Markdown",
        ],

        "Version Control": [
            "Git",
            "GitHub",
            "GitHub Desktop",
        ],

        "Development Tools": [
            "Visual Studio Code",
            "Pandoc",
            "Windows Command Line",
        ],

        "Engineering Software": [
            "ArcGIS Pro",
            "QGIS",
            "Leapfrog Geo",
            "RockWorks",
            "MODFLOW",
            "Surfer",
        ],

        "Artificial Intelligence": [
            "ChatGPT",
            "GitHub Copilot",
            "Codex",
        ],

        "Productivity": [
            "Microsoft Word",
            "Microsoft Excel",
            "Microsoft PowerPoint",
            "Microsoft Outlook",
        ],

    }

    html = ""

    for category, items in software.items():

        html += f"""
<div class="skill-group">

    <h3>{category}</h3>

    <div class="project-tags">
"""

        for item in items:

            html += f'<span class="tag">{item}</span>'

        html += """
    </div>

</div>
"""

    return html