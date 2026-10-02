from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)

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
