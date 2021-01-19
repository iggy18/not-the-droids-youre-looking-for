#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        else:
            isSameTree(root.left)
            isSameTree(root.right)
            if p.root.val == q.root.val
                return True
            else:
                return False