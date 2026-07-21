# Last updated: 22/07/2026, 04:25:07
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        for num in freq:
            if freq[num]==1:
                return num
