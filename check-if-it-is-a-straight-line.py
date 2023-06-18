class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, n):
            x, y = coordinates[i]
            if (y-y0)*(x1-x0) != (y1-y0)*(x-x0):
                return False

        return True
