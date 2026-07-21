# Last updated: 22/07/2026, 04:24:15
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)

        return left + middle + right