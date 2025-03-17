import os
import shutil

def copy_files_recursive(source_dir, dest_dir):
    # First, delete the destination if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # Create the destination directory
    os.mkdir(dest_dir)
    
    # Now copy files recursively
    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        print(f" * {from_path} -> {dest_path}")
        
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)