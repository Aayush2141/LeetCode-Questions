# Last updated: 22/07/2026, 04:25:25
class Solution:
    def mySqrt(self, x: int) -> int:
        def FindSqrt(x):
            ans=0
            low=0
            high=x

            while low<=high:
                mid=(low+high)//2
                if (mid*mid)<=x:
                    ans=mid
                    low=mid+1
                elif mid*mid>x:
                    high=mid-1
                else:
                    low=mid+1
            return ans
        return FindSqrt(x)