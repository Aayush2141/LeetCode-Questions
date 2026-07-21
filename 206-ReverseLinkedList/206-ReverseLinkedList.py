# Last updated: 22/07/2026, 04:24:56
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        arr=[]

        if head.next==None:
            return head

        while curr!=None:
            arr.append(curr.val)
            curr=curr.next
        
        arr.reverse()
        curr=head

        for i in range(len(arr)):
            curr.val=arr[i]
            curr=curr.next
        
        return head