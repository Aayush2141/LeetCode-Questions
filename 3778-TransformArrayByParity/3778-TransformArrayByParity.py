# Last updated: 22/07/2026, 04:24:01
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in nums:
            if i%2==0:
                arr.append(0)
            else:
                arr.append(1)
        
        arr.sort()
        return arr