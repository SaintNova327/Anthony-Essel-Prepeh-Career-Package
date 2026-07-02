from jinja2 import Template
import os

DATA_PATH = "../data"
TEMPLATE_PATH = "../templates"
OUTPUT_PATH = "../docs"

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def render_template(template_file, context):
    template_content = load_file(os.path.join(TEMPLATE_PATH, template_file))
    template = Template(template_content)
    return template.render(context)

def save_output(filename, content):
    with open(os.path.join(OUTPUT_PATH, filename), "w", encoding="utf-8") as f:
        f.write(content)

def main():
    context = {
        "name": "YOUR NAME",
        "career_summary": load_file(f"{DATA_PATH}/career_summary.md"),
        "skills": load_file(f"{DATA_PATH}/skills.md"),
        "software": load_file(f"{DATA_PATH}/software.md"),
        "projects": load_file(f"{DATA_PATH}/projects.md"),
        "experience": load_file(f"{DATA_PATH}/experience.md"),
        "education": load_file(f"{DATA_PATH}/education.md"),
        "certificates": load_file(f"{DATA_PATH}/certificates.md"),
        "memberships": load_file(f"{DATA_PATH}/memberships.md")
    }

    # Generate Resume
    resume = render_template("resume.template.md", context)
    save_output("resume.md", resume)

    # Generate ATS Resume
    ats = render_template("ats.template.md", context)
    save_output("ats_resume.md", ats)

    # Generate Website Content
    website = render_template("website.template.md", context)
    save_output("website.md", website)

if __name__ == "__main__":
    main()