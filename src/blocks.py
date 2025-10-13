from enum import Enum
from htmlnode import ParentNode, LeafNode
from inline import text_to_textnode
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    return [s.strip() for s in filter(lambda x: x, markdown.split("\n\n"))]

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    if all(map(lambda x: x and x[0] == ">", block.split("\n"))):
        return BlockType.QUOTE
    if all(map(lambda x: len(x) > 1 and x[:2] == "- ", block.split("\n"))):
        return BlockType.UNORDERED_LIST
    block = block.split("\n")
    if all([block[i-1][:len(str(i))+2] == f"{i}. " for i in range(1, len(block)+1)]):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    return [text_node_to_html_node(node) for node in text_to_textnode(text)]

def block_to_paragraph_node(text):
    text = " ".join(text.split("\n"))
    children = text_to_children(text)
    return ParentNode("p", children)

def block_to_heading_node(text):
    i = 0
    while i < len(text) and text[i] == "#":
        i += 1
    children = text_to_children(text[i:])
    return ParentNode(f"h{i}", children)

def block_to_code_node(text):
    return ParentNode("pre", [LeafNode("code", text[4:-3])])

def block_to_quote_node(text):
    children = text_to_children(" ".join([s[1:] for s in text.split("\n")]))
    return ParentNode("blockquote", children)

def block_to_unordered_list_node(text):
    children = [ParentNode("li", text_to_children(s[2:])) for s in text.split("\n")]
    return ParentNode("ul", children)

def block_to_ordered_list_node(text):
    children = [ParentNode("li", text_to_children(s[s.find(" ")+1:])) for s in text.split("\n")]
    return ParentNode("ol", children)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)            
        match block_type:
            case BlockType.PARAGRAPH:
                children.append(block_to_paragraph_node(block))
            case BlockType.HEADING:
                children.append(block_to_heading_node(block))
            case BlockType.CODE:
                children.append(block_to_code_node(block))
            case BlockType.QUOTE:
                children.append(block_to_quote_node(block))
            case BlockType.UNORDERED_LIST:
                children.append(block_to_unordered_list_node(block))
            case BlockType.ORDERED_LIST:
                children.append(block_to_ordered_list_node(block))
    return ParentNode("div", children)

