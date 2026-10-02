from textnode import TextNode, TextType


def main() -> None:
    text_node: TextNode = TextNode("Just some good old plain text", TextType.PLAIN)
    print(text_node)


if __name__ == "__main__":
    main()
