# Last updated: 22/07/2026, 04:25:18
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False

            return rec(root1.left,root2.right) and rec(root1.right,root2.left)
        if not root:
            return True
        
        return rec(root.left,root.right)























        # def rec(root):
        #     if not root.left or not root.right:
        #         return False
        #     if not root.left and not root.right:
        #         return False
        #     if root.left.val!=root.right.val:
        #         return False
        #     if root.right.val!=root.left.val:
        #         return False
        #     if not root.left and not root.right:
        #         return
        #     rec(root.left)
        #     rec(root.right)
        #     return True
        # return rec(root)
        # def is_mirror(root1,root2):
            # if root1==None and root2==None:
            #     return True 
            # if root1==None or root2==None:
            #     return False
            # if root1.val==root2.val and is_mirror(root1.left,root2.right) and is_mirror(root1.right,root2.left):
            #     return True 
            # else:
            #     return False
            # if not root1 and not root2:
            #     return True
            # if not root1 or not root2:
            #     return False
            # if root1.val!=root2.val:
            #     return False
            # if root1.right!=root2.left:
            #     return False
            # return is_mirror(root1.left,root2.right) and is_mirror(root2.left,root1.right)
        # if not root:
        #     return True
        # return is_mirror(root.left,root.right)