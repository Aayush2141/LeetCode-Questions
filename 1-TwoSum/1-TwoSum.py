# Last updated: 22/07/2026, 04:25:42
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        arr=[]
        # for i in nums:
        #     if i in dic:
        #         dic[i]+=1
        #     else:
        #         dic[i]=1
        
        for i in range(len(nums)):
            val=target-nums[i]

            if val in dic:
                return [i,dic[val]]
            else:
                dic[nums[i]]=i

        return arr
