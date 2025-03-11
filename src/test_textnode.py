import unittest
from markdown_extractor import *
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is NOT a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC, url=None)
        node2 = TextNode("This is a text node", TextType.ITALIC, url="https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

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

def test_text_to_textnodes_plain():
    text = "This is plain text"
    nodes = text_to_textnodes(text)
    assert len(nodes) == 1
    assert nodes[0].text == "This is plain text"
    assert nodes[0].text_type == TextType.TEXT

def test_text_to_textnodes_bold():
    text = "This is **bold** text"
    nodes = text_to_textnodes(text)
    assert len(nodes) == 3
    assert nodes[0].text == "This is "
    assert nodes[0].text_type == TextType.TEXT
    assert nodes[1].text == "bold"
    assert nodes[1].text_type == TextType.BOLD
    assert nodes[2].text == " text"
    assert nodes[2].text_type == TextType.TEXT

def test_text_to_textnodes_complex():
    text = "This is **bold** and _italic_ with a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    # Assert the correct number of nodes (7 in this case)
    assert len(nodes) == 7
    # You can add more specific assertions about each node

def test_text_to_textnodes_example():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"



if __name__ == "__main__":
    unittest.main()