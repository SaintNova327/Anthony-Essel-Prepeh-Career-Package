# Development Guide

This document explains how to work with the Anthony Essel Prepeh Career Package.

---

# Project Overview

The Career Package is a centralized career management system that generates:

- Professional resumes
- ATS resumes
- Executive resumes
- Academic CVs
- Cover letters
- Portfolio website
- Future career documents

Everything is generated from a single source of truth located in the `data/` directory.

---

# Project Structure

```
Anthony-Essel-Prepeh-Career-Package/

├── config/
│   └── site_config.md
│
├── data/
│   ├── career_summary.md
│   ├── education.md
│   ├── experience.md
│   ├── projects.md
│   ├── skills.md
│   ├── software.md
│   ├── certificates.md
│   ├── memberships.md
│   ├── portfolio.md
│   └── references.md
│
├── templates/
│
├── scripts/
│   ├── generate.py
│   ├── build.py
│   └── build_website.py
│
├── website/
│
└── docs/
```

---

# Data Layer

The `data/` folder is the single source of truth.

Each Markdown file contains one category of career information.

Example:

```
projects.md
```

contains all project information.

The website and resumes are generated from these files.

---

# Resume Generation

Generate all resume documents:

```bash
python scripts/generate.py
```

Generate PDF:

```bash
python scripts/build.py
```

---

# Website Generation

Generate the website:

```bash
python scripts/build_website.py
```

Generated pages are written into:

```
website/
```

---

# Configuration

Global website configuration is stored in:

```
config/site_config.md
```

This controls:

- author information
- website title
- navigation
- theme
- footer

---

# Templates

Reusable templates are stored inside:

```
templates/
```

Website layouts are stored inside:

```
website/layouts/
```

---

# CSS Architecture

```
website/css/

variables.css
layout.css
navigation.css
hero.css
cards.css
timeline.css
buttons.css
footer.css
responsive.css

main.css
```

Each stylesheet has a single responsibility.

---

# Adding a New Website Page

1. Create a layout

```
website/layouts/newpage.html
```

2. Register it in:

```
scripts/build_website.py
```

Example:

```python
{
    "output": "newpage.html",
    "layout": "newpage.html",
    "title": "New Page"
}
```

3. Build:

```bash
python scripts/build_website.py
```

---

# Adding Career Data

Create a new Markdown file inside:

```
data/
```

Example:

```
awards.md
```

The website generator automatically loads all Markdown files in the data directory.

---

# Git Workflow

After completing a feature:

```bash
git add .

git commit
```

Recommended commit style:

Summary:

```
Implement feature name
```

Description:

```
Describe what was added
and why.
```

---

# Development Philosophy

The project follows these principles:

- Single source of truth
- Reusable templates
- Separation of content and presentation
- Automation first
- Documentation driven
- Version controlled
- Easy to extend
- Professional software engineering practices

---

# Future Enhancements

Planned improvements include:

- GitHub Pages deployment
- Automatic PDF deployment
- Dark mode
- Search
- Project cards
- Experience timeline
- Certificate gallery
- Blog section
- Custom domain
- GitHub Actions automation

---

# Maintainer

Anthony Essel Prepeh

Geological Engineer

Mining Technology • Artificial Intelligence • Data Analysis