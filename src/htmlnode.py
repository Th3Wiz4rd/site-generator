
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result = []
        for key, value in self.props.items():
            formatted_prop = f' {key}="{value}"'
            result.append(formatted_prop)

        return "".join(result)
    

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
       
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None: 
            raise ValueError
        
        if self.tag is None:
            return self.value 
        
        else: 
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):

        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        
        if self.children is None:
            raise ValueError("Uhoh! Boots lost his monocle! check your data!")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props_html = self.props_to_html() 
        return f"<{self.tag}>{children_html}</{self.tag}>"        

parent_with_props = ParentNode(
    "div",
    [LeafNode("b", "Bold text")],
    {"class": "container"}
)

print(parent_with_props.to_html())