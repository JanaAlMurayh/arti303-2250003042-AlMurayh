def clean_name(name: str) -> str:
    return " ".join(name.strip().split()).title()
