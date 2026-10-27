# Last updated: 27/10/2026, 15:14:09
1class Solution:
2    def permute(self, nums: list[int]) -> list[list[int]]:
3        result=[]
4        def backtrack(current,used):
5            if len(current)==len(nums):
6                result.append(current[:])
7                return
8            
9            # current.append(nums[idx])
10            # backtrack(idx+1,current)
11            # current.pop()
12
13            # backtrack(idx+1,current)
14
15            for i in range(len(nums)):
16                if used[i]:
17                    continue
18                
19                current.append(nums[i])
20                used[i]=True
21
22                backtrack(current,used)
23                current.pop()
24                used[i]=False
25            
26        backtrack([],[False]*len(nums))
27
28        return result