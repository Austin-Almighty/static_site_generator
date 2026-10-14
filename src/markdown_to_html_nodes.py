from block_to_block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode
from mardown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_text_nodes import text_to_text_nodes
from textnode import TextNode, TextType, text_node_to_html_node


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
                block_node = ParentNode(f"h{heading_count}", children_nodes)
                html_nodes.append(block_node)
            case BlockType.PARAGRAPH:
                normalized_text = block.replace("\n", " ")
                children_nodes = text_to_children(normalized_text)
                block_node = ParentNode("p", children_nodes)
                html_nodes.append(block_node)
            case BlockType.CODE:
                normalized_text = block[4:-3]
                code_text_node = TextNode(normalized_text, TextType.PLAIN)
                code_html_node = text_node_to_html_node(code_text_node)
                inner_node = ParentNode("code", [code_html_node])
                out_node = ParentNode("pre", [inner_node])
                html_nodes.append(out_node)
            case BlockType.QUOTE:
                lines = block.split("\n")
                normalized_lines = [line.replace(">", "", count=1).strip() for line in lines]
                normalized_text = "\n".join(normalized_lines)
                children_nodes = text_to_children(normalized_text)
                block_node = ParentNode("blockquote", children_nodes)
                html_nodes.append(block_node)
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                normalized_lines = [line[2:] for line in lines]
                children_nodes: list[HTMLNode] = [ParentNode("li", text_to_children(line)) for line in normalized_lines]
                block_node = ParentNode("ul", children_nodes)
                html_nodes.append(block_node)
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                splitted_lines = [line.split(". ") for line in lines]
                normalized_lines = [line[1] for line in splitted_lines]
                children_nodes: list[HTMLNode] = [ParentNode("li", text_to_children(line)) for line in normalized_lines]
                block_node = ParentNode("ol", children_nodes)
                html_nodes.append(block_node)

    whole_block_node = ParentNode("div", html_nodes)
    return whole_block_node