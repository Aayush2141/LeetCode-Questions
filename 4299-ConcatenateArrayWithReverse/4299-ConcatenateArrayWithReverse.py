# Last updated: 22/07/2026, 04:23:48
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev=nums.copy()
        rev.reverse()
        return nums+rev