# Last updated: 22/07/2026, 04:25:23
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[]

        for i in range(len(matrix)):
            arr+=matrix[i]

        def rec(nums):
            low=0
            high=len(nums)-1

            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return False

        return rec(arr)