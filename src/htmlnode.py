class HTMLNode:

    def __init__(self, tag: str=None, value: str=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html_str = ""
        for p in self.props:
            html_str += f" {p}=\"{self.props[p]}\""
        return html_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("no tag")
        if not self.children:
            raise ValueError("no children")
        return f"<{self.tag}{self.props_to_html()}>{''.join([node.to_html() for node in self.children])}</{self.tag}>"
    


