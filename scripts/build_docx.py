"""
Career DOCX Generator

Builds all professional Word documents.
"""

from document_builder.resume import build as build_resume
from document_builder.curriculum_vitae import build as build_curriculum_vitae
from document_builder.cover_letter import build as build_cover_letter
from document_builder.portfolio import build as build_portfolio
from document_builder.cover_page import build as build_cover_page
from document_builder.references import (
    build as build_references,
)


def main():
    """
    Generate all DOCX documents.
    """

    print("=" * 60)
    print("Anthony Essel Prepeh Career Package")
    print("Professional DOCX Generator")
    print("=" * 60)
    print()

    builders = [
        ("Professional Resume", build_resume),
        ("Curriculum Vitae", build_curriculum_vitae),
        ("Cover Page", build_cover_page),
        ("Cover Letter", build_cover_letter),
        ("Professional References", build_references),
        ("Project Portfolio", build_portfolio),
    ]

    for name, builder in builders:
        print(f"Building {name}...")

        try:
            builder()
            print(f"✓ {name} completed.\n")

        except Exception as error:
            print(f"✗ {name} failed.")
            raise

    print("=" * 60)
    print("All DOCX documents generated successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()