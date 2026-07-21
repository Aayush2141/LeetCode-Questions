# Last updated: 22/07/2026, 04:25:40
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x==x[::-1]:
            return True
        else:
            return False
        
        