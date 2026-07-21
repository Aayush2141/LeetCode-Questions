# Last updated: 22/07/2026, 04:23:59
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr=[]
        for i in order:
            for j in friends:
                if i==j:
                    arr.append(i)
        
        return arr
