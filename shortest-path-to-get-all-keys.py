from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        totalKeys = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    q.append((i, j, 0, tuple()))  # starting point
                elif 'a' <= grid[i][j] <= 'f':
                    totalKeys += 1

        while q:
            r, c, dist, keys = q.popleft()
            if (r < 0 or c < 0 or r >= m or c >= n
                    or (r, c, keys) in visit or grid[r][c] == '#'):  # out of bonund or visited
                continue
            char = grid[r][c]
            if char in 'ABCDEF' and char.lower() not in set(keys):
                continue

            visit.add((r, c, keys))
            newKeys = set(keys)
            if char in 'abcdef':
                newKeys.add(char)
            if len(newKeys) == totalKeys:
                return dist

            q.append((r, c+1, dist+1, tuple(newKeys)))
            q.append((r, c-1, dist+1, tuple(newKeys)))
            q.append((r+1, c, dist+1, tuple(newKeys)))
            q.append((r-1, c, dist+1, tuple(newKeys)))

        return -1
