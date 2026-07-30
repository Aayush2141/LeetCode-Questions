# Last updated: 31/07/2026, 00:17:35
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        left = []
4        middle = []
5        right = []
6
7        for num in nums:
8            if num < pivot:
9                left.append(num)
10            elif num == pivot:
11                middle.append(num)
12            else:
13                right.append(num)
14
15        return left + middle + right