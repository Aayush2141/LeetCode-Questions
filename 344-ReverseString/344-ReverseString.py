# Last updated: 22/07/2026, 04:24:43
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1

        while left<right:
            s[left],s[right]=s[right],s[left]

            left=left+1
            right=right-1
        return s
        