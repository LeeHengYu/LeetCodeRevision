class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'W': (-1, 0), 'E':(1, 0), 'S': (0, -1), 'N': (0, 1)} # W E S N
        X = Y = 0
        seen = set([(0,0)])
        for d in path:
            X += directions[d][0]
            Y += directions[d][1]
            if (X,Y) in seen: return True
            seen.add((X,Y))
        return False