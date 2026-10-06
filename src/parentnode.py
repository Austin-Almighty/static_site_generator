from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag value not found!")
        if self.children is None:
            raise ValueError("No children nodes found!")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        output = f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

        return output

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag!r}, children={self.children}, props={self.props})"
