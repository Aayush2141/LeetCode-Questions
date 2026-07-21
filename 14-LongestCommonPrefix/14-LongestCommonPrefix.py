# Last updated: 22/07/2026, 04:25:39
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ss=sorted(strs)

        first=ss[0]
        last=ss[-1]

        limit=min(len(first),len(last))

        result=""
        for i in range(limit):
            if first[i]==last[i]:
                result+=first[i]
            else:
                break

        return result


        