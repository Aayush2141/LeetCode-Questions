# Last updated: 08/09/2026, 15:29:28
1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        ans=[]
4        curr=[]
5        def backtrack(k,n,curr,ans,start):
6            if len(curr)==k:
7                if n==0:
8                    ans.append(curr[:])
9                    return
10                return 
11            
12            for i in range(start,10):
13                curr.append(i)
14                backtrack(k,n-i,curr,ans,i+1)
15                curr.pop()
16        
17        backtrack(k,n,curr,ans,1)
18        return ans