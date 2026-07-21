# Last updated: 22/07/2026, 04:23:49
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        arr=[]
        for i in matrix:
            cnt=0
            for j in i:
                if j==1:
                    cnt+=1
            arr.append(cnt)
        
        return arr
