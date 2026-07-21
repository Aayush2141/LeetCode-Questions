# Last updated: 22/07/2026, 04:25:11
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root==None):
            return False
        def rec1(cnt,root):
            if(root==None):
                # if(cnt==targetSum) :
                #     return True
                return False
            if(root.left==None and root.right==None):
                cnt+=root.val
                if(cnt==targetSum):
                    return True
                return False
            return rec1(cnt+root.val,root.left) or rec1(cnt+root.val,root.right)
        return rec1(0,root)
            
            


            
