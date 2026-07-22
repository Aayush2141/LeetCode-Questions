# Last updated: 23/07/2026, 04:27:47
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        def bs(nums,target):
4            low=0
5            high=len(nums)-1
6            ans=nums[0]
7
8            while low<=high:
9                mid=(low+high)//2
10
11                if nums[mid]>target:
12                    high=mid-1
13                    ans=nums[mid]
14                else:
15                    low=mid+1
16            return ans
17        
18        return bs(letters,target)