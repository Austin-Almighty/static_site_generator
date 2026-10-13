import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Text 1", TextType.CODE)
        node2 = TextNode("Text 2", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("Same text", TextType.IMAGE, None)
        node2 = TextNode("Same text", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("Some text", TextType.PLAIN)
        self.assertIsNone(node.url)



class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_1(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_code(self):
        node = TextNode("def hello(): hello world!", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "def hello(): hello world!")

if __name__ == "__main__":
    unittest.main()