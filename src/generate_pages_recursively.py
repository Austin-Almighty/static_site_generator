from pathlib import Path

from generate_page import generate_page


def generate_pages_recursively(dir_path_content: Path, template_path: Path, dest_dir_path: Path, base_path: str):

    if not dir_path_content.exists():
        raise FileNotFoundError("Could not find the content path")

    for item in dir_path_content.iterdir():
        if item.is_file() and item.suffix == ".md":
            generate_page(item, template_path, dest_dir_path.joinpath(item.name).with_suffix(".html"), base_path)
        elif item.is_dir():
            generate_pages_recursively(item, template_path, dest_dir_path.joinpath(item.name), base_path)


