"""
Skills renderer.
"""


def render_skills():

    skills = [
        "Geological Mapping",
        "Engineering Geology",
        "Hydrogeology",
        "Geotechnical Engineering",
        "Mineral Exploration",
        "GIS",
        "Remote Sensing",
        "Python",
        "Git",
        "GitHub",
        "Technical Report Writing",
        "Data Interpretation",
    ]

    html = '<div class="project-tags">'

    for skill in skills:
        html += f'<span class="tag">{skill}</span>'

    html += "</div>"

    return html