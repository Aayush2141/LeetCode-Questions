# Last updated: 22/07/2026, 04:25:26
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        lens=len(words[-1])
        return lens
        