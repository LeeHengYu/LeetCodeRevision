class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        RowOnes = [0]*m
        ColOnes = [0]*n
        for r in range(m):
            RowOnes[r] = sum(grid[r])
        for c in range(n):
            ColOnes[c] = sum([ grid[x][c] for x in range(m) ])
            
        for i in range(m):
            for j in range(n):
                # onesRow - zerosRow = onesRow - (n - onesRow)
                # = 2 onesRow - n
                grid[i][j] = 2*RowOnes[i] + 2*ColOnes[j] - n - m
        return grid