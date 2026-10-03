import unittest
from pprint import pprint

from split_delimiter import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_parses_correctly(self):
        new_nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_only_special_text_parses_correct(self):
        new_nodes = text_to_textnodes(
            "**Bold text **_and a _[link](https://github.com)** and an **![image](../../img/my-image)"
        )
        self.assertListEqual(
            [
                TextNode("Bold text ", TextType.BOLD),
                TextNode("and a ", TextType.ITALIC),
                TextNode("link", TextType.LINK, "https://github.com"),
                TextNode(" and an ", TextType.BOLD),
                TextNode("image", TextType.IMAGE, "../../img/my-image"),
            ],
            new_nodes,
        )

    def test_handle_line_brakes(self):
        new_nodes = text_to_textnodes(
            '''Just some **Bold text** and
                some _italic text to
                test line brakes_'''
        )
        self.assertListEqual(
            [
                TextNode("Just some ", TextType.PLAIN),
                TextNode("Bold text", TextType.BOLD),
                TextNode(''' and
                some ''', TextType.PLAIN),
                TextNode('''italic text to
                test line brakes''', TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_empty_string_returns_empty_list(self):
        new_nodes = text_to_textnodes("")
        self.assertListEqual(
            [],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
