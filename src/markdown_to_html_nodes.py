from block_to_block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode
from mardown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_text_nodes import text_to_text_nodes
from textnode import text_node_to_html_node


def text_to_children(text: str) -> list[HTMLNode]:
    children_text_nodes = text_to_text_nodes(text)
    children_html_nodes: list[HTMLNode] = [text_node_to_html_node(children) for children in children_text_nodes]
    return children_html_nodes


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                heading_splits = block.split(" ", maxsplit=1)
                heading_count = heading_splits[0].count("#")
                children_nodes = text_to_children(heading_splits[1])
                parent = ParentNode(f"h{heading_count}", children_nodes)
                html_nodes.append(parent)

