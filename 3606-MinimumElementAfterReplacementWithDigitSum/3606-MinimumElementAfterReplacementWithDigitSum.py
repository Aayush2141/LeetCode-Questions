# Last updated: 22/07/2026, 04:24:02
class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]

        def dsum(n):
            sumn=0
            while n>0:
                sumn+=n%10
                n//=10
            
            return sumn
        
        for i in nums:
            arr.append(dsum(i))
        
        return min(arr)