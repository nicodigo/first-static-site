from md_helpers import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
from pprint import pprint


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError(f'the string: "{node.text}" is not valid markdown sintax')
        for i in range(len(split_node)):
            if not split_node[i]:
                continue
            # if even index then text is 'PLAIN' type, else is 'text_type'
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node[i], TextType.PLAIN))
            else:
                new_nodes.append(TextNode(split_node[i], text_type))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        # if there is no links in the node
        if len(links) == 0:
            if node.text:
                new_nodes.append(TextNode(node.text, TextType.PLAIN))
            continue

        node_text = node.text
        for link in links:
            split_text = node_text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.PLAIN))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = split_text[1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.PLAIN))
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            if node.text:
                new_nodes.append(TextNode(node.text, TextType.PLAIN))
            continue
        node_text = node.text
        for image in images:
            split_text = node_text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.PLAIN))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = split_text[1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.PLAIN))
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    new_nodes: list[TextNode] = [TextNode(text, TextType.PLAIN)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes
