class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n=len(obstacleGrid), len(obstacleGrid[0])
        dp = {}
        def dfs(r,c): 
            if r<0 or c<0 or r>=m or c>=n or obstacleGrid[r][c]: 
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            if r==0 and c==0:
                return 1
            res = dfs(r-1,c)+dfs(r,c-1)
            dp[(r,c)]=res
            return res

        return dfs(m-1,n-1)