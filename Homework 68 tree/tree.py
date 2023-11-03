from abc import ABC, abstractmethod


class BinarySearchTree(ABC):
    def __init__(self, root=None):
        self.root = root

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def find_min(self):
        pass

    @abstractmethod
    def search(self, value):
        pass


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class MyBinarySearchTree(BinarySearchTree):

    def __init__(self, root=None):
        super().__init__(root)
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def remove(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return self._remove(current)
            elif value < current.value:
                current = current.left
            else:
                current = current.right

    def _remove(self, node):
        if node.left is None and node.right is None:
            return None
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        successor = self._min_value_node(node.right)
        successor.right = self._remove_min(node.right)
        successor.left = node.left
        return successor

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _remove_min(self, node):
        if node.left is None:
            return node.right
        else:
            node.left = self._remove_min(node.left)
            return node

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False





root = Node(12)
tree = MyBinarySearchTree(root)
tree.insert(8)
tree.insert(19)
tree.insert(4)
tree.insert(10)
tree.insert(5)
tree.insert(9)
tree.insert(11)
tree.insert(15)
tree.insert(21)
tree.insert(14)
tree.insert(16)

print(tree.find_min())
tree.remove(11)
print(tree.find_min())
tree.remove(10)
print(tree.find_min())
tree.remove(12)
print(tree.find_min())