# Last updated: 22/07/2026, 04:24:23
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def bs(nums):
            low = 0
            high = len(nums) - 1
            ans = len(nums)

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] < 0:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return len(nums) - ans

        count = 0

        for row in grid:
            count += bs(row)

        return count