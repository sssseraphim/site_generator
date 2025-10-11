from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        nodes_to_add = list(node.text.split(delimiter))
        if len(nodes_to_add) % 2 == 0:
            raise Exception("invalid markdown")
        for i in range(len(nodes_to_add)):
            if not nodes_to_add[i]:
                continue
            if i % 2:
                new_nodes.append(TextNode(nodes_to_add[i], text_type))
            else:
                new_nodes.append(TextNode(nodes_to_add[i], TextType.TEXT))
    return new_nodes

            
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_images(text)
        for l in links:
            pre, text = text.split(f"![{l[0]}]({l[1]})", 1)
            if pre:
                new_nodes.append(TextNode(pre, TextType.TEXT))
            new_nodes.append(TextNode(l[0], TextType.IMAGE, l[1]))
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        for l in links:
            pre, text = text.split(f"[{l[0]}]({l[1]})", 1)
            if pre:
                new_nodes.append(TextNode(pre, TextType.TEXT))
            new_nodes.append(TextNode(l[0], TextType.LINK, l[1]))
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def text_to_textnode(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
