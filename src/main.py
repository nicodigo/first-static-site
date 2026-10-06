import os
import shutil
import sys

from htmlnode import HTMLNode
from markdown_to_html_node import markdown_to_html_node
from md_helpers import extract_markdown_title


def copy_files(src: str, dst: str) -> None:
    for item in os.listdir(src):
        if os.path.isfile(os.path.join(src, item)):
            shutil.copy(os.path.join(src, item), os.path.join(dst, item))
            print(f"copying... {os.path.join(src, item)} to {os.path.join(dst, item)}")
        else:
            os.makedirs(os.path.join(dst, item), exist_ok=True)
            copy_files(os.path.join(src, item), os.path.join(dst, item))


def copy_contents(src: str, dst: str) -> None:
    if not os.path.exists(src):
        raise FileNotFoundError("source directory not found")

    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.makedirs(dst)
    print("calling copy files")

    copy_files(src, dst)


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.isfile(from_path):
        raise ValueError("from_path must be a file")

    if not os.path.isfile(template_path):
        raise ValueError("template_path must be a file")

    with open(from_path, "r") as f:
        markdown: str = f.read()

    with open(template_path) as f:
        template_html = f.read()

    parent_div_node: HTMLNode = markdown_to_html_node(markdown)
    html_string = parent_div_node.to_html()
    md_title = extract_markdown_title(markdown)

    html_page = template_html.replace("{{ Title }}", md_title).replace(
        "{{ Content }}", html_string
    )
    html_page = html_page.replace('href="/', f'href="{basepath}')
    html_page = html_page.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_page)


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str) -> None:
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                generate_page(from_path, template_path, dest_path.replace(".md", ".html"), basepath)
            return
        generate_pages_recursive(from_path, template_path, dest_path, basepath)



def main() -> None:
    base_path = sys.argv[1] or "/"
    copy_contents("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", base_path)


if __name__ == "__main__":
    main()
