from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    # Start with a single TextNode with the entire text
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Process bold text (with **)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # Process italic text (with _)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # Process code text (with `)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Process other types as needed
    
    return nodes