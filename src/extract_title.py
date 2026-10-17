from mardown_to_blocks import markdown_to_blocks


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    h1_block = list(filter(lambda block: block.startswith("# "), blocks))

    if h1_block is None:
        raise SyntaxError("No title found in the markdown")

    title = h1_block[0].replace("# ", "").strip()

    return title
