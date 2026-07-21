# Last updated: 22/07/2026, 04:24:20
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        sumn=0

        for i in range(len(gain)):
            sumn+=gain[i]
            ans=max(ans,sumn)
        
        return ans