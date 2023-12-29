from functools import cache
from math import inf

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        @cache
        def dfs(i, day):
            if i == n:
                return 0 if day == d else inf # finish all tasks using day 0, 1, ..., d-1 (d days in total)
            if day == d:
                return inf
            
            dayMax = 0
            res = inf
            for j in range(i, n): # consider every possible ending of the day
                dayMax = max(dayMax, jobDifficulty[j])
                res = min(res, dayMax + dfs(j+1, day+1))
            return res

        res = dfs(0,0)
        return -1 if res == inf else res