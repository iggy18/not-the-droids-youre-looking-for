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

        def walk_around(node):
            # if there is no node return
            if not node:
                return
            # DO A THING
            node_values.append(node.value)
            # WALK AROUND
            walk_around(node.left)
            walk_around(node.right)
        # calls recursive function
        walk_around(self.root)

class BinarySearchTree:

    def __init__(self):
        self.root = None
    