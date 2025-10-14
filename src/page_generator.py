from blocks import markdown_to_html_node
import os 
from pathlib import Path

def extract_title(markdown):
    for line in markdown.split("\n"):
        if len(line) >= 2 and line[0] == "#" and line[1] != "#":
            return line[1:].strip()
    raise Exception("no h1 header")
    
def generate_page(from_path, template_path, dest_path):
    from_path = os.path.abspath(from_path)
    template_path = os.path.abspath(template_path)
    dest_path = os.path.abspath(dest_path)
    print(f"Generating a page from {from_path} to {dest_path} using {template_path} template")
    with open(from_path, 'r') as source:
        markdown = source.read()
    with open(template_path, 'r') as t:
        template = t.read()
    node = markdown_to_html_node(markdown)
    template = template.replace("{{ Title }}", extract_title(markdown))
    template = template.replace("{{ Content }}", node.to_html())
    
    new = os.path.join(dest_path, Path(from_path).stem)
    os.makedirs(os.path.dirname(new), exist_ok=True)
    with open(new, 'a') as dest:
        dest.write(template)

def generate_page_rec(dir_path_content, template_path, dest_dir_path):
    content_path = os.path.abspath(dir_path_content)
    dest_path = os.path.abspath(dest_dir_path)
    if os.path.isfile(content_path):
        generate_page(content_path, template_path, dest_dir_path)
    else:
        for path in os.listdir(dir_path_content):
            c = os.path.join(content_path, path)
            if os.path.isfile(c):
                generate_page(c, template_path, dest_path)
            else:
                c, d = os.path.join(content_path, path), os.path.join(dest_path, path)
                generate_page_rec(c, template_path, d)
        
    

