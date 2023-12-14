from collections import defaultdict

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        RowOnes = defaultdict(int)
        ColOnes = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    RowOnes[i] += 1
                    ColOnes[j] += 1
        for i in range(m):
            for j in range(n):
                # onesRow - zerosRow = onesRow - (n - onesRow)
                # = 2 onesRow - n
                grid[i][j] = 2*RowOnes[i] + 2*ColOnes[j] - n - m
        return grid