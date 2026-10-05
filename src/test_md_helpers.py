import unittest

from md_helpers import (
    extract_markdown_images,
    extract_markdown_links,
    extract_markdown_title,
)


class TestExtractMdImg(unittest.TestCase):
    def test_extract_one_image_correctly(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_image_on_a_link_should_return_empty(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) to an image"
        )
        self.assertListEqual([], matches)

    def test_extract_image_with_line_break_return_empty(self):
        matches = extract_markdown_images(
            '''This is text with an ![im
            age](https://i.imgur.com/zjjcJKZ.png)
            This is text with an ![image](https://i.i
            mgur.com/zjjcJKZ.png)
            '''
        )
        self.assertListEqual([], matches)



class TestExtractMdLink(unittest.TestCase):
    def test_extract_one_markdown_link_correctly(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) to an image"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_link_on_an_image_should_return_empty(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_link_with_line_break_return_empty(self):
        matches = extract_markdown_links(
            '''This is text with a [lin
            k](https://i.imgur.com/zjjcJKZ.png)
            This is text with a ![link](https://www.boot.dev/cour
            ses/learn-python-beginners)
            '''
        )
        self.assertListEqual([], matches)

class TestExtractMdTitle(unittest.TestCase):
    def test_extrcts_title(self):
        md="""
this is some markdown
with a

# Title

and some text"""
        self.assertEqual(
            extract_markdown_title(md),
            "Title",
        )

        md="""

#       A Title

and some text"""
        self.assertEqual(
            extract_markdown_title(md),
            "A Title",
        )

    def test_extracts_title_raises_exception(self):
        md="text with no title"
        self.assertRaises(ValueError, extract_markdown_title, md)

if __name__ == "__main__":
    unittest.main()
