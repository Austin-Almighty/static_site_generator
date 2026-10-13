from unittest import TestCase

from src.block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlock(TestCase):
    def test_heading_without_space(self):
        text_block = "#heading"
        block_type = block_to_block_type(text_block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading_1(self):
        text_block = "### a h3 heading"
        block_type = block_to_block_type(text_block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_to_many(self):
        text_block = "######### too many #"
        block_type = block_to_block_type(text_block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_quote_blocks_1(self):
        text_block = """> first line\n>second line\n> third line"""
        block_type = block_to_block_type(text_block)

        self.assertEqual(block_type, BlockType.QUOTE)

    def test_empty_code_blocks(self):
        text_block = "```\n```"
        block_type = block_to_block_type(text_block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_ordered_list(self):
        text_block = "1. first line\n2. second line\n3. third line"
        block_type = block_to_block_type(text_block)

        self.assertEqual(block_type, BlockType.ORDERED_LIST)