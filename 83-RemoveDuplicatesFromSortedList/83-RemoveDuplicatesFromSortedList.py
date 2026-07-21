# Last updated: 22/07/2026, 04:25:22
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head

        while curr:
            if curr.next and curr.val==curr.next.val:
                # data=curr.val
                # while curr and curr.val==data:
                #     curr=curr.next
                # prev=prev.next
                curr.next=curr.next.next
            else:
                curr=curr.next

        return dummy.next
