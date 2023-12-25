from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        # backtracking
        n = len(s)
        @cache
        def dfs(i):
            if i == n: return 1
            if s[i] == '0': return 0
            res = 0
            res += dfs(i+1)
            if i+1 < n and ((s[i] == '1') or s[i] == '2' and 0<=int(s[i+1])<=6):
                res += dfs(i+2)
            return res

        return dfs(0)