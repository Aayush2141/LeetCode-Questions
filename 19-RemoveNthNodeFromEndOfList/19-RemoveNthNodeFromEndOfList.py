# Last updated: 22/07/2026, 04:25:37
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        cnt = 0

        while curr:
            cnt += 1
            curr = curr.next
        curr = dummy
        
        for i in range(cnt - n):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next