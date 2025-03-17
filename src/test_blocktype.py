import unittest
from blocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("###### Heading"), BlockType.heading)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- List item"), BlockType.unordered_list)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ordered_list)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> A quote"), BlockType.quote)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.code)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a paragraph."), BlockType.paragraph)

if __name__ == "__main__":
    unittest.main()