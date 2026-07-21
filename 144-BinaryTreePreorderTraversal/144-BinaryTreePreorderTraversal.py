# Last updated: 22/07/2026, 04:25:02
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        def rec(root):
            if not root:
                return 
            
            li.append(root.val)
            rec(root.left)
            rec(root.right)
            return li
        rec(root)
        return li