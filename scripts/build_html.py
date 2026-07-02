from pathlib import Path
import markdown

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOCS = PROJECT_ROOT / "docs"

EXPORT = PROJECT_ROOT / "exports" / "html"

TEMPLATE = PROJECT_ROOT / "templates" / "html" / "resume.html"


EXPORT.mkdir(parents=True, exist_ok=True)


def main():

    resume = (DOCS / "resume.md").read_text(encoding="utf-8")

    html = markdown.markdown(resume)

    template = TEMPLATE.read_text(encoding="utf-8")

    html = template.replace("{{ content }}", html)

    (EXPORT / "resume.html").write_text(
        html,
        encoding="utf-8"
    )

    print("✓ HTML Resume created")


if __name__ == "__main__":
    main()