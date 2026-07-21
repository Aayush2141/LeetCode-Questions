# Last updated: 22/07/2026, 04:24:19
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans