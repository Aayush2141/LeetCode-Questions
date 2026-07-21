# Last updated: 22/07/2026, 04:25:32
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first (nums):
            low=0
            high=len(nums)-1
            ans=-1

            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        
        def last(nums):
            low=0
            high=len(nums)-1
            ans=-1

            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        
        return [first(nums),last(nums)]