import sys
import os
import shutil

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()