import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.PLAIN),
            ],
        )

    def test_split_delimiter_at_start(self):
        node = TextNode("**bold** at the start", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("bold", TextType.BOLD),
            TextNode(" at the start", TextType.PLAIN)
        ])

    def test_split_multiple_bold(self):
        node = TextNode("**bold** and **more bold**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [
                            TextNode("bold", TextType.BOLD),
                            TextNode(" and ", TextType.PLAIN),
                            TextNode("more bold", TextType.BOLD)
                         ],
                        )

    def test_non_text_node_untouched(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This has **unmatched bold", TextType.PLAIN)
        with self.assertRaises(SyntaxError):
         split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_valid_nodes(self):
        node1 = TextNode("Some `code` here", TextType.PLAIN)
        node2 = TextNode("Some `more code` there", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("Some ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.PLAIN),
            TextNode("Some ", TextType.PLAIN),
            TextNode("more code", TextType.CODE),
            TextNode(" there", TextType.PLAIN)
        ])


if __name__ == "__main__":
    unittest.main()


