import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_tag(self):
        node = LeafNode(None, "Hi")
        self.assertEqual(node.to_html(), "Hi")

    def test_value_is_none(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None)
            node.to_html()

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!")
        self.assertEqual(node.to_html(), "<a>Click me!</a>")

    def test_repr(self):
        node = LeafNode("p", "Hello, world!", props={"class": "greeting"})
        expected = "LeafNode(tag='p', value='Hello, world!', props={'class': 'greeting'})"
        self.assertEqual(repr(node), expected)




if __name__ == "__main__":
    unittest.main()