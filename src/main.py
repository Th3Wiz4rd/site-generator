import sys
import os
import shutil

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages recursively...")
    # Call the recursive function with directory paths, not file paths
    generate_pages_recursive(
        dir_path_content,  # The entire content directory
        template_path,     # The template file
        dir_path_public    # The destination directory
    )


main()