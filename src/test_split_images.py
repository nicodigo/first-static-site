import unittest

from split_delimiter import split_nodes_image
from textnode import TextNode, TextType


class TestSplitImages(unittest.TestCase):
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
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_multiple_nodes(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        node2 = TextNode(
            "![This is the same image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        node3 = TextNode(
            "And this is just some plain old text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node, node2, node3])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(
                    "This is the same image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode("And this is just some plain old text", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_images_empty_node(self):
        node = TextNode("", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
