# Last updated: 22/07/2026, 04:25:19
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p,q):
            if not q and not p:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            if p and p.val!=q.val:
                return False
            return rec(p.left,q.left) and rec(p.right,q.right)
        return rec(p,q)