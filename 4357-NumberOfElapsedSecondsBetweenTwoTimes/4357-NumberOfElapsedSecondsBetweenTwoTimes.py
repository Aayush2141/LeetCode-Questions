# Last updated: 22/07/2026, 04:23:44
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:

        def conv(n):
            h,m,s=map(int,n.split(":"))
            return 3600*h+60*m+s

        return conv(endTime)-conv(startTime)