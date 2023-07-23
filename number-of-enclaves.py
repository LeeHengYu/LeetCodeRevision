class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # dfs from grid edge
        m, n = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visit or grid[r][c]==0:
                return
            grid[r][c]=0
            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    dfs(i,j)
        return sum( [sum(grid[i]) for i in range(m)] )