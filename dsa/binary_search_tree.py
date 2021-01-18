from structures import  treeNode
    

root = treeNode(3)
root.left = treeNode(6)
root.right = treeNode(2)
root.left.left = treeNode(7)
root.left.right = treeNode(10)
root.right.left = treeNode(4)
root.right.right = treeNode(1)

root_two = treeNode(3)
root_two.left = treeNode(6)
root_two.right = treeNode(2)
root_two.left.left = treeNode(7)
root_two.left.right = treeNode(10)
root_two.right.left = treeNode(4)
root_two.right.right = treeNode(1)
root_two.left.left.left = treeNode(12)

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


def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))

print("height tree one", height(root))
print("height tree two", height(root_two))


