# Last updated: 22/07/2026, 04:25:08
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(root,sumn):
            if not root:
                return 0

            sumn+=str(root.val)
            if not root.left and not root.right:
                return sumn
            
            return int(rec(root.left,sumn))+int(rec(root.right,sumn))
        return int(rec(root,""))