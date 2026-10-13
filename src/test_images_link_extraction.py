import unittest

from extract_images_links import extract_markdown_images, extract_markdown_links


class TestImagesLinksExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_images_fail_case(self):
        matches = extract_markdown_images("This is text with an incomplete image ![image(https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([], matches)

    def test_empty_string(self):
        matches = extract_markdown_images("")
        self.assertListEqual([], matches)

    def test_links_on_images_markdown(self):
        matches = extract_markdown_links("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([], matches)


