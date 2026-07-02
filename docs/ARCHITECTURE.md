# Architecture

**Project:** Anthony Essel Prepeh Career Package

**Version:** 1.1

**Last Updated:** July 2026

---

# Purpose

This document describes the architecture of the Career Package project.

The goal is to maintain a **single source of truth** for career information while automatically generating professional documents, resumes, portfolio pages, and exports.

---

# Design Principles

The project follows these principles:

- Write information once.
- Generate everything automatically.
- Keep source files separate from generated files.
- Preserve completed work.
- Build in small, testable increments.
- Use version control throughout development.

---

# Repository Structure

```text
Anthony-Essel-Prepeh-Career-Package/
│
├── data/
├── docs/
├── templates/
├── scripts/
├── website/
├── exports/
├── assets/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── TODO.md
└── .gitignore
```

---

# Folder Responsibilities

## data/

Purpose:

Stores the master career information.

Examples:

- education.md
- coursework.md
- skills.md
- software.md
- projects.md
- experience.md
- certificates.md
- memberships.md
- references.md
- portfolio.md
- career_summary.md

These files are edited manually.

They are the **single source of truth**.

---

## templates/

Purpose:

Contains reusable templates used to generate documents.

Current templates include:

- resume.template.md
- ats.template.md
- executive.template.md
- academic_cv.template.md
- cover_letter.template.md
- linkedin.template.md
- github.template.md
- website.template.md

HTML templates are stored inside:

```text
templates/html/
```

Templates are edited manually.

---

## docs/

Purpose:

Stores generated Markdown documents.

Examples:

- resume.md
- ats_resume.md
- executive_resume.md
- academic_cv.md
- linkedin_profile.md
- github_profile.md

These files are generated automatically whenever possible.

---

## scripts/

Purpose:

Contains the automation engine.

Current scripts:

- build.py
- generate.py
- build_html.py
- text_utils.py

Future scripts:

- export_pdf.py
- export_docx.py
- website_generator.py
- deploy.py

---

## website/

Purpose:

Stores the portfolio website.

Includes:

- HTML
- CSS
- JavaScript
- Images

---

## exports/

Purpose:

Stores generated output files.

Structure:

```text
exports/
│
├── html/
├── pdf/
└── docx/
```

Generated files should not be edited manually.

---

## assets/

Purpose:

Stores reusable resources.

Examples:

- profile photographs
- icons
- logos
- downloadable documents

---

# Automation Pipeline

The current workflow is:

```text
data/
    │
    ▼
generate.py
    │
    ▼
docs/
    │
    ▼
build_html.py
    │
    ▼
exports/html/
```

Future workflow:

```text
data/
    │
    ▼
generate.py
    │
    ▼
Markdown Documents
    │
    ▼
HTML Generator
    │
    ├──────────────┐
    ▼              ▼
Website        PDF Generator
                   │
                   ▼
              DOCX Generator
```

---

# Build Process

The long-term goal is to use a single command:

```bash
python scripts/build.py
```

The build process will:

1. Verify the project structure.
2. Read career data.
3. Generate Markdown documents.
4. Generate HTML pages.
5. Generate PDF files.
6. Generate DOCX files.
7. Update the portfolio website.
8. Prepare for deployment.

---

# Emoji Handling

Markdown source files may contain emojis for readability.

Example:

```text
📧 Email
📍 Location
🎓 Education
```

During automated generation, emojis are removed before HTML and PDF creation.

The source files remain unchanged.

---

# Version Control

Every completed feature should follow this workflow:

1. Implement
2. Test
3. Commit
4. Push
5. Continue

This ensures every stage of the project can be restored if needed.

---

# Current Status

Completed:

- Repository structure
- Career database
- Documentation
- Resume templates
- Build system
- Document generator
- Emoji handling
- HTML generator

In Progress:

- Professional HTML layout
- CSS styling

Planned:

- PDF generation
- DOCX generation
- Portfolio website
- GitHub Pages deployment
- GitHub Actions automation

---

# Long-Term Vision

The Career Package will become a complete professional career management system capable of generating:

- Professional resumes
- ATS resumes
- Executive resumes
- Academic CVs
- Cover letters
- Portfolio website
- PDF exports
- DOCX exports

from a single, well-maintained career database.