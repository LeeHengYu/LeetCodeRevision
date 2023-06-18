class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        ans = set()  # record pairs
        hash = {}  # rows -> count

        for rows in grid:
            hash[tuple(rows)] = hash.get(tuple(rows), 0)+1

        # loop over the columns
        count = 0
        for c in range(len(grid)):
            col = tuple([grid[i][c] for i in range(len(grid))])

            if tuple(col) in hash:
                count += hash[tuple(col)]
        return count
