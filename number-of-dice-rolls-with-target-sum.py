class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(n, rem):
            if rem < 0 or (n == 0 and rem > 0): return 0
            if rem == n == 0: return 1 
            res = 0
            for i in range(1,k+1):
                res += dfs(n-1, rem-i) % MOD
                res %= MOD
            return res
        return dfs(n, target) % MOD