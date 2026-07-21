# Last updated: 22/07/2026, 04:23:40
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dic={}
        arr=list(map(int, str(n)))
        sumn=0

        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for i in dic:
            sumn+=i*dic[i]

        return sumn