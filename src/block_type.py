from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#") and not block.startswith("#######"):
        heading = block.lstrip("#")
        if heading.startswith(" ") and heading.strip():
            return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        is_quote = True
        for line in block.split("\n"):
            if not line.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return BlockType.QUOTE

    if block.startswith("- "):
        is_ul = True
        for line in block.split("\n"):
            if not line.startswith("- "):
                is_ul = False
                break
        if is_ul:
            return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        is_ol = True
        i = 1
        for line in block.split("\n"):
            if not line.startswith(f"{i}. "):
                is_ol = False
                break
            i += 1
        if is_ol:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

