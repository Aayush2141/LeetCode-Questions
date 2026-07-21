# Last updated: 22/07/2026, 04:23:57
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sumn=0
        subt=0

        for i in range(len(nums)):
            if i%2==0:
                sumn+=nums[i]
            else:
                subt+=nums[i]
        
        return sumn-subt