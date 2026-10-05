import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[([^\r\n\[\]]*)\]\(([^\r\n\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!!)\[([^\r\n\[\]]*)\]\(([^\r\n\(\)]*)\)", text)
    return matches


def markdown_to_blocks(text: str) -> list[str]:
    text_blocks = text.split("\n\n")
    final_blocks: list[str] = []
    for text_block in text_blocks:
        if text_block.strip():
            final_blocks.append(text_block.strip())

    return final_blocks

def extract_markdown_title(text: str) -> str:
    for line in text.split("\n"):
        if line.startswith("# "):
            return line[1:].strip(" ")
    raise ValueError("markdown must have a title")
