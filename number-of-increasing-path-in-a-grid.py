class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # Standard DFS + recursion with memorisation
        # for 2D DP problems: use caching technique

        m = len(grid)
        n = len(grid[0])
        dp = {}

        def dfs(r, c, prev):
            # base cases
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] <= prev):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            total = 1  # count only this cell
            total += dfs(r+1, c, grid[r][c])
            total += dfs(r-1, c, grid[r][c])
            total += dfs(r, c+1, grid[r][c])
            total += dfs(r, c-1, grid[r][c])

            dp[(r, c)] = total
            return total

        res = 0
        for i in range(m):
            for j in range(n):
                res += dfs(i, j, 0)

        return res % (10**9+7)
