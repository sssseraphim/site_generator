import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("<h>", "bob", props={"bob": "bean", "href":"bobs"})
        self.assertEqual(node.props_to_html(), " bob=\"bean\" href=\"bobs\"")

    def test_empty_props(self):
        node = HTMLNode("<h>", "bob")
        self.assertEqual(node.props_to_html(), "")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_leaf_no_tag(self):
        s = "lgakjdl;fj"
        node = LeafNode(None, s)
        self.assertEqual(node.to_html(), s)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '''<a href="https://www.google.com">Click me!</a>''')

    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_no_children(self):
        node = ParentNode("a", [])
        self.assertRaises(ValueError, node.to_html)
    
    def test_parent_to_html_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            props={"bob": "bean", "href":"bobs"}
        )
        self.assertEqual(
            node.to_html(),
            "<p bob=\"bean\" href=\"bobs\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )