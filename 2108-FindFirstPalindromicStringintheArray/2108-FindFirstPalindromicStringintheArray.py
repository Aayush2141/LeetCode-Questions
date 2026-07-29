# Last updated: 30/07/2026, 01:18:02
1class Solution:
2    def firstPalindrome(self, words: List[str]) -> str:
3        def checker(s):
4            left=0
5            right=len(s)-1
6
7            while left<=right:
8                if s[left]!=s[right]:
9                    return False
10                left+=1
11                right-=1
12            return True
13
14        for word in words:
15            if checker(word):
16                return word
17
18        return ""
19
20