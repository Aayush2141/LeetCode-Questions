# Last updated: 22/07/2026, 04:24:04
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if num % 3 != 0:
                count += 1

        return count