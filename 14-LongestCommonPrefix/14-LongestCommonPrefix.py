# Last updated: 06/08/2026, 01:15:32
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        ss=sorted(strs)
4
5        first=ss[0]
6        last=ss[-1]
7
8        limit=min(len(first),len(last))
9
10        result=""
11        for i in range(limit):
12            if first[i]==last[i]:
13                result+=first[i]
14            else:
15                break
16
17        return result
18
19
20        