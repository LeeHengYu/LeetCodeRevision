from heapq import heappop, heappush
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        res = 0
        # Dijkstra: because we are looking for shortest "something"
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        # pq (diff, r, c)
        pq = [(0, 0, 0)]
        visit = set()
        while True: # loop until we touch R-1,C-1
            curDif, x, y = heappop(pq)
            res = max(res, curDif)
            if x==R-1 and y==C-1: return res
            visit.add((x,y))
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if (nx>=0 and nx<R and ny>=0 and ny<C and (nx,ny) not in visit):
                    newDif = abs(heights[x][y]-heights[nx][ny])
                    heappush(pq, (newDif, nx, ny))