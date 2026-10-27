# Last updated: 27/10/2026, 11:37:19
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        result=[]
4        def backtrack(index,current):
5            if index==len(nums):
6                result.append(current[:])
7                return
8            
9            current.append(nums[index])
10            backtrack(index+1,current)
11            current.pop()
12
13            backtrack(index+1,current)
14        
15        backtrack(0,[])
16        return result
17