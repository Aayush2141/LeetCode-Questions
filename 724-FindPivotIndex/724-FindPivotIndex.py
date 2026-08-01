# Last updated: 01/08/2026, 23:54:43
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total=sum(nums)
4        left=0
5
6        for i in range(len(nums)):
7            right=total-left-nums[i]
8
9            if left==right:
10                return i
11            
12            left+=nums[i]
13        
14        return -1