# Last updated: 22/07/2026, 04:24:34
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rec(nums):
            low=0
            high=len(nums)-1

            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        
        return rec(nums)
