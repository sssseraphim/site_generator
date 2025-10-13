from textnode import TextNode, TextType
import os, shutil

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
    copy_tree("./static", "./static copy")


main()