# Last updated: 22/07/2026, 04:24:59
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        arr=[]
        new=ListNode(0)
        Dummy=new
        while curr:
            arr.append(curr.val)
            curr=curr.next
        
        arr.sort()

        for i in range(len(arr)):
            Dummy.next=ListNode(arr[i])
            Dummy=Dummy.next

        return new.next
