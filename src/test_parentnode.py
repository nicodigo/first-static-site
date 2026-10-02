import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"class": "my-div"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="my-div"><span><b>grandchild</b></span></div>',
        )

    def test_to_html_with_grandchildren_with_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"class": "medium-bold"})
        child_node = ParentNode("a", [grandchild_node], {"href": "/home/profile", "target": "_self"})
        parent_node = ParentNode("div", [child_node], {"class": "my-div"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="my-div"><a href="/home/profile" target="_self"><b class="medium-bold">grandchild</b></a></div>',
        )

if __name__ == "__main__":
    unittest.main()
