# Last updated: 22/07/2026, 04:24:46
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        if n == 1:
            return True

        if n % 3 != 0:
            return False

        quotient = n // 3

        return self.isPowerOfThree(quotient)