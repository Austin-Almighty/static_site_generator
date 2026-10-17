import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_only_title(self):
        markdown = "# Hello"
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")

    def test_long_markdown(self):
        markdown = "- This is one of the many blocks. \n\n# This is a title that we want.\n\nThis is a regular paragraph.\n"
        title = extract_title(markdown)

        self.assertEqual(title, "This is a title that we want.")


# if __name__ == "__main__":
#     unittest.main()