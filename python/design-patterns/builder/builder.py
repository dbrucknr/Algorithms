# Manufacture HTML from Python

# Easy - Create a paragraph
text = "hello world"
parts = ["<p>", text, "</p>"]
print("".join(parts))

# More complicated: Create a list of words in HTML
words = ["hello", "world", "foo", "bar", "baz"]
parts = ["<ul>"]
for word in words:
    parts.append(f" <li>{word}</li>")
parts.append("</ul>")
print("\n".join(parts))

# Outsource the logic:
class HTMLElement:
    """Helper Module for the Builder"""
    indent_size = 2

    def __init__(self, name="", text="") -> None:
        self.name = name
        self.text = text
        self.elements = [] #Child HTML Elements

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for element in self.elements:
            lines.append(element.__str(indent + 1))
    
        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create(name):
        # Appears to break the open-closed principle..it does, 
        # but the Builder is entangled to the Element
        return HTMLBuilder(name)

class HTMLBuilder:
    __root = HTMLElement()

    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.__root.name = root_name

    # Not chainable (not fluent)
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HTMLElement(child_name, child_text)
        )

    # Chainable calls (fluent)
    def add_child_fluently(self, child_name, child_text):
        self.__root.elements.append(
            HTMLElement(child_name, child_text)
        )
        return self

    def clear(self):
        self.__root = HTMLElement(name=self.root_name)

    def __str__(self) -> str:
        return str(self.__root)

builder = HTMLElement.create("ul")

# Non-Fluent Use:
builder.add_child("li", "foo")
builder.add_child("li", "bar")
print("Ordinary, non-fluent builder")
print(builder)

builder.clear()

# Fluent Use
builder.add_child_fluently(
    "li", "foo-fluent"
    ).add_child_fluently(
        "li", "bar-fluent"
    )
print('Fluent builder:')
print(builder)