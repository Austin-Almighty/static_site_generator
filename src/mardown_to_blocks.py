def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    return [stripped for block in blocks if (stripped := block.strip())]


