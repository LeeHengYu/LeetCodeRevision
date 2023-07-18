class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        cache = {}
        def dp(i,j):
            if i==n or j==m:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s1[i]==s2[j]:
                res = dp(i+1, j+1)+1
            else:
                res = max(dp(i+1,j), dp(i,j+1))
            cache[(i,j)] = res
            return res
        return dp(0,0)
    
    # caching