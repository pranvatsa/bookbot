from collections import Counter
from typing import Dict, List

def get_num_words(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())

def get_char_counts(text: str) -> Dict[str, int]:
    """Return a dictionary of character counts (case-insensitive) for the given text."""
    return dict(Counter(text.lower()))

def sort_char_counts(char_counts: Dict[str, int]) -> List[Dict[str, int]]:
    """
    Return a sorted list of dictionaries with character and count,
    sorted by count descending, only for alphabetic characters.
    """
    return sorted(
        ({"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()),
        key=lambda x: x["num"],
        reverse=True
    )