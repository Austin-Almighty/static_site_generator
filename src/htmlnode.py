from dataclasses import dataclass


@dataclass
class HTMLNode:
    tag: str|None = None
    value: str|None = None
    children: list["HTMLNode"]|None = None
    props: dict|None = None

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            return "".join(f' {key}="{val}"' for key, val in self.props.items())
        return ""

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children}, props={self.props})"
