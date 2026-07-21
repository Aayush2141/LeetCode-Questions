# Last updated: 22/07/2026, 04:25:35
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        Dummy=ListNode(0)
        new=Dummy

        while curr1 and curr2:
            if curr1.val<=curr2.val:
                new.next=curr1
                curr1=curr1.next
            else:
                new.next=curr2
                curr2=curr2.next
            new=new.next
        
        if curr2:
            new.next=curr2
            curr2=curr2.next
            new=new.next
        
        if curr1:
            new.next=curr1
            curr1=curr1.next
            new=new.next

        return Dummy.next

