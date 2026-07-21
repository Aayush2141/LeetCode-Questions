# Last updated: 22/07/2026, 04:24:29
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val=root.val
        def rec(root):
            nonlocal val
            if not root:
                return True
            
            if root.val!=val:
                return False
            
            return rec(root.left) and rec(root.right)
        return rec(root)

            

        