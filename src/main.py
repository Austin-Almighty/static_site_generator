import logging
import shutil
import sys
from pathlib import Path

from generate_pages_recursively import generate_pages_recursively

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def recursive_copy_contents(src: Path, target: Path):
    if not isinstance(src, Path) or not isinstance(target, Path):
        raise TypeError("Please pass in valid Path objects")
    if not src.exists():
        raise FileNotFoundError("Source Folder Not Found")
    if not src.is_dir():
        raise NotADirectoryError("The source path is not a directory")
    target.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        if item.is_dir():
            target_copy_dir = target / item.name
            logger.info(f"Entering directory: {item}")
            recursive_copy_contents(item, target_copy_dir)
        else:
            logger.info(f"Copying file: {item} -> {target / item.name}")
            shutil.copy2(item, target / item.name)


def copy_files_from_static_to_public():
    PUBLIC_DIR = Path(__file__).resolve().parent.parent / "public"

    if PUBLIC_DIR.is_dir():
        for item in PUBLIC_DIR.iterdir():
            if item.is_dir() and not item.is_symlink():
                shutil.rmtree(item)
            else:
                item.unlink()

    STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
    recursive_copy_contents(STATIC_DIR, PUBLIC_DIR)



basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


def main():
    copy_files_from_static_to_public()

    source_path = Path(__file__).resolve().parent.parent / "content"
    template_path = Path(__file__).resolve().parent.parent / "template.html"
    destination_path = Path(__file__).resolve().parent.parent / "docs"

    generate_pages_recursively(source_path, template_path, destination_path, basepath)

if __name__ == "__main__":
    main()