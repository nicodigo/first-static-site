from block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from md_helpers import markdown_to_blocks
from split_delimiter import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def numbered_html_heading(heading: str) -> ParentNode:
    h_num = 0
    for char in heading:
        if char != "#":
            break
        h_num += 1
    return ParentNode(f"h{h_num}", [])


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes: list[TextNode] = text_to_textnodes(text)
    html_nodes: list[HTMLNode] = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def process_quote_block(text: str) -> str:
    proccesed_quote: str = ""
    for line in text.split("\n"):
        proccesed_quote += line.lstrip(">").lstrip(" ").replace("\n", " ")
        proccesed_quote += " "
    return proccesed_quote.strip()


def process_ul_block(text: str) -> list[HTMLNode]:
    li_nodes: list[HTMLNode] = []
    for line in text.split("\n"):
        li_text = line.lstrip("-").lstrip(" ").replace("\n", "")
        li_nodes.append(ParentNode("li", children=text_to_children(li_text)))
    return li_nodes


def process_ol_block(text: str) -> list[HTMLNode]:
    li_nodes: list[HTMLNode] = []
    for line in text.split("\n"):
        li_text = line[2:].lstrip(" ").replace("\n", "")
        li_nodes.append(ParentNode("li", children=text_to_children(li_text)))
    return li_nodes


def markdown_to_html_node(markdown: str) -> HTMLNode:
    md_blocks = markdown_to_blocks(markdown)
    parent_node: ParentNode = ParentNode("div", [])
    parent_node.children = []
    for block in md_blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                html_node = ParentNode("p", [])
                text = block.replace("\n", " ")
                html_node.children = text_to_children(text)
            case BlockType.HEADING:
                html_node = numbered_html_heading(block)
                text = block.lstrip("#").lstrip(" ")
                html_node.children = text_to_children(text)
            case BlockType.CODE:
                html_node = ParentNode("pre", [])
                text = block.strip("`").lstrip("\n")
                html_node.children = [  # type: ignore
                    text_node_to_html_node(TextNode(text, TextType.CODE))
                ]
            case BlockType.QUOTE:
                html_node = ParentNode("blockquote", [])
                text = process_quote_block(block)
                html_node.children = text_to_children(text)
            case BlockType.UNORDERED_LIST:
                html_node = ParentNode("ul", [])
                ul_children: list[HTMLNode] = process_ul_block(block)
                html_node.children = ul_children
            case BlockType.ORDERED_LIST:
                html_node = ParentNode("ol", [])
                ol_children: list[HTMLNode] = process_ol_block(block)
                html_node.children = ol_children
            case _:
                # Should be unreachable
                html_node = ParentNode("div", [])
        parent_node.children.append(html_node)
    return parent_node
