import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_with_spaces(self):
        md = """
This is **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    
    def test_heading_block(self):
        block = "### big beans"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )
    
    def test_code_block(self):
        block = '''```big beans```'''
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_quote_block(self):
        block = '''>ig beans/n>gay'''
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_unordered_list_block(self):
        block = "- big beans\n- gomer\n- busy"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list_block(self):
        block = "1. big beans\n2. nerd \n3. busy"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )
        
    def test_paragraphs_to_html(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock_to_html(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock_to_html(self):
        md = """
>This is quote text that _should_
>and **will be**
""" 
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is quote text that <i>should</i> and <b>will be</b></blockquote></div>"
        ) 

    def test_heading_to_html(self):
        md = """
#### I hate **beans**
""" 
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4> I hate <b>beans</b></h4></div>"
        ) 
    
    def test_unordered_list_to_html(self):
        md = """
- bob
- **fat bob**
- _italian bob_
""" 
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>bob</li><li><b>fat bob</b></li><li><i>italian bob</i></li></ul></div>"
        ) 

    def test_ordered_list_to_html(self):
        md = """
1. bob
2. **fat bob**
3. _italian bob_
""" 
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>bob</li><li><b>fat bob</b></li><li><i>italian bob</i></li></ol></div>"
        ) 