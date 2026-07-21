# Last updated: 22/07/2026, 04:24:33
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # def rec(root1,root2,arr1,arr2):
        #     if not root1 and not root2:
        #         return True

        #     if not root1 or not root2:
        #         return False
            
        #     if not root1.left and not root1.right:
        #         arr1.append(root1.val)
            
        #     if not root2.left and not root2.right:
        #         arr2.append(root2.val)
            
        #     rec(root1.left,root2.left,arr1,arr2) 
        #     rec(root1.right,root2.right,arr1,arr2) 

        # rec(root1,root2,[],[])
        # return

        def rec(root,val):
            if not root:
                return
            
            if not root.left and not root.right:
                val.append(root.val)
            
            rec(root.left,val)
            rec(root.right,val)
        
        arr1=[]
        arr2=[]
        rec(root1,arr1)
        rec(root2,arr2)
        return arr1==arr2