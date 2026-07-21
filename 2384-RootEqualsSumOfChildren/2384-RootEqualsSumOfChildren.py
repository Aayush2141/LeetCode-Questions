# Last updated: 22/07/2026, 04:24:14
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # curr=root
        # count=0
        # while curr!=None:
        #     count+=root.val
        #     curr=curr.next

        # if count==root.data:
        #     return True
        # else:
        #     return False

        # def rec(root):
        #     count=0
        #     if root==None:
        #         return
            
        #     count+=root.val
        #     rec(root.left)
        #     rec(root.right)
        #     return count
        
        # a=rec(root)

        # if a-root.val==root.val:
        #     return True
        # else:
        #     return False

        # def rec(root):
        #     count=0
        #     if root==None:
        #         return
        #     if root.left==None or root.right==None:
        #         count+=1
            
        #     rec(root.left)
        #     rec(root.right)
        #     return count
        # a=rec(root)

        # if a-root.val==root.val:
        #     return True
        # else:
        #     return False
        # curr=root
        # curr=root.next
        # count=0
        # while root!=None:
        #     count+=

        if root.val==root.left.val+root.right.val:
            return True
        else:
            return False
                

            
            

            

