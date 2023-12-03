class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)-1):
            x0, y0 = points[i]
            x1, y1 = points[i+1]
            diag = min(abs(x0-x1), abs(y0-y1))
            straight = max(abs(x0-x1), abs(y0-y1))-diag
            res += diag + straight
        return res