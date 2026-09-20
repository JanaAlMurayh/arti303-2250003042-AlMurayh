"""Module containing utility functions for text processing."""

def clean_name(raw):
    """Clean and title-case a messy name string."""
    cleaned = " ".join(raw.split()).title()
    return cleaned
