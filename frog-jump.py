from functools import cache
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1: return False
        @cache
        def dfs(i, k):
            if i==len(stones)-1: return True
            if i>len(stones)-1: return False
            res = False
            for j in range(i+1, len(stones)):
                if stones[i]+k-1==stones[j]:
                    res = res or dfs(j, k-1)
                if stones[i]+k==stones[j]:
                    res = res or dfs(j, k)
                if stones[i]+k+1==stones[j]:
                    res = res or dfs(j, k+1)

            return res
        return dfs(1, 1)