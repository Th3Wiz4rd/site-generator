from textnode import TextNode, TextType

def main():
    node = TextNode("This is a test node", TextType.BOLD, "https://www.boot.dev")

    print(node)

if __name__ == "__main__":
    main()