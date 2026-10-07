import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

    def test_tag_is_none(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            node = ParentNode(None, [child_node])
            node.to_html()
    def test_children_is_none(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()
            

if __name__ == "__main__":
    unittest.main()