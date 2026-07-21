# Last updated: 22/07/2026, 04:23:45
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        cnt=0
        zeroes=nums.count(0)

        for i in range(len(nums)-zeroes):
            if nums[i]==0:
                cnt+=1

        return cnt
        