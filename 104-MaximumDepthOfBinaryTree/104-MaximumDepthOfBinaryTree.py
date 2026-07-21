# Last updated: 22/07/2026, 04:25:17
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if not root:
                return 0

            left=1+rec(root.left)
            right=1+rec(root.right)

            return max(left,right)
        return rec(root)