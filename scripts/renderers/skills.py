"""
Skills renderer.
"""


def render_skills():

    categories = {

        "Geological Engineering": [
            "Geological Mapping",
            "Engineering Geology",
            "Mineral Exploration",
        ],

        "Hydrogeology": [
            "Hydrogeology",
            "Groundwater Development",
        ],

        "Geospatial": [
            "GIS",
            "Remote Sensing",
        ],

        "Digital": [
            "Python",
            "Git",
            "GitHub",
        ],

        "Professional": [
            "Technical Report Writing",
            "Data Interpretation",
        ],

    }

    html = ""

    for category, skills in categories.items():

        html += f"""
<div class="skill-group">

    <h3>{category}</h3>

    <div class="project-tags">
"""

        for skill in skills:
            html += f'<span class="tag">{skill}</span>'

        html += """
    </div>

</div>
"""

    return html