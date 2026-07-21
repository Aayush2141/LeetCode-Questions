# Last updated: 22/07/2026, 04:23:53
class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        temp = n

        while temp:
            rev = rev * 10 + temp % 10
            temp //= 10

        return abs(n - rev)