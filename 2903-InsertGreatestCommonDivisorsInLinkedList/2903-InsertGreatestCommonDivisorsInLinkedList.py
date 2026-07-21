# Last updated: 22/07/2026, 04:24:09
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)

            newNode = ListNode(g)
            newNode.next = curr.next
            curr.next = newNode

            curr = newNode.next

        return head