# Last updated: 22/07/2026, 04:24:17
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for op in operations:
            if "+" in op:
                x += 1
            else:
                x -= 1

        return x