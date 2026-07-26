# Last updated: 27/07/2026, 02:42:52
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        dic1={}
4        dic2={}
5
6        for i in nums1:
7            if i in dic1:
8                dic1[i]+=1
9            else:
10                dic1[i]=1
11        
12        for i in nums2:
13            if i in dic2:
14                dic2[i]+=1
15            else:
16                dic2[i]=1
17        
18
19        ans=[]
20        for i in dic1:
21            if i in dic2:
22                ans.append(i)
23            
24        return ans