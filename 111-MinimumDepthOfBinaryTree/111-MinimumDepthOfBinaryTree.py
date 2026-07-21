# Last updated: 22/07/2026, 04:25:12
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if not root.left:
                return 1 + rec(root.right)
            if not root.right:
                return 1 + rec(root.left)
            return 1 + min(rec(root.left), rec(root.right))
        return rec(root)