class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            if not r or not c:
                return 1
            dp[(r,c)] = dfs(r-1,c)+dfs(r,c-1)
            return dp[(r,c)]

        return dfs(m-1,n-1)