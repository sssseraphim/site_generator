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
    dest_file = os.path.join(dest_path, Path(from_path).stem)
    dest_file += ".html"
    print(dest_file, "file")
    with open(dest_file, 'a') as dest:
        dest.write(template)

def generate_page_rec(dir_path_content, template_path, dest_dir_path):
    content_path = os.path.abspath(dir_path_content)
    dest_path = os.path.abspath(dest_dir_path)
    for p in os.listdir(content_path):
        path = os.path.join(content_path, p)
        if os.path.isfile(path):
            generate_page(os.path.join(content_path, p), template_path, dest_path)
        else:
            dest = os.path.join(dest_path, p)
            os.mkdir(dest)
            generate_page_rec(os.path.join(content_path, p), template_path, dest)

        
        

    
        


                 
        
        
    

