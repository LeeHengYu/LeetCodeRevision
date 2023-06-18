class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        res = 0
        for c in range(n-1, -1, -1):
            if grid[m-1][c] >= 0:
                break
            for r in range(m-1, -1, -1):
                if grid[r][c] < 0:
                    res += 1
                else:
                    break

        return res
