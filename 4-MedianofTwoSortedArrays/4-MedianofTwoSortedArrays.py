# Last updated: 28/07/2026, 02:41:24
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        merged=nums1+nums2
4        merged.sort()
5        n=len(merged)
6        if n%2==1:
7             median = merged[n // 2]
8        else:
9            median=(merged[n//2-1]+merged[n//2])/2
10        return median
11        