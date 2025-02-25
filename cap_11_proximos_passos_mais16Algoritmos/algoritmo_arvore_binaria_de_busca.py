class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

tree = BST()
root = None
values = [50, 30, 20, 40, 70, 60, 80]
for v in values:
    root = tree.insert(root, v)

tree.inorder(root)
