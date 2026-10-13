from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_node_list = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_node_list.append(node)
            continue
        split_nodes = node.text.split(delimiter)
        if (len(split_nodes)%2 == 0):
            raise SyntaxError(f"Invalid markdown syntax: unclosed delimiter '{delimiter}'")
        new_node = []
        for i, part in enumerate(split_nodes):
            if (len(part) == 0):
                continue
            elif (i%2==0):
                new_node.append(TextNode(part, TextType.PLAIN))
            else:
                new_node.append(TextNode(part, text_type))

        new_node_list.extend(new_node)

    return new_node_list