# Last updated: 22/07/2026, 04:25:33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        k=-1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                k=i
                break
        
        if k==-1:
            k=len(nums)-1

        def before(nums):
            low=0
            high=k

            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
                
            return -1
        
        def after(nums):
            low=k+1
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
        

        if (before(nums))!=-1:
            return before(nums)
        return after(nums)

            
        