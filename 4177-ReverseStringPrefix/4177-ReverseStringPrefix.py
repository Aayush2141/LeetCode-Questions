# Last updated: 22/07/2026, 04:23:52
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        first = s[:k]
        first = first[::-1]
        second = s[k:]
        return first + second