from enum import Enum
import re

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.heading
    if block.startswith(">"):
        return BlockType.quote
    if block.startswith("```") and block.endswith("```"):
        return BlockType.code
    if block.startswith("- "):
        return BlockType.unordered_list
    if block[0].isdigit() and block[1] == "." and block[2] == " ":
        return BlockType.ordered_list
    else:
        return BlockType.paragraph
        