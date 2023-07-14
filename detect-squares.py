class DetectSquares:

    def __init__(self):
        self.pts = {}
        # point: count

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pts[(x,y)] = self.pts.get((x,y),0)+1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for pt in self.pts:
            if pt[0]==x and pt!=tuple(point):
                length = abs(pt[1]-y)
                count += self.pts.get((x-length,pt[1]),0)*self.pts.get((x-length,y),0)*self.pts[pt]
                count += self.pts.get((x+length,pt[1]),0)*self.pts.get((x+length,y),0)*self.pts[pt]

        return count