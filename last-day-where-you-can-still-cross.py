class Solution:
    def latestDayToCross(self, R: int, C: int, cells: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def validPath(day):
            grid = [[0] * C for _ in range(R)]
            for i in range(day):
                # restore the grid until (day)
                r, c = cells[i]
                grid[r-1][c-1] = 1

            # DFS to check if there is any path
            stack = []
            for c in range(C):
                if grid[0][c] == 0:
                    stack.append((0, c))

            while stack:
                r, c = stack.pop()
                if r == R-1:
                    return True
                for dr, dc in directions:
                    newR, newC = r+dr, c+dc
                    if (newR < 0 or newC < 0 or newR >= R or newC >= C
                            or grid[newR][newC] == 1):
                        continue
                    stack.append((newR, newC))
                    grid[newR][newC] = 1  # avoid double couting

            return False

        # Binary Search
        l, r = 1, R*C
        res = 0
        while l <= r:
            mid = l+(r-l)//2
            if validPath(mid):
                res = max(res, mid)
                l = mid+1
            else:
                r = mid-1
        return res
