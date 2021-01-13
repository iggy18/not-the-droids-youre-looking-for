class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

root = Node(3)
root.left = Node(6)
root.right = Node(2)
root.left.left = Node(7)
root.left.right = Node(10)
root.right.left = Node(4)
root.right.right = Node(1)

def tree_val(root):
    nums = []
    def walk(root):
        if not root:
            return "empty tree"
        nums.append(root.val)
        walk(root.left)
        walk(root.right)
    walk(root)
    return nums

print("print", tree_val(root))

def vals_between(root):
    nums = []
    def walk(root):
        if not root:
            return "empty tree"
        if root.val > 4 and root.val < 10:
            nums.append(root.val)
            walk(root.left)
            walk(root.right)
    walk(root)
    return nums

print("between", vals_between(root))

def add(root):
    if not root: 
        return 0
    return root.val + add(root.left) + add(root.right)


print("add", add(root))

def matching_parent_and_children(root, value):
    if not root:
        return "not in tree"
    matching_parent_and_children(root.left, 2)
    matching_parent_and_children(root.right, 2)
    if root.val == value:
        return(root.val, root.left.val, root.right.val)

print(matching_parent_and_children(root, 2))