# Last updated: 22/07/2026, 04:24:31
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr=head
        length=0

        while curr!=None:
            length+=1
            curr=curr.next
        
        curr=head
        for i in range(length//2):
            curr=curr.next
        
        return curr

        