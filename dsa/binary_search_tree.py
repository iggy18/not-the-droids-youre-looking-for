class Node:

    def __init__(self, value,):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        # traversals are walking around and doing stuff.
        node_values = []

        def walk_around(root):
            # if there is no root return
            if not root:
                return
            # DO A THING
            node_values.append(root.value)
            # WALK AROUND
            walk_around(root.left)
            walk_around(root.right)
        # calls recursive function
        walk_around(self.root)

class BinarySearchTree:

    def __init__(self):
        self.root = None
    