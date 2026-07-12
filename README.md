# Anthony Essel Prepeh Career Operating System

> A professional automation system that generates a complete career package and portfolio website from a single source of truth.

---

## Overview

The **Career Operating System** is a Python-based automation project that manages and generates professional career documents and a portfolio website from centralized Markdown and YAML data.

Rather than maintaining multiple versions of the same information, this system stores career data once and automatically generates consistent, professional outputs.

The project was developed as part of my continuous learning in software development, automation, and professional engineering documentation while pursuing a Bachelor of Science in Geological Engineering.

---

## Features

### Professional Website

- Responsive portfolio website
- Professional homepage
- About page
- Projects page
- Education page
- Experience page
- Certificates page
- Contact page
- Downloadable career documents

---

### Career Documents

Automatically generates:

- Professional Resume
- Academic Curriculum Vitae (CV)
- Professional Cover Page
- Professional Cover Letter
- Professional References
- Project Portfolio

---

### Automation

- Single source of truth
- Markdown-driven content
- YAML databases
- Automatic HTML generation
- Automatic DOCX generation
- Automatic PDF generation
- Shared rendering system
- Modular document builder

---

## Project Structure

```
Anthony-Essel-Prepeh-Career-Package/

├── career_documents/
├── config/
├── data/
├── output/
├── scripts/
│   ├── build.py
│   ├── build_docx.py
│   ├── build_website.py
│   ├── document_builder/
│   └── renderers/
├── website/
│   ├── components/
│   ├── css/
│   ├── js/
│   └── layouts/
└── README.md
```

---

## Technology Stack

### Programming

- Python

### Markup

- Markdown
- HTML5
- CSS3

### Data

- YAML

### Libraries

- python-docx
- Markdown
- PyYAML

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## Generated Outputs

The system generates:

- Portfolio Website
- Professional Resume
- Curriculum Vitae
- Cover Page
- Cover Letter
- References
- Project Portfolio
- PDF versions of career documents

---

## How to Build

Generate the website

```bash
python scripts/build.py
```

Generate the DOCX documents

```bash
python scripts/build_docx.py
```

Generate PDFs

```bash
python scripts/build_pdf.py
```

---

## Design Philosophy

The project follows a modular architecture.

- Single source of truth
- Reusable renderers
- Shared styling
- Maintainable codebase
- Automated generation
- Consistent branding

This minimizes duplicated content while making updates simple and reliable.

---

## Current Status

**Version:** 1.0.0

Current release includes:

- Professional website
- Complete document generation
- Automated build system
- Professional styling
- Responsive layouts

---

## Roadmap

### Version 1.1

- ATS Resume
- Executive Resume
- Resume selection page
- Company-specific cover letters

### Version 2.0

- Interactive dashboard
- Theme support
- Multiple resume templates
- AI-assisted customization
- Advanced certificate management
- Analytics dashboard

---

## About Me

**Anthony Essel Prepeh**

Final-year BSc Geological Engineering Student

Kwame Nkrumah University of Science and Technology (KNUST)

Interested in:

- Geological Engineering
- Mining Technology
- Hydrogeology
- GIS
- Remote Sensing
- Python
- Artificial Intelligence

---

## License

This project is released under the MIT License.