class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def preorder(self, start, trace):
        if start:
            trace = trace + str(start.value) + "--"
            trace = self.preorder(start.left, trace)
            trace = self.preorder(start.right, trace)
        return trace

    def postorder(self, start, trace):
        if start is not None:
            trace = self.postorder(start.left, trace)
            trace = self.postorder(start.right, trace)
            trace = trace + str(start.value) + "--"
        return trace

    def inorder(self, start, trace):
        if start:
            trace = self.inorder(start.left, trace)
            trace = trace + str(start.value) + "--"
            trace = self.inorder(start.right, trace)
        return trace

    def find_parent_by_value(self, node, value):
        if node.value == value:
            return node
        if node.left:
            node = self.find_parent_by_value(node.left, value)
        elif node.right:
            node = self.find_parent_by_value(node.right, value)
        return node

root = Node("A")
tree = Tree(root)
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")
tree.root.left.left.left = Node("H")
tree.root.left.left.right = Node("I")
tree.root.right.left = Node("F")
tree.root.right.right = Node("G")
tree.root.right.right.left = Node("J")


print(f"Pre-order: {tree.preorder(start=root, trace="")}")
print(f"In-order: {tree.inorder(start=root, trace="")}")
print(f"Post-order: {tree.postorder(start=root, trace="")}")
print(f"Find Parent: {tree.find_parent_by_value(tree.root, "F")}")