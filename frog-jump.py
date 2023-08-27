from bisect import bisect_left
from functools import cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1: return False
        @cache
        def dfs(i, k):
            if i==len(stones)-1: return True
            res = False
            for jump in (k,k+1,k-1):
                idx = bisect_left(stones, stones[i]+jump, lo=i+1)
                if idx<len(stones) and stones[i]+jump==stones[idx]:
                    res = res or dfs(idx, jump)
            return res
        return dfs(1, 1)