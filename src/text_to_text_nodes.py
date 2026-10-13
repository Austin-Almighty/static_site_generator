from extract_images_links import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def text_to_text_nodes(text: str) -> list[TextNode]:
    # delimiters = {TextType.CODE: "`", TextType.ITALIC: "_", TextType.BOLD: "**"}
    source_node = TextNode(text, TextType.PLAIN)

    code_nodes = split_nodes_delimiter([source_node], "`", TextType.CODE)
    italic_nodes = split_nodes_delimiter(code_nodes, "_", TextType.ITALIC)
    bold_nodes = split_nodes_delimiter(italic_nodes, "**", TextType.BOLD)

    check_for_images_nodes = split_nodes_image(bold_nodes)
    check_for_links_nodes = split_nodes_link(check_for_images_nodes)

    return check_for_links_nodes

