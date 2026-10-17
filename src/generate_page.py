from pathlib import Path

from extract_title import extract_title
from markdown_to_html_nodes import markdown_to_html_node


def generate_page(from_path: Path, template_path: Path, dest_path: Path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not from_path.exists():
        raise FileNotFoundError("Source file not found")
    if not from_path.is_file():
        raise FileNotFoundError("The source path does not point to a file")

    source_content = from_path.read_text(encoding="utf-8")

    if not template_path.exists():
        raise FileNotFoundError("Template file not found")
    if not template_path.is_file():
        raise FileNotFoundError("The template path does not point to a file")

    template_content = template_path.read_text(encoding="utf-8")

    html_string = markdown_to_html_node(source_content).to_html()
    title = extract_title(source_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_string)


    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(template_content, encoding="utf-8")


