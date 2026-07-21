# Last updated: 22/07/2026, 04:25:41
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        merged.sort()
        n=len(merged)
        if n%2==1:
             median = merged[n // 2]
        else:
            median=(merged[n//2-1]+merged[n//2])/2
        return median
        