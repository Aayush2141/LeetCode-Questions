# Last updated: 22/07/2026, 04:24:26
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
#         count=0
#         def rec(root):
#             nonlocal count
#             if not root:
#                 return 
#             if root.left==None or root.right==None:
#                 count+=root.val
            
#             rec(root.left)
#             rec(root.right)

#             return count
#         rec(root)
#         return count
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        maxDepth = -1

        def rec(root, depth):
            nonlocal ans, maxDepth

            if not root:
                return

            if not root.left and not root.right:
                if depth > maxDepth:
                    maxDepth = depth
                    ans = root.val
                elif depth == maxDepth:
                    ans += root.val
                return

            rec(root.left, depth + 1)
            rec(root.right, depth + 1)

        rec(root, 0)
        return ans