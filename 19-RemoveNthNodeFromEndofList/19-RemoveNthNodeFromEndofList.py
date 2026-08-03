# Last updated: 04/08/2026, 01:55:52
1class Solution:
2    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
3        dummy = ListNode(0, head)
4        curr = head
5        cnt = 0
6
7        while curr:
8            cnt += 1
9            curr = curr.next
10        curr = dummy
11        
12        for i in range(cnt - n):
13            curr = curr.next
14
15        curr.next = curr.next.next
16        return dummy.next