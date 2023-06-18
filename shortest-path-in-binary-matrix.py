class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0]:
            return -1
        # bfs
        n = len(grid)
        visit = set()
        direction = [[-1, -1], [-1, 0], [-1, 1],
                     [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        visit.add((0, 0))
        q = []
        q.append((0, 0))

        curlen = 0
        while q:
            L = len(q)
            curlen += 1
            for i in range(L):
                R, C = q.pop(0)
                if R == n-1 and C == n-1:
                    return curlen
                for dr, dc in direction:
                    neiR, neiC = R+dr, C+dc
                    if (neiR < 0 or neiC < 0 or neiR >= n or neiC >= n
                            or (neiR, neiC) in visit or grid[neiR][neiC]):
                        continue
                    q.append((neiR, neiC))
                    visit.add((neiR, neiC))

        return -1
