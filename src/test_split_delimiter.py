from types import new_class
import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_code_block_on_the_middle(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.PLAIN),
            ],
        )

    def test_text_starting_and_ending_with_bold(self):
        node = TextNode("**This is text **starting with **bold text**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text ", TextType.BOLD),
                TextNode("starting with ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
            ],
        )

    def test_text_starting_with_italic_bold_in_the_middle(self):
        node = TextNode("_This is text_ starting with **italic** and ending plain", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text", TextType.ITALIC),
                TextNode(" starting with **italic** and ending plain", TextType.PLAIN),
            ],
        )

    def test_two_nodes_with_bold_text(self):
        node = TextNode("_This is text_ starting with **italic** and ending plain", TextType.PLAIN)
        node2 = TextNode("**This is text** starting with **bold text**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("_This is text_ starting with ", TextType.PLAIN),
                TextNode("italic", TextType.BOLD),
                TextNode(" and ending plain", TextType.PLAIN),
                TextNode("This is text", TextType.BOLD),
                TextNode(" starting with ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
            ],
        )

    def test_using_function_twice_doesnt_duplicate_text(self):
        node = TextNode("_This is text_ starting with **italic** and ending plain", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

        self.assertListEqual(
            [
                TextNode("This is text", TextType.ITALIC),
                TextNode(" starting with ", TextType.PLAIN),
                TextNode("italic", TextType.BOLD),
                TextNode(" and ending plain", TextType.PLAIN),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
