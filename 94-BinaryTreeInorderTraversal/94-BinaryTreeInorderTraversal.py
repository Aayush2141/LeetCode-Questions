# Last updated: 22/07/2026, 04:25:20
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        def rec(root):
            if not root:
                return []
            
            rec(root.left)
            li.append(root.val)
            rec(root.right)
            return li
        return rec(root)

            
        