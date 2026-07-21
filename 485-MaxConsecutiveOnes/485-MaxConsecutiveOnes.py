# Last updated: 22/07/2026, 04:24:38
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        cnt=0
        for i in nums:
            if i==1:
                cnt+=1
            else:
                cnt=0
            ans=max(cnt,ans)
        return ans
