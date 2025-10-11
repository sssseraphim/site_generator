import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_dif_text(self):
        node = TextNode("This is bean", TextType.ITALIC)
        node1 = TextNode("bob", TextType.ITALIC)
        self.assertNotEqual
    
    def test_dif_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://developer.mozilla.org/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/lessons/")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/lessons/")
        self.assertNotEqual(node, node2)


class TestTextToHTML:
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_img(self):
        node = TextNode("beans", TextType.LINK, "https://sybau")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<a href=\"https://sybau\">beans</a>")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
        
if __name__ == "__main__":
    unittest.main()