import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_return_empty_when_no_props(self):
        node = HTMLNode("a", "anchor text")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_start_with_space(self):
        node = HTMLNode("a", "anchor text", props={"href": "/home"})
        self.assertStartsWith(node.props_to_html(), " ")

    def test_props_to_html_have_two_elements(self):
        node = HTMLNode("a", "anchor text", props={"href": "/home", "target": "_self"})
        self.assertEqual(len(node.props_to_html().split()), 2)


if __name__ == "__main__":
    unittest.main()
