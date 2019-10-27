# AST tree

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

tree = Node('A')
tree.children.append(Node('B'))
tree.children.append(Node('C'))


def print_node_value(value):
    print(value)

def visit(node, handle_node):
    handle_node(node.value)
    for child in node.children:
        visit(child, handle_node)

# tree is from the previous example.
visit(tree, print_node_value)