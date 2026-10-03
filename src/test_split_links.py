import unittest

from split_delimiter import split_nodes_link
from textnode import TextNode, TextType


class TestSplitLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_links_multiple_nodes(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        node2 = TextNode(
            "[This is the same link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        node3 = TextNode(
            "And this is just some plain old text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node, node2, node3])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This is the same link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("And this is just some plain old text", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_links_empty_node(self):
        node = TextNode("", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
