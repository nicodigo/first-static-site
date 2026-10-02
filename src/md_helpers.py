import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[([^\r\n\[\]]*)\]\(([^\r\n\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!!)\[([^\r\n\[\]]*)\]\(([^\r\n\(\)]*)\)", text)
    return matches
