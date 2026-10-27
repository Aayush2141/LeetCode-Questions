# Last updated: 27/10/2026, 16:36:06
1class Solution:
2    def combine(self, n: int, k: int) -> list[list[int]]:
3        visited=[False]*(n+1)
4        result=[]
5        def backtrack(start,current,visited):
6            if len(current)==k:
7                result.append(current[:])
8                return
9            
10            for i in range(start,n+1):
11                if visited[i]:
12                    continue
13                
14                current.append(i)
15                visited[i]=True
16
17                backtrack(i+1,current,visited)
18
19                current.pop()
20                visited[i]=False
21
22                # backtrack(current,visited)
23
24        backtrack(1,[],visited)
25
26        return result
27
28