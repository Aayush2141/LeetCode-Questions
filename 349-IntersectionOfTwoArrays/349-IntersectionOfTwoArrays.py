# Last updated: 22/07/2026, 04:24:42
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1={}
        dic2={}

        for i in nums1:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1
        
        for i in nums2:
            if i in dic2:
                dic2[i]+=1
            else:
                dic2[i]=1
        

        ans=[]
        for i in dic1:
            if i in dic2:
                ans.append(i)
            
        return ans