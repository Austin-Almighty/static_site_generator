import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()