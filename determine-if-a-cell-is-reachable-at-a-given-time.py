class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx-sx)
        dy = abs(fy-sy)
        if dx>t or dy>t or (dx==0 and dy==0 and t==1): return False
        return True