class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            # Both nodes are empty
            if not left and not right:
                return True

            # One node is empty
            if not left or not right:
                return False

            # Values should match and children should be mirrors
            return (
                left.val == right.val
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)
       
        