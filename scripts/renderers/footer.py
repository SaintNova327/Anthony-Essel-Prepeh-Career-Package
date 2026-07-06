"""
Footer renderer.
"""

from .shared import load_config


def render_footer():
    """
    Generate the website footer from site_config.md.
    """

    config = load_config("site_config.md")

    footer = config["footer"]

    return f"""
<footer>

    <p>{footer["copyright"]}</p>

    <p>{footer["message"]}</p>

</footer>
"""