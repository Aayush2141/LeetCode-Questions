# Last updated: 22/07/2026, 04:23:43
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        arr2=[]
        for i in nums:
            if len(arr2)<k or arr2[-k]!=i:
                arr2.append(i)

        return arr2
           
           