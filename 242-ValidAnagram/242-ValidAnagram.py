# Last updated: 22/07/2026, 04:24:49
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        dic1={}
        dic2={}

        for i in s:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1

        for j in t:
            if j in dic2:
                dic2[j]+=1
            else:
                dic2[j]=1

        if dic1==dic2:
            return True
        else:
            return False