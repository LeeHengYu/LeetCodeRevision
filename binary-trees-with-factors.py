class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        mod = 10**9+7
        A.sort()
        n = len(A)
        s = set(A)
        dp = {x:1 for x in A}
        for i in A:
            for j in A:
                if j > i/2: break
                if i%j==0 and i//j in s:
                    dp[i] += dp[j]*dp[i//j] 
                    dp[i] %= mod
        return sum(dp.values())%mod