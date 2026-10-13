from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"


def block_to_block_type(block: str) -> BlockType:
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    if " " in block:
        first_section_list = block.split(" ", maxsplit=1)
        heading_count = first_section_list[0].count("#")
        if len(first_section_list[0]) == heading_count and 1 <= heading_count < 7:
            return BlockType.HEADING
    lines = block.split("\n")

    quote = True
    ul = True
    ol = True

    for i, line in enumerate(lines):
        if not line.startswith(">"):
            quote = False
        if not line.startswith("- "):
            ul = False
        if not line.startswith(f"{i+1}. "):
            ol = False

    if quote:
        return BlockType.QUOTE
    if ul:
        return BlockType.UNORDERED_LIST
    if ol:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
