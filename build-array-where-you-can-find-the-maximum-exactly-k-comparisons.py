class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # dp
        MOD = 10**9+7
        @cache
        def dfs(i,prevMax,k):
            if i==n: #finish construction
                if k==0: # used up all costs
                    return 1
                return 0
            res = 0
            # recursion
            for nxt in range(1,m+1):
                if nxt > prevMax:
                    res += dfs(i+1, nxt, k-1)
                else:
                    res += dfs(i+1, prevMax, k)
            res %= MOD
            return res
        return dfs(0,-1,k)