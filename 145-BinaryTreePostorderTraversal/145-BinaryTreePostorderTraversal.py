# Last updated: 22/07/2026, 04:25:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        def rec(root):
            if not root:
                return
            
            rec(root.left)
            rec(root.right)
            li.append(root.val)
            return li
        rec(root)
        return li