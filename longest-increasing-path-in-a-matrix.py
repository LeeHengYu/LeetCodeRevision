class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DP + DFS
        # if not caching => TLE
        cache = {} # (r,c) => length
        m, n = len(matrix), len(matrix[0])

        def dfs(r,c,prev):
            if (r<0 or r>=m or c<0 or c>=n
                or matrix[r][c]<=prev):
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            top = dfs(r-1,c,matrix[r][c])
            bot = dfs(r+1,c,matrix[r][c])
            left = dfs(r,c-1,matrix[r][c])
            right = dfs(r,c+1,matrix[r][c])
            res = 1+max(top, bot, left, right)
            cache[(r,c)] = res
            return res

        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(dfs(i,j,-1), ans)
        return ans