import re

from textnode import TextNode, TextType


def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    res_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAIN:
            res_nodes.append(node)
            continue
        extracted_images_tuples = extract_markdown_images(node.text)
        if not extracted_images_tuples:
            res_nodes.append(node)
            continue

        remaining_text = node.text

        for image_alt, image_link in extracted_images_tuples:
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            before_text = sections[0]
            remaining_text = sections[1]

            if before_text != "":
                res_nodes.append(TextNode(before_text, TextType.PLAIN))
            res_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

        if remaining_text != "":
            res_nodes.append(TextNode(remaining_text, TextType.PLAIN))

    return res_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAIN:
            res_nodes.append(node)
            continue
        extracted_links_tuples = extract_markdown_links(node.text)
        if not extracted_links_tuples:
            res_nodes.append(node)
            continue

        remaining_text = node.text

        for link_txt, link_url in extracted_links_tuples:
            sections = remaining_text.split(f"[{link_txt}]({link_url})", 1)
            before_text, remaining_text = sections[0], sections[1]

            if before_text != "":
                res_nodes.append(TextNode(before_text, TextType.PLAIN))
            res_nodes.append(TextNode(link_txt, TextType.LINK, link_url))

        if remaining_text != "":
            res_nodes.append(TextNode(remaining_text, TextType.PLAIN))

    return res_nodes



