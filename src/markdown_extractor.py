import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            result.append(old_node)
            continue
        remaining_text = old_node.text

        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(image_markdown, 1)
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
            result.append(TextNode(alt_text, TextType.IMAGE, url))

            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            result.append(old_node)
            continue
        remaining_text = old_node.text

        for text, url in links:
            link_markdown = f"[{text}]({url})"
            parts = remaining_text.split(link_markdown, 1)
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
            result.append(TextNode(text, TextType.LINK, url))

            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )


def test_split_link(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )