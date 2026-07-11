"""
Career DOCX Generator

Builds all professional Word documents.
"""

from document_builder.resume import build as build_resume

from document_builder.curriculum_vitae import (
    build as build_curriculum_vitae,
)

from document_builder.cover_letter import (
    build as build_cover_letter,
)

from document_builder.portfolio import (
    build as build_portfolio,
)


# ==========================================================
# Main
# ==========================================================

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
        ("Resume", build_resume),
        ("Curriculum Vitae", build_curriculum_vitae),
        ("Cover Letter", build_cover_letter),
        ("Project Portfolio", build_portfolio),
    ]

    for name, builder in builders:

        print(f"Building {name}...")

        try:

            builder()

            print(f"✓ {name} completed.\n")

        except Exception as error:

            print(f"✗ {name} failed.")
            raise error

    print("=" * 60)
    print("All DOCX documents generated successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()