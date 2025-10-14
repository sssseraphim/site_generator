from textnode import TextNode, TextType
import os, shutil
from page_generator import generate_page_rec, generate_page
import sys

def copy_tree(source, destination):
    source, destination = os.path.abspath(source), os.path.abspath(destination)
    if not os.path.exists(source):
        raise Exception("source directory does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    for name in os.listdir(source):
        abs_name = os.path.abspath(os.path.join(source, name))
        if os.path.isdir(abs_name):
            s, d = abs_name, os.path.join(destination, name)
            copy_tree(s, d)
        if os.path.isfile(abs_name):
            shutil.copy(abs_name, destination)


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    if os.path.exists("/docs"):
        shutil.rmtree("/docs")
    copy_tree("./static", "./docs")
    generate_page_rec("./content", "./template.html", "./docs", basepath)

main()