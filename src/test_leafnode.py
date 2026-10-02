import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "this is a link", {"href": "/homepage"})
        self.assertEqual(node.to_html(), '<a href="/homepage">this is a link</a>')

    def test_leaf_to_html_a_multiple_props(self):
        node = LeafNode("a", "link", {"href": "/homepage", "target": "_self"})
        self.assertEqual(node.to_html(), '<a href="/homepage" target="_self">link</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "world!")
        self.assertEqual(node.to_html(), "<b>world!</b>")


if __name__ == "__main__":
    unittest.main()
