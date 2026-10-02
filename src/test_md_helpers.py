import unittest

from md_helpers import extract_markdown_images, extract_markdown_links


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
