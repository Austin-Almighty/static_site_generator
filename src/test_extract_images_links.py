import unittest

from extract_images_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestExtractImagesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "this is text with an [link](https://google.com) and another [second link](https://yahoo.com.tw)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("this is text with an ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second link", TextType.LINK, "https://yahoo.com.tw")
            ],
            new_nodes
        )

    def test_image_in_front(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) Testing if this will work",
            TextType.PLAIN
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" Testing if this will work", TextType.PLAIN),
        ],
            new_nodes
        )