# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        # If both nodes are None
        if p is None and q is None:
            return True

        # If one is None and the other is not
        if p is None or q is None:
            return False

        # If values are different
        if p.val != q.val:
            return False

        # Compare left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        