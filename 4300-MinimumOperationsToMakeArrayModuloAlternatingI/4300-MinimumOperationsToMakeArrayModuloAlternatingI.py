# Last updated: 22/07/2026, 04:23:47
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        ans=float('inf')
        for x in range(k):
            for y in range(k):

                if x==y:
                    continue

                ops=0

                for i in range(len(nums)):
                    rem=nums[i]%k

                    if i%2==0:
                        target=x
                    else:
                        target =y

                    ops+=min((rem-target)%k,(target-rem)%k)

                ans=min(ans,ops)

        return ans