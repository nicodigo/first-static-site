import unittest

from block_type import BlockType, block_to_block_type


class TestBlockeFromBlockType(unittest.TestCase):
    def test_return_paragraph(self):
        md = """This is just
a paragraph
of text in markdown"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_return_heading(self):
        headings = ["# h1", "## h2", "### h3", "#### h4", "##### h5", "###### h6"]
        for h in headings:
            self.assertEqual(block_to_block_type(h), BlockType.HEADING)

    def test_bad_format_heading_return_paragraph(self):
        md = """############ This is NOT a header"""
        md2 = """###This is NOT a header"""
        md3 = """####### This is NOT a header"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(md2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(md3), BlockType.PARAGRAPH)

    def test_return_code_block(self):
        code = """```
print("this is a generic code block")
```"""
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_bad_format_code_returns_paragraph(self):
        md = """```
I forgot a backtick closing this code block
``"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_return_quote(self):
        quote = """>The purpose of a storyteller is not to tell you how to think,
> but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_bad_format_quote_returns_paragraph(self):
        quote = """>The purpose of a storyteller is not to tell you how to think, 
but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(quote), BlockType.PARAGRAPH)

    def test_return_ul(self):
        ul = """- The purpose of a storyteller is not to tell you how to think,
- but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_bad_format_ul_returns_paragraph(self):
        ul = """- The purpose of a storyteller is not to tell you how to think, 
-but to give you questions to think upon."""
        ul2 = """- The purpose of a storyteller is not to tell you how to think, 
but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(ul), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(ul2), BlockType.PARAGRAPH)

    def test_return_ol(self):
        ol = """1. The purpose of a storyteller is not to tell you how to think,
2. but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

    def test_bad_format_ol_returns_paragraph(self):
        ol = """1. The purpose of a storyteller is not to tell you how to think, 
2.but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(ol), BlockType.PARAGRAPH)

        ol = """2. The purpose of a storyteller is not to tell you how to think, 
2. but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(ol), BlockType.PARAGRAPH)

        ol = """1. The purpose of a storyteller is not to tell you how to think, 
2 but to give you questions to think upon."""
        self.assertEqual(block_to_block_type(ol), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
