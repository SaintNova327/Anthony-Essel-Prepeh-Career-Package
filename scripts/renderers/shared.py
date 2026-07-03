"""
Shared rendering utilities.
"""

from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def load_yaml(filename):

    path = PROJECT_ROOT / "data" / filename

    with open(path, "r", encoding="utf-8") as f:

        data = yaml.safe_load(f)

    return data or {}


def load_component(name):
    """
    Load a reusable HTML component.
    """

    path = (
        PROJECT_ROOT
        / "website"
        / "components"
        / name
    )

    return path.read_text(encoding="utf-8")