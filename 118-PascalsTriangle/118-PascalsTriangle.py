# Last updated: 22/07/2026, 04:25:10
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []

        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    left = ans[i - 1][j - 1]
                    right = ans[i - 1][j]
                    row.append(left + right)
            ans.append(row)

        return ans