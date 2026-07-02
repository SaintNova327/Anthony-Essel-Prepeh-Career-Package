"""
Text utilities for the Career Package.
"""

import emoji


def remove_emojis(text: str) -> str:
    """
    Remove emojis from text while keeping all other characters.
    """

    return emoji.replace_emoji(text, replace="")