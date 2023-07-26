from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)>ceil(hour): return -1
        def canReach(speed):
            time = 0
            for i in range(len(dist)-1):
                time += ceil(dist[i]/speed)
                if time>hour:
                    return False
            return (time+dist[-1]/speed)<=hour

        # binary search
        l, h = 1, 10**7
        res = 10**7
        while l<=h:
            m = (l+h)//2
            if canReach(m):
                h=m-1
                res = min(res, m)
            else:
                l=m+1
        return res