class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # calculate distance to thieves: BFS
        # calculate max score: negated Dijkstra
        n = len(grid)
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i,j,i,j))
        dis = [[0 for i in range(n)] for j in range(n)]
        # calculate depth
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        visit = set()
        while queue:
            px, py, tx, ty = queue.pop(0)
            if (px, py) in visit: continue
            visit.add((px,py))
            dis[px][py] = abs(px-tx)+abs(py-ty)
            for dx,dy in dirs:
                cx, cy = px+dx, py+dy
                if 0<=cx<n and 0<=cy<n and (cx,cy) not in visit:
                    queue.append((cx,cy,tx,ty))

        # dijkstra
        visit = set()
        pq = [[-dis[0][0], 0, 0]] # distance, r, c; we always wants the largest dist
        while pq:
            dist, i, j = heapq.heappop(pq)
            if (i,j) not in visit:
                visit.add((i,j))
                if i==n-1 and j==n-1:
                    return -dist
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=x<n and 0<=y<n:
                        heapq.heappush(pq, [-min(-dist, dis[x][y]), x, y])
        return 0