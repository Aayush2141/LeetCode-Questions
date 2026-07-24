# Last updated: 24/07/2026, 23:05:54
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        narr=[]
4        for i in nums:
5            narr.append(i**2)
6        
7        narr.sort()
8        return narr