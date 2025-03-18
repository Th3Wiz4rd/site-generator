import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        content_entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(content_entry_path):
            if content_entry_path.endswith('.md'):
                rel_path = os.path.relpath(content_entry_path, dir_path_content)
                html_filename = os.path.splitext(rel_path)[0] + '.html'
                dest_file_path = os.path.join(dest_dir_path, html_filename)

                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

                generate_page(content_entry_path, template_path, dest_file_path)

        elif os.path.isdir(content_entry_path):
            dest_subdir = os.path.join(dest_dir_path, entry)
            os.makedirs(dest_subdir, exist_ok=True)
            
            generate_pages_recursive(content_entry_path, template_path, dest_subdir)

        
            