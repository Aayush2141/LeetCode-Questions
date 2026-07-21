# Last updated: 22/07/2026, 04:24:24
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        arr1=[]

        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            

        for i in dic:
            arr1.append(dic[i])
        
        print(arr1)

        if len(arr1)==len(set(arr1)):
            return True
        else:
            return False 