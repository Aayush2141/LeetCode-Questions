# Last updated: 22/07/2026, 04:24:53
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if not root:
                return 0
            
            return 1+rec(root.left)+rec(root.right)
        return rec(root)