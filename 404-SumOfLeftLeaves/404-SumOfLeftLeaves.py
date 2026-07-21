# Last updated: 22/07/2026, 04:24:40
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        cnt=0
        def rec(root):
            nonlocal cnt
            if not root:
                return
            
            if root.left and root.left.left==None and root.left.right==None:
                cnt+=root.left.val
            rec(root.left)
            rec(root.right)
            return cnt
        rec(root)
        return cnt