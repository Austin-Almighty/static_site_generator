from htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, tag:str|None, value: str, props: dict[str, str]|None=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node: value required")
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
            return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props})"