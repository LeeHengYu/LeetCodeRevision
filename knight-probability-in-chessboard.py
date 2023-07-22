class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # DFS
        cache = {}
        directions = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
        def dfs(r,c,k):
            if k == 0:
                if (r>=0 and r<n and c>=0 and c<n): return 1
            if (r<0 or r>=n or c<0 or c>=n): return 0

            if (r,c,k) in cache:
                return cache[(r,c,k)]

            res = 0
            for dx, dy in directions:
                newR, newC = r+dx, c+dy
                res += dfs(newR,newC,k-1)
            cache[(r,c,k)] = res
            return res

        ALL = 8**k
        return dfs(row, column, k)/ALL