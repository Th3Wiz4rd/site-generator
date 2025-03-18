import sys
import os
import shutil

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages recursively...")
    # Call the recursive function with directory paths, not file paths
    generate_pages_recursive(
        dir_path_content,  
        template_path,     
        dir_path_docs,
        basepath    
    )


main()