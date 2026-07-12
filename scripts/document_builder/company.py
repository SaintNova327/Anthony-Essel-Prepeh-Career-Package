"""
Company information loader.
"""

from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

COMPANIES = PROJECT_ROOT / "data" / "companies"


def load_company(filename):
    """
    Load a company YAML file.

    Example:
        load_company("anglogold_ashanti.yml")
    """

    path = COMPANIES / filename

    if not path.exists():
        raise FileNotFoundError(
            f"Company file not found: {path}"
        )

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as f:

        return yaml.safe_load(f)["company"]