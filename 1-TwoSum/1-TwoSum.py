# Last updated: 03/08/2026, 03:43:45
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dic={}
4        arr=[]
5        # for i in nums:
6        #     if i in dic:
7        #         dic[i]+=1
8        #     else:
9        #         dic[i]=1
10        
11        for i in range(len(nums)):
12            val=target-nums[i]
13
14            if val in dic:
15                return [i,dic[val]]
16            else:
17                dic[nums[i]]=i
18
19        return arr
20